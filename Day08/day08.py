import re
from math import lcm

def part1(start_node, instructions, nodes):
    actual_node = start_node
    step = 0
    while actual_node[0] != 'ZZZ':
        for instruction in instructions:
            step += 1
            if instruction == 'L':
                actual_node = next(x for x in nodes if actual_node[1] == x[0])
            if instruction == 'R':
                actual_node = next(x for x in nodes if actual_node[2] == x[0])

    return step


def part2(start_node, instructions, nodes):
    steps = []
    for current in start_node:
        step = 0
        while not current[0].endswith('Z'):
            instruction = instructions[step % len(instructions)]
            step += 1
            if instruction == 'L':
                current = next(x for x in nodes if x[0] == current[1])
            else:
                current = next(x for x in nodes if x[0] == current[2])
        steps.append(step)

    return steps


if __name__ == "__main__":
    with open("test.txt", "r", encoding="utf-8") as f:
        fileInput = f.read()
        lines = fileInput.split('\n')
        instructions = lines[0]
        network = lines[2:]

        PATTERN = r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)'

        nodes = []
        for i in network:
            match = re.match(PATTERN, i)
            if match:
                nodes.append(
                    [match.group(1), match.group(2), match.group(3)])

        start_node1 = next(x for x in nodes if x[0] == 'AAA')

        start_node2 = [x for x in nodes if x[0][2] == 'A']

        print(f'Part 1: {part1(start_node1, instructions, nodes)}')
        print(f'Part 2: {lcm(*part2(start_node2, instructions, nodes))}')

