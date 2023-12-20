import re


def main():
    with open("input.txt", "r") as read_file:
        s = read_file.read()
        replace = re.sub(r':', r"|", s)
    with open("input.txt", "w") as write_file:
        write_file.write(replace)
    with open("input.txt") as f:
        lines = f.read().splitlines()
    print(f'Part 1: {part1(lines)}, Part 2: {part2(lines)}')


def double(num, times):
    val = num
    for _ in range(times - 1):
        val *= 2
    return val


def part1(lines):
    total = 0
    lines = [line for line in [re.split(r'\|', line) for line in lines]]
    for line in lines:
        player_nums = set([int(x) for x in line[1].split()])
        winning_nums = set([int(x) for x in line[2].split()])
        matching_nums = player_nums.intersection(winning_nums)
        if matching_nums:
            total += double(1, len(matching_nums))
    return total


def part2(lines):
    # create a card mapping for each card, you will have at least 1 of each (original)
    card_map = [1 for _ in lines]
    lines = [line for line in [re.split(r'\|', line) for line in lines]]
    for idx, line in enumerate(lines):
        player_nums = set([int(x) for x in line[1].split()])
        winning_nums = set([int(x) for x in line[2].split()])
        matching_nums = player_nums.intersection(winning_nums)

        # value at the current index tells you how many of that card you have. Add current index value to the value for
        # each card won from current card, since you have to add 1 of the winning cards for each copy.
        # (ie card 2 wins cards 3 and 4, since you have two copies of card 2 you need two copies added to cards 3 and 4)
        card_multiplier = card_map[idx]

        for j in range(idx+1, idx + len(matching_nums)+1):
            card_map[j] += card_multiplier
    return sum(card_map)


if __name__ == "__main__":
    main()
