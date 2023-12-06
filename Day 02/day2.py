constraint = {'red': 12, 'green': 13, 'blue': 14}

def get_games(file):
    lines = open(file).read().splitlines()
    games = [item.split(": ")[1].split("; ") for item in lines]
    return_games = list()
    for game in games:
        return_game = list()
        for configuration in game:
            return_configuration = dict()
            aux_configuration = configuration.split(", ")
            for box_count in aux_configuration:
                aux_box = box_count.split(" ")
                return_configuration[aux_box[1]] = int(aux_box[0])
            return_game.append(return_configuration)
        return_games.append(return_game)
    return return_games

def check_game_possible(game, constraint):
    for configuration in game:
        for key in configuration.keys():
            if configuration[key] > constraint[key]:
                return False
    return True

def possible_games(games, constraint):
    result = 0
    for i, game in enumerate(games):
        result += (i + 1) * int(check_game_possible(game, constraint))
    return result

def get_game_power(game):
    import math
    minimum_possibles = {'red': 0, 'green': 0, 'blue': 0}
    for configuration in game:
        for key in configuration.keys():
            minimum_possibles[key] = max(configuration[key], minimum_possibles[key])
    return math.prod(minimum_possibles.values())

print("Part 1: ", possible_games(get_games("input.txt"), constraint))
print("Part 2: ", sum(get_game_power(game) for game in get_games("input.txt")))