def get_schematic(file):
    return list(map(list, open(file).read().splitlines()))

def get_schematic_numbers(schematic):
    schematic_numbers = list()
    for i, line in enumerate(schematic):
        in_number = False
        current_number = ""
        first_index = 0
        for j, char in enumerate(line):
            if char.isdigit():
                first_index = (i, j) if not in_number else first_index
                in_number = True if not in_number else in_number
                current_number += char
                if j == len(line) - 1:
                    schematic_numbers.append((int(current_number), first_index))
                    in_number = False
                    current_number = ""
                    first_index = 0
            else:
                if in_number:
                    schematic_numbers.append((int(current_number), first_index))
                    in_number = False
                    current_number = ""
                    first_index = 0
    return schematic_numbers

def get_schematic_gears(schematic):
    schematic_gears = dict()
    for i, line in enumerate(schematic):
        for j, char in enumerate(line):
            if char == '*':
                schematic_gears[(i, j)] = list()
    return schematic_gears
    

def check_is_part(number, index, schematic, schematic_gears):
    vstart = index[0] - 1 if index[0] > 0 else index[0]
    vend = index[0] + 1 if index[0] < len(schematic) - 1 else index[0]
    hstart = index[1] - 1 if index[1] > 0 else index[1]
    hend = index[1] + len(str(number)) if index[1] + len(str(number)) < len(schematic[0]) else index[1] + len(str(number)) - 1
    for i in range(vstart, vend + 1):
        for j in range(hstart, hend + 1):
            if (schematic[i][j] != '.' and not schematic[i][j].isdigit()):
                if (schematic[i][j] == '*'):
                    schematic_gears[(i, j)].append(number)
                return True
    return False
    
def sum_part_numbers(file):
    result = 0
    gear_result = 0
    schematic = get_schematic(file)
    schematic_numbers = get_schematic_numbers(schematic)
    schematic_gears = get_schematic_gears(schematic)
    for schematic_number in schematic_numbers:
        result += schematic_number[0] * int(check_is_part(schematic_number[0], schematic_number[1], schematic, schematic_gears))
    for value in schematic_gears.values():
        if len(value) == 2:
            gear_result += value[0] * value[1]
    return "Part 1: " + str(result) + "\nPart 2: " + str(gear_result)

print((sum_part_numbers("input.txt")))