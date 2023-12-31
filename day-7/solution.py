from collections import Counter


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    print(f'Part 1: {part1(lines)}, Part 2: {part2(lines)}')


def part1(lines):
    char_map = {'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'}

    def score_hand(hand):
        count = [card for card in sorted(Counter(hand).values())]
        match count:
            case [1, 1, 1, 1, 1]:
                return 0
            case [1, 1, 1, 2]:
                return 1
            case [1, 2, 2]:
                return 2
            case [1, 1, 3]:
                return 3
            case [2, 3]:
                return 4
            case [1, 4]:
                return 5
            case _:
                return 6

    def strength(hand):
        return score_hand(hand), [char_map.get(card, card) for card in hand]

    games = []

    for line in lines:
        hand, bid = line.split()
        games.append((hand, int(bid)))
    games.sort(key=lambda game: strength(game[0]))

    winnings = 0

    for rank, (hand, bid) in enumerate(games, 1):
        winnings += rank * bid

    return winnings


def part2(lines):
    char_map = {'T': 'A', 'J': ',', 'Q': 'C', 'K': 'D', 'A': 'E'}

    def score_hand(hand):
        count = [card for card in sorted(Counter(hand).values())]
        match count:
            case [1, 1, 1, 1, 1]:
                return 0
            case [1, 1, 1, 2]:
                return 1
            case [1, 2, 2]:
                return 2
            case [1, 1, 3]:
                return 3
            case [2, 3]:
                return 4
            case [1, 4]:
                return 5
            case _:
                return 6

    def replacements(hand):
        if hand == "":
            return [""]

        return [
            x + y
            for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
            for y in replacements(hand[1:])
        ]

    def classify_hand(hand):
        return max(map(score_hand, replacements(hand)))

    def strength(hand):
        return classify_hand(hand), [char_map.get(card, card) for card in hand]

    games = []

    for line in lines:
        hand, bid = line.split()
        games.append((hand, int(bid)))
    games.sort(key=lambda game: strength(game[0]))

    winnings = 0

    for rank, (hand, bid) in enumerate(games, 1):
        winnings += rank * bid

    return winnings


if __name__ == "__main__":
    main()
