import re
import math


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    print(f'Part 1: {part1(lines)}, Part 2: {part2(lines)}')


def part1(lines):
    total = 0
    lines = ['.' * 10] + ['.' + line + '.' for line in lines] + ['.' * 10]

    for idx, line in enumerate(lines):
        for num in re.finditer(r'\d+', line):
            left = num.start() - 1
            right = num.end()
            adjacency = set(
                lines[idx-1][left:right+1] + lines[idx+1][left:right+1] + lines[idx][left] + lines[idx][right]
            ).difference({'1','2','3','4','5','6','7','8','9'})
            if adjacency != {'.'}:
                total += int(num.group())
    return total


def part2(lines):
    part_coords = {}
    gear_ratios = []
    lines = ['.' * 10] + ['.' + line + '.' for line in lines] + ['.' * 10]

    for idx, line in enumerate(lines):
        for num in re.finditer(r'\d+', line):
            left = num.start() - 1
            right = num.end()
            adjacency = set(
                lines[idx - 1][left:right + 1] + lines[idx + 1][left:right + 1] + lines[idx][left] + lines[idx][right]
            ).difference({'1', '2', '3', '4', '5', '6', '7', '8', '9'})
            if adjacency != {'.'}:
                part_number = int(num.group())
                for y in range(num.start(), num.end()):
                    part_coords[(idx, y)] = part_number

    for idx, line in enumerate(lines):
        for gear in re.finditer('\*', line):
            gear_y = gear.start()
            adjacent_coordinates = [(x, y) for x in range(idx - 1, idx + 2) for y in range(gear_y - 1, gear_y + 2)]
            adjacent_parts = set([part_coords[x_y]
                                  for x_y in adjacent_coordinates if x_y in part_coords])
            if len(adjacent_parts) == 2:
                gear_ratios.append(math.prod(adjacent_parts))
    return sum(gear_ratios)


if __name__ == '__main__':
    main()

