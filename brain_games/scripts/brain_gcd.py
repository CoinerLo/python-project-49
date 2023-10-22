#!/usr/bin/env python3
from brain_games import cli
from random import randrange
from brain_games import utils
import prompt


def calculate_result_of_operation(number_first, number_second):
    a = number_first
    b = number_second

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


def question():
    number_first = randrange(100)
    number_two = randrange(100)
    correct_answer = calculate_result_of_operation(number_first, number_two)

    print(f'Question: {number_first} {number_two}')
    answer = prompt.string('Your answer: ')
    return (correct_answer, answer)


def main():
    name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count_answers = 0
    while count_answers < utils.number_of_rounds:
        (correct_answer, answer) = question()
        if answer == str(correct_answer):
            count_answers += 1
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return None
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
