import re
from math import floor, ceil, prod, sqrt

def get_records(file):
    records = list()
    input_ = open(file).read().splitlines()
    times = list(map(int, re.split("\s+", input_[0].split(":")[1])[1:]))
    distances = list(map(int, re.split("\s+", input_[1].split(":")[1])[1:]))
    for time, distance in zip(times, distances):
        records.append((time, distance))
    return records

def get_record_corrected_kerning(file):
    records = get_records(file)
    time, dist = "", ""
    for time_, dist_ in records:
        time += str(time_)
        dist += str(dist_)
    return [(int(time), int(dist))]


def get_possible_wins(time, distance):
    min_root, max_root = solve_equation(1, -time, distance)
    return ceil(max_root - 1) - floor(min_root + 1) + 1
    
def solve_equation(a, b, c):
    disc = abs(b * b) - 4 * a * c
    return ((-b - sqrt(disc)) / (2*a), (-b + sqrt(disc)) / (2*a))

def get_error_margin(records):
    return prod([get_possible_wins(*record) for record in records])
    
    
print(get_error_margin(get_records("input.txt")))
print(get_error_margin(get_record_corrected_kerning("input.txt")))