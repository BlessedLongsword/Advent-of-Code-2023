def trabuchet(file):
    result = 0
    for line in open(file).read().splitlines():
        reformatted_line = reformat(line)
        first_number = True
        line_result = ""
        latest_number = ""
        for char in reformatted_line:
            if char.isnumeric():
                latest_number = char
                line_result += latest_number if first_number else ""
                first_number = False
        line_result += latest_number
        #print(line_result)
        result += int(line_result)
    return result

def reformat(line):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    line = stabilize(line)
    for i, num in enumerate(numbers):
        line = line.replace(num, str(i+1))
    return line

def stabilize(line):
    line = line.replace("oneight", "oneeight")
    line = line.replace("twone", "twoone")
    line = line.replace("threeight", "threeeight")
    line = line.replace("fiveight", "fiveeight")
    line = line.replace("sevenine", "sevennine")
    line = line.replace("eightwo", "eighttwo")
    line = line.replace("eighthree", "eightthree")
    line = line.replace("nineight", "nineeight")
    return line
                
print(trabuchet("input.txt"))