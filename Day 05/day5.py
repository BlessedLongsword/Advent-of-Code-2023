maps = {'seed': 'soil', 'soil': 'fertilizer', 'fertilizer': 'water',
            'water': 'light', 'light': 'temperature', 'temperature': 'humidity',
            'humidity': 'location'}

def get_almanac(file):
    almanac = dict()
    almanac_literal = [line.rstrip()
                       for line in open(file).read().splitlines() if line]
    seeds = list(map(int, almanac_literal[0].split(' ')[1:]))
    for map_ in maps.keys():
        current_map = map_ + '-to-' + maps[map_] + ' map:'
        if map_ == 'humidity':
            map_range_groups = almanac_literal[almanac_literal.index(current_map) + 1:]
        else:
            next_map = maps[map_] + '-to-' + maps[maps[map_]] + ' map:'
            map_range_groups = almanac_literal[almanac_literal.index(current_map) + 1: almanac_literal.index(next_map)]
        almanac[map_] = [tuple(map(int, range_group.split(' '))) for range_group in map_range_groups]
    return seeds, almanac

def get_seed_location(seed, almanac):
    location_flow = dict()
    location_flow['seed'] = seed
    current_val = seed
    for map_ in almanac.keys():
        current_val = evaluate_coord_in_map(current_val, map_, almanac)
        location_flow[maps[map_]] = current_val
    return location_flow

def evaluate_coord_in_map(coord, map, almanac):
    for dest, source, range_ in almanac[map]:
        if source <= coord <= source + range_:
            return dest + coord - source
    return coord

def get_min_location(seeds, almanac):
    return min([get_seed_location(seed, almanac)['location'] for seed in seeds])

def process_interval(interval, map_, almanac, min_values):
    destination_intervals = get_destinations_from_interval(interval, map_, almanac)
    if maps[map_] == 'location':
        min_values.append(min([destination_interval[0] for destination_interval in destination_intervals]))
    else:
        for destination_interval in destination_intervals:
            process_interval(destination_interval, maps[map_], almanac, min_values)

def get_destinations_from_interval(interval, map_, almanac):
    new_intervals = [interval]
    dest_intervals = list()
    for dest, source, range_ in almanac[map_]:
        aux_new_intervals = list()
        for split, eval in [split_eval for split_eval in split_intervals(new_intervals, source, range_)]:
            if eval:
                dest_intervals.append([dest + split[0] - source, dest + split[1] - source])
            else:
                aux_new_intervals.append(split)
        new_intervals = [aux_interval for aux_interval in aux_new_intervals]
    for new_interval in new_intervals:
        dest_intervals.append(new_interval)            
    return dest_intervals

def split_intervals(interval_list, source, range_):
    result = list()
    for interval in interval_list:
        for split, eval in split_interval(interval, source, range_):
            result.append((split, eval))
    return result
        
def split_interval(interval, source, range_):
    if interval[1] < source or interval[0] > source + range_ - 1:
        return [(interval, False)]
    elif interval[0] >= source and interval[1] <= source + range_ - 1:
        return [(interval, True)]
    elif interval[0] >= source and interval[1] > source + range_ - 1:
        return [([interval[0], source + range_ - 1], True), ([source + range_, interval[1]], False)]
    elif interval[0] < source and interval[1] <= source + range_ - 1:
        return [([interval[0], source - 1], False), ([source, interval[1]], True)]
    else:
        return [([interval[0], source - 1], False), ([source, source + range_ - 1], True), ([source + range_, interval[1]], False)]


def get_min_location_nightmare(seeds, almanac):
    seeds = [[seeds[i], seeds[i] + seeds[i+1] - 1] for i in range(0, len(seeds), 2)]
    min_values = list()
    for seed in seeds:
        process_interval(seed, 'seed', almanac, min_values)
    return min(min_values)

#print(get_min_location(*get_almanac("input.txt")))
print(get_min_location_nightmare(*get_almanac("input.txt")))
