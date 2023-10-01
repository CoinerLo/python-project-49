#!/usr/bin/env python3
from brain_games import cli
from random import randrange, randint
from brain_games import utils
import prompt


def alculate_result_of_operation(number_first, number_second):
    operations = ['+', '-', '*']
    operation_index = randint(0, len(operations) - 1)
    if operation_index == 0:
        return (number_first + number_second, operations[operation_index])
    if operation_index == 1:
        return (number_first - number_second, operations[operation_index])
    if operation_index == 2:
        return (number_first * number_second, operations[operation_index])


def qyestion():
    number_first = randrange(1000)
    number_two = randrange(1000)
    (correct_answer, operator) = alculate_result_of_operation(number_first, number_two)

    print(f'Question: {number_first} {operator} {number_two}')
    answer = prompt.string('Your answer: ')
    return (correct_answer, answer)


def main():
    name = cli.welcome_user()
    print('What is the result of the expression?')
    count_answers = 0
    while count_answers < utils.number_of_rounds:
        (correct_answer, answer) = qyestion()
        if answer.lower() == correct_answer:
            count_answers += 1
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return None
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
