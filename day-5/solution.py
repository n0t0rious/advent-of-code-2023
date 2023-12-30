import re
from itertools import batched


def main():
    with open("test_input.txt") as f:
        lines = f.read()
    print(f'Part 1: {part1(lines)}, Part 2: {part2(lines)}')


def part1(lines):
    min_loc = float('inf')
    seeds = [int(seed) for seed in re.match(r'seeds:\s+([0-9]+( [0-9]+)+)', lines).group().split(':')[1].split()]
    mappings = [list(batched(number.split(), 3)) for number in
                [line.group().replace('\n', ' ').split(':')[1] for line in re.finditer(r'([A-Za-z]+(-['r'A-Za-z]+)+) '
                                                                                       r'['r'A-Za-z]+:'
                                                                                       r'('r'\s(['r'0-9]+\s)+)'
                                                                                       r'\d+', lines)]]
    for seed in seeds:
        curr_seed = seed
        for _map in mappings:
            for m in _map:
                diff = int(m[1]) - int(m[0])
                if curr_seed in range(int(m[1]), int(m[1]) + int(m[2])):
                    curr_seed = curr_seed - diff
                    break
        min_loc = min(curr_seed, min_loc)
    return min_loc


def part2(lines):
    mappings = [list(batched(number.split(), 3)) for number in
                [line.group().replace('\n', ' ').split(':')[1] for line in re.finditer(r'([A-Za-z]+(-['r'A-Za-z]+)+) '
                                                                                       r'['r'A-Za-z]+:'
                                                                                       r'('r'\s(['r'0-9]+\s)+)'
                                                                                       r'\d+', lines)]]
    raw_seeds = list(
        batched([int(seed) for seed in re.match(r'seeds:\s+([0-9]+( [0-9]+)+)', lines).group().split(':')[1].split()],
                2))
    seeds = [(start, start + end) for start, end in raw_seeds]
    for _map in mappings:
        ranges = []
        for m in _map:
            ranges.append(tuple(map(int,m)))
        locs = []
        while seeds:
            start, end = seeds.pop()
            for dest, source, length in ranges:
                i_s = max(start, source)
                i_e = min(end, source + length)
                if i_s < i_e:
                    locs.append((i_s - source + dest,i_e - source + dest))
                    if i_s > start:
                        seeds.append((start,i_s))
                    if end > i_e:
                        seeds.append((i_e,end))
                    break
            else:
                locs.append((start,end))
        seeds = locs
    return min(seeds)[0]


if __name__ == "__main__":
    main()
