import random
import os




random.shuffle(m_question_prompts)
random.shuffle(movie_questions)

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
movietime(movie_questions)


print("""
.-------------------------------------------------.
| Congratulations! You've reached the next level! |
'-------------------------------------------------'
""")
