import os
import re
from functools import reduce


def parse_game(line):
    matches = re.match(r'^Game \d+: (.+)$', line)

    sets = []
    for set in matches[1].split(';'):
        dice = [0, 0, 0] # Default (rgb)
        for match in re.findall(r'(\d+) (red|green|blue)', set):

            for idx, color in enumerate(['red', 'green', 'blue']):
                if match[1] == color:
                    dice[idx] = int(match[0])
                    break

        sets.append(dice)

    return sets


def part_1(games):

    def valid_game(game):
        return all([
            set[0] <= 12 and set[1] <= 13 and set[2] <= 14
            for set in game
        ])

    return sum([id for id, game in enumerate(games, 1) if valid_game(game)])


def part_2(games):

    def minimum_dice(game):
        minimum_dice = [0, 0, 0] # rgb

        for set in game:
            for i in range(len(set)):
                minimum_dice[i] = max(minimum_dice[i], set[i])

        return minimum_dice

    return sum([
        reduce((lambda x, y: x * y), minimum_dice(game) )
        for game in games
    ])


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day_02.txt'), 'r') as f:
        games = [parse_game(line) for line in f.readlines()]

    print('Solution 1 - Answer is:', part_1(games))
    print('Solution 2 - Answer is:', part_2(games))
