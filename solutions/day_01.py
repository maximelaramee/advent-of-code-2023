import os
import re


text_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def convert_digit(digit: str) -> str:
    return text_digits[digit] if digit in text_digits.keys() else digit


def part_1(lines) -> int:
    pattern = r'\d'

    return sum([
        int(convert_digit(digits[0]) + convert_digit(digits[-1]))
        for digits in [re.findall(pattern, line) for line in lines]
    ])


def part_2(lines) -> int:
    pattern = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'

    return sum([
        int(convert_digit(digits[0]) + convert_digit(digits[-1]))
        for digits in [re.findall(pattern, line) for line in lines]
    ])


if __name__ == '__main__':

    with open(os.path.join('inputs', 'day_01.txt'), 'r') as f:
        puzzle_input = f.readlines()

    print('Solution 1 - Answer is:', part_1(puzzle_input))
    print('Solution 2 - Answer is:', part_2(puzzle_input))
