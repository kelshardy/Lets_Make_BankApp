import random
import os

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What was the mother's name in How I Met Your Mother?\n(a) Stella\n(b) Zoe\n(c) Tracy\n(d) Robin\nAnswer: ",
    "What was Ross's surname in Friends?\n(a) Green\n(b) Geller\n(c) Bing\n(d) Buffay\nAnswer: ",
    "Who played Michael Kelso in That 70s Show?\n(a) Ashton Kutcher\n(b) Topher Grace\n(c) Eric Foreman\n(d) Wilmer Valderrama\nAnswer: ",
    "What is the name of the hospital in Scrubs\n(a) County General\n(b) Seattle Grace\n(c) San Jose St. Bonaventure\n(d) Sacred Heart\nAnswer: ",
    "What is the family's last name in Arrested Development?\n(a) Sitwell\n(b) Bluth\n(c) Michael\n(d) Bateman\nAnswer: ",
    "What was the name of Captain Holt's dog in Brooklyn Nine-Nine?\n(a) Bruce\n(b) Arlo\n(c) Terry\n(d) Cheddar\nAnswer: ",
    "In the kids tv series, Bluey, who is Bluey's father?\n(a) Bandit\n(b) Chilli\n(c) Stripe\n(d) Bingo\nAnswer: ",
    "What subject did Walter White teach in Breaking Bad?\n(a) Math\n(b) Physical Education\n(c) Chemistry\n(d) Biology\nAnswer: ",
    "What is the name of the pet dog in The Simpsons\n(a) Spike\n(b) Snowball\n(c) Odie\n(d) Santa's Little Helper\nAnswer: ",
    "What game do the boys of Stranger Things like to play?\n(a) Tag\n(b) Dungeons and Dragons\n(c) Yahtzee\n(d) Baldur's Gate\nAnswer: "
]


tv_questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "d"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "d"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "d"),
    Question(question_prompts[9], "b")
]
random.shuffle(question_prompts)
random.shuffle(tv_questions)

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
tvtime(tv_questions)


print("""
.-------------------------------------------------.
| Congratulations! You've reached the next level! |
'-------------------------------------------------'
""")
