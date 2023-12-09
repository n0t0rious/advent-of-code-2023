import math
import re


def main():
    with open('input.txt') as f:
        lines = f.readlines()
    print(f'Part 1: {part1(lines)}, Part 2: {part2(lines)}')


def part1(lines):
    invalid_games = set()
    valid_games = {idx + 1 for (idx, _) in enumerate(lines)}
    game_res = []

    for l in lines:
        game_id, games = l.strip().split(':')
        game_id = int(game_id.split(' ')[-1])
        games = games.split(';')
        for g in games:
            green_match = re.search(r'(\d+)\s+green', g)
            red_match = re.search(r'(\d+)\s+red', g)
            blue_match = re.search(r'(\d+)\s+blue', g)
            res = {'game_id': game_id, 'green': -1, 'red': -1, 'blue': -1}
            if green_match:
                res['green'] = int(green_match.group(1))
            if red_match:
                res['red'] = int(red_match.group(1))
            if blue_match:
                res['blue'] = int(blue_match.group(1))
            game_res.append(res)

    for game in game_res:
        if game['green'] > 13 or game['red'] > 12 or game['blue'] > 14:
            invalid_games.add(int(game['game_id']))
    valid_games = valid_games.difference(invalid_games)
    return sum(valid_games)


def part2(lines):
    game_res = []
    all_games = {idx +1: [1,1,1] for (idx,_) in enumerate(lines)}

    for l in lines:
        game_id, games = l.strip().split(':')
        game_id = int(game_id.split(' ')[-1])
        games = games.split(';')
        for g in games:
            green_match = re.search(r'(\d+)\s+green', g)
            red_match = re.search(r'(\d+)\s+red', g)
            blue_match = re.search(r'(\d+)\s+blue', g)
            res = {'game_id': game_id, 'green': -1, 'red': -1, 'blue': -1}
            if green_match:
                res['green'] = int(green_match.group(1))
            if red_match:
                res['red'] = int(red_match.group(1))
            if blue_match:
                res['blue'] = int(blue_match.group(1))
            game_res.append(res)

    for game in game_res:
        if game['green'] > all_games[game['game_id']][0]:
            all_games[game['game_id']][0] = game['green']
        if game['red'] > all_games[game['game_id']][1]:
            all_games[game['game_id']][1] = game['red']
        if game['blue'] > all_games[game['game_id']][2]:
            all_games[game['game_id']][2] = game['blue']
    res = [math.prod(values) for id_, values in all_games.items()]
    return sum(res)


if __name__ == '__main__':
    main()
