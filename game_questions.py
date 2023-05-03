import random
import os

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is the name of the player character in Uncharted?\n(a) Victor Sullivan\n(b) Nathan Drake\n(c) Max Payne\n(d) Big Boss\nAnswer: ",
    "What is Joel's surname in The Last Of Us?\n(a) Smith\n(b) Harrison\n(c) Miller\n(d) Garrett\nAnswer: ",
    "Who does Atreus turn out to be in God Of War?\n(a) Loki\n(b) Kratos\n(c) Zeus\n(d) Thor\nAnswer: ",
    "Which company created Super Mario?\n(a) Sony\n(b) Nintendo\n(c) Microsoft\n(d) Atari\nAnswer: ",
    "What colour is Luigi's hat in Super Mario?\n(a) Yellow\n(b) Red\n(c) Blue\n(d) Green\nAnswer: ",
    "What is the alias of the main antogonist in Bioshock?\n(a) Andrew Ryan\n(b) ADAM\n(c) Atlas\n(d) Frank Fontaine\nAnswer: ",
    "What is the name of the jungle that naked snake is dropped into at the beginning on of Metal Gear Solid 3: Snake Eater\n(a) Semipalatinsk\n(b) Stalingrad\n(c) Ural Mountains\n(d) Tselinoyarsk\nAnswer: ",
    "Which character doesn't swear in The Last Of Us Part 1?\n(a) Tommy\n(b) Ellie\n(c) Joel\n(d) David\nAnswer: ",
    "According to Metacritic, what is the highest rated game of all-time?\n(a) Tony Hawk Pro Skater 2\n(b) Grand Theft Auto V\n(c) The Legend Of Zelda: Ocarina Of Time\n(d) Elden Ring\nAnswer: ",
    "The Umbrella Corporation is a fictitious pharmaceutical company in what game?\n(a) Resident Evil\n(b) Dino Crisis\n(c) Clock Tower\n(d) Project Zero\nAnswer: "
]

game_questions = [
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
random.shuffle(game_questions)

def gametime(questions):
 for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print("Correct! Next Question")
            input()
            os.system('clear')
        else:
            print("Unfortunately that is incorrect. Game Over")
            input()
            exit()
gametime(game_questions[0:5])


print("""
.-------------------------------------------------.
| Congratulations! You've reached the next level! |
'-------------------------------------------------'
""")

