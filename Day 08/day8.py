def get_data(file):
    lines = open(file).read().splitlines()
    instructions = lines[0]
    nodes = dict()
    for line in lines[2:]:
        node_source, node_target = line.split(' = ')
        node_target = node_target.split(', ')
        node_target[0] = node_target[0][1:]
        node_target[1] = node_target[1][:-1]
        nodes[node_source] = tuple(node_target)
    return instructions, nodes

def count_steps(instructions, nodes, start, end):
    current_node = start
    step = 0
    while current_node != end:
        instruction = instructions[step % len(instructions)]
        current_node = nodes[current_node][0 if instruction == 'L' else 1]
        step += 1
    return step

def count_steps_ghosts(instructions, nodes, start_char, end_char):
    from math import lcm
    start_nodes = [node for node in nodes.keys() if node[2] == start_char]
    steps = list()
    for node in start_nodes:
        step = 0
        current_node = node
        while current_node[2] != end_char:
            instruction = instructions[step % len(instructions)]
            current_node = nodes[current_node][0 if instruction == 'L' else 1]
            step += 1
        steps.append(step)
    return lcm(*steps)

print(count_steps(*get_data("input.txt"), 'AAA', 'ZZZ'))
print(count_steps_ghosts(*get_data("input.txt"), 'A', 'Z'))