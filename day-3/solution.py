import re
import itertools
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
            adjacent_coordinates = [(x, y) for x in range(idx - 1, idx + 2) for y in range(gear_y - 1, gear_y + 2)
                                    if (x, y) != (idx, gear_y)
                                    and 0 <= x < len(lines)
                                    and 0 <= y < len(line)]
            adjacent_parts = set([part_coords[x_y]
                                  for x_y in adjacent_coordinates if x_y in part_coords])

            if len(adjacent_parts) == 2:
                gear_ratios.append(math.prod(adjacent_parts))
    return sum(gear_ratios)


    # TODO:
    #  1. Iterate through once to get each part number and put into a set
    #  2. Go through again and match on '*' character
    #  3. Check adjacency to see if any numbers border it
    #  4. check 3 places to right and to left from index of '*' character at idx -1, idx, and idx-1 since numbers are
    #  at max 3 characters. do a regex match to see if this new adjacency matrix contains part nums and store them
    #  5. check if part nums length in store is == 2, if it is calculate gear ratio else continue


if __name__ == '__main__':
    main()

