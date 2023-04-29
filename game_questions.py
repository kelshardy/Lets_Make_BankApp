import random
import os

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer



def gametime():

    question_prompts = [
    "What is the name of the player character in Uncharted?\n(a) Victor Sullivan\n(b) Nathan Drake\n(c) Max Payne\n(d) Big Boss",
    "What is Joel's surname in The Last Of Us?\n(a) Smith\n(b) Harrison\n(c) Miller\n(d) Garrett",
    "Who does Atreus turn out to be in God Of War?\n(a) Loki\n(b) Kratos\n(c) Zeus\n(d) Thor",
    "Which company created Super Mario?\n(a) Sony\n(b) Nintendo\n(c) Microsoft\n(d) Atari",
    "What colour is Luigi's hat in Super Mario?\n(a) Yellow\n(b) Red\n(c) Blue\n(d) Green",
    "What is the alias of the main antogonist in Bioshock?\n(a) Andrew Ryan\n(b) ADAM\n(c) Atlas\n(d) Frank Fontaine",
    "What is the name of the jungle that naked snake is dropped into at the beginning on of Metal Gear Solid 3: Snake Eater\n(a) Semipalatinsk\n(b) Stalingrad\n(c) Ural Mountains\n(d) Tselinoyarsk",
    "Which character doesn't swear in The Last Of Us Part 1?\n(a) Tommy\n(b) Ellie\n(c) Joel\n(d) David",
    "According to Metacritic, what is the highest rated game of all-time?\n(a) Tony Hawk Pro Skater 2\n(b) Grand Theft Auto V\n(c) The Legend Of Zelda: Ocarina Of Time\n(d) Elden Ring",
    "The Umbrella Corporation is a fictitious pharmaceutical company in what game?\n(a) Resident Evil\n(b) Dino Crisis\n(c) Clock Tower\n(d) Project Zero"
]


    questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "d"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "d"),
    Question(question_prompts[7], "d"),
    Question(question_prompts[8], "c"),
    Question(question_prompts[9], "a")
]
    random.shuffle(question_prompts)
    random.shuffle(questions)

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
gametime()


print("""
.-------------------------------------------------.
| Congratulations! You've reached the next level! |
'-------------------------------------------------'
""")

