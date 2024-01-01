import itertools
import math
import sys

sys.setrecursionlimit(25000)


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    print(f'Part 1: {part1(lines)}, Part 2: {part2(lines)}')


def part1(lines):
    mapping = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2::]}
    instructions = itertools.cycle(lines[0])
    dir_map = {'R': 1, 'L': 0}

    def traverse(lookup, instruction, c):
        if mapping[lookup][dir_map[instruction[0]]] == 'ZZZ':
            return c
        else:
            return traverse(mapping[lookup][dir_map[instruction[0]]], next(instructions), c+1)

    return traverse('AAA', next(instructions), 1)


def part2(lines):
    mapping = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2::]}
    instructions = itertools.cycle(lines[0])
    dir_map = {'R': 1, 'L': 0}
    starts = [node for node in mapping if node.endswith('A')]

    def traverse(lookup, instruction, c):
        if not mapping[lookup][dir_map[instruction[0]]].endswith('Z'):
            return traverse(mapping[lookup][dir_map[instruction[0]]], next(direction),  c+1)
        else:
            return c

    cycles = []

    for node in starts:
        direction = instructions
        cycles.append(traverse(node, next(direction), 1))

    return math.lcm(*cycles)


if __name__ == "__main__":
    main()
