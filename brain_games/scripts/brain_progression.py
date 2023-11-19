#!/usr/bin/env python3
from brain_games import cli
from random import randrange
from brain_games import utils
import prompt


def question():
    start_progression = randrange(1, 1000)
    step_progression = randrange(2, 50)
    count_steps = 10
    hide_progressionPosition = randrange(0, count_steps)
    end_progression = (step_progression * count_steps) + start_progression
    answer_list = list(range(start_progression, end_progression, step_progression))
    correct_answer = answer_list[hide_progressionPosition]
    answer_list[hide_progressionPosition] = '..'
    answer_string = ' '.join(map(str, answer_list))

    print(f'Question: {answer_string}')
    answer = prompt.string('Your answer: ')
    return (str(correct_answer), answer)


def main():
    name = cli.welcome_user()
    print('What number is missing in the progression?')
    count_answers = 0
    while count_answers < utils.number_of_rounds:
        (correct_answer, answer) = question()
        if answer == correct_answer:
            count_answers += 1
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return None
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
