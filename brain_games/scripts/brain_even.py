#!/usr/bin/env python3
from brain_games import cli
from random import randrange
import prompt

number_of_rounds = 3


def qyestion():
    number = randrange(1000001)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    return (correct_answer, answer)


def main():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_answers = 0
    while count_answers < number_of_rounds:
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
