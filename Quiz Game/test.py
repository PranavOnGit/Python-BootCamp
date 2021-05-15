
from Quiz import Quiz

prompt = [
    'Which Alphabate comes befor X?\n(a) M\n(b) Y\n(c) W\n\n',
    'Which Alphabate comes after M?\n(a) P\n(b) L\n(c) N\n\n',
    'Which second last Alphabate?\n(a) Y\n(b) B\n(c) X\n\n'
]

quiz = [
    Quiz(prompt[0], "b"),
    Quiz(prompt[1], "c"),
    Quiz(prompt[2], "a")
]

def run_test(quiz):
    score  = 0
    for quiz in quiz:
        answer = input(quiz.prompt)
        if answer == quiz.answer:
            score +=1

    print('You got '+ str(score)+' / '+str(len(prompt))+' correct')


run_test(quiz)