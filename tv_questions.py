import random
import os

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "q\n(a) a\n(b) a\n(c) a\n(d) a\nAnswer: ",
    "q\n(a) a\n(b) a\n(c) a\n(d) a\nAnswer: ",
    "q\n(a) a\n(b) a\n(c) a\n(d) a\nAnswer: ",
    "q\n(a) a\n(b) a\n(c) a\n(d) a\nAnswer: ",
    "q\n(a) a\n(b) a\n(c) a\n(d) a\nAnswer: ",
    "q\n(a) a\n(b) a\n(c) a\n(d) a\nAnswer: ",
    "q\n(a) a\n(b) a\n(c) a\n(d) a\nAnswer: ",
    "q\n(a) a\n(b) a\n(c) a\n(d) a\nAnswer: ",
    "q\n(a) a\n(b) a\n(c) a\n(d) a\nAnswer: ",
    "q\n(a) a\n(b) a\n(c) a\n(d) a\nAnswer: "
]


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "a")
]
random.shuffle(question_prompts)
random.shuffle(questions)

def tvtime(questions):
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print("Correct! Next Round!")
            input()
            os.system('cls||clear')
        else:
            print("Unfortunately that is incorrect. Game Over")
            input()
            exit()
tvtime(questions[1:5])


print("""
.-------------------------------------------------.
| Congratulations! You've reached the next level! |
'-------------------------------------------------'
""")
