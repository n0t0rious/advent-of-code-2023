import math


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    print(f'Part 1: {part1(lines)}, Part 2: {part2(lines)}')


def part1(lines):
    time = [int(x) for x in lines[0].split(':')[1].strip().split()]
    distance = [int(x) for x in lines[1].split(':')[1].strip().split()]
    combs = []
    for t, d in zip(time, distance):
        t_remaining = [x for x in range(0, t+1)][::-1]
        t_button = [x for x in range(0, t+1)]
        combs.append(len((distances := [x * y for x, y in zip(t_remaining, t_button) if x * y > d])))
    return math.prod(combs)


def part2(lines):
    time = int(lines[0].split(':')[1].strip().replace(' ', ''))
    distance = int(lines[1].split(':')[1].strip().replace(' ', ''))
    curr_dist = 0
    l = 0
    r = time
    while curr_dist < distance:
        l += 1
        r -= 1
        curr_dist = l * r
    return r - l + 1


if __name__ == "__main__":
    main()
