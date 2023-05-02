import random
import os

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is Hermione Granger's middle name?\n(a) Jean\n(b) Luna\n(c) Emma\n(d) Rose\nAnswer: ",
    "Who is Frodo's best friend in The Lord Of the Rings Trilogy\n(a) Legolas\n(b) Bilbo Baggins\n(c) Gollum\n(d) Samwise Gamgee\nAnswer: ",
    "How many Oceans films have been released?\n(a) 3\n(b) 1\n(c) 4\n(d) 5\nAnswer: ",
    "Who does Keanu Reeves play in the Matrix series?\n(a) Morpheus\n(b) Neo\n(c) Trinity\n(d) Agent Smith\nAnswer: ",
    "What movie has the longest run-time in Hollywood?\n(a) Gone With The Wind\n(b) Cleopatra\n(c) Titanic\n(d) Avatar: The Way Of The Water\nAnswer: ",
    "What name is given to the human character in Monsters Inc.?\n(a) Sully\n(b) Celia\n(c) Boo\n(d) 23-19\nAnswer: ",
    "What is the Tin Man missing in The Wizard Of Oz\n(a) Heart\n(b) Courage\n(c) Brains\n(d) Home\nAnswer: ",
    "One what day does the first Die Hard movie take place?\n(a) Thanksgiving\n(b) Good Friday\n(c) Halloween\n(d) Christmas Eve\nAnswer: ",
    "What was the name of Marty's band in Back To The Future?\n(a) The Pinheads\n(b) The Blockheads\n(c) The Eggheads\n(d) The Coneheads\nAnswer: ",
    "Who played Cher in Clueless?\n(a) Lindsay Lohan\n(b) Alicia Silverstone\n(c) Rachel McAdams\n(d) Heather Graham\nAnswer: "
]


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "d"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b")
]
random.shuffle(question_prompts)
random.shuffle(questions)

def movietime(questions):
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
movietime(questions[1:5])


print("""
.-------------------------------------------------.
| Congratulations! You've reached the next level! |
'-------------------------------------------------'
""")
