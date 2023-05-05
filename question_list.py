import os
import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def ask_questions(questions):
    random.shuffle(questions)
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print("Correct! Next Round!")
            input()
            os.system('cls||clear')
        else:
            print("Unfortunately that is incorrect.")
            input()
            exit()

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

movie_questions = [
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

question_prompts = [
    "Which classical composer was deaf?\n(a) Chopin\n(b) Brahms\n(c) Beethoven\n(d) Tchaikovsky\nAnswer: ",
    "What band features frontman, Jared Leto?\n(a) 30 Seconds to Mars\n(b) Three Days Grace\n(c) Fall Out Boy\n(d) Weezer\nAnswer: ",
    "Some fans believed that this particular Beatle had actually died and been replaced by a double:\n(a) Ringo\n(b) John\n(c) George\n(d) Paul\nAnswer: ",
    "Which cover did Andy Warhol design for The Rolling Stones?\n(a) Exile on Main St.\n(b) Let It Bleed\n(c) Sticky Fingers\n(d) Goats Head Soup\nAnswer: ",
    "What was the name of Elvis Presley's daughter?\n(a) Gladys\n(b) Lisa-Marie\n(c) Priscilla\n(d) Dottie\nAnswer: ",
    "Justin Timberlake was part of which boy band originally?\n(a) Backstreet Boys\n(b) NSYNC\n(c) Westlife\n(d) Five\nAnswer: ",
    "Which actor used to be known by his stage name, Marky Mark?\n(a) Mark Ruffalo\n(b) Mark Hamill\n(c) Mark Strong\n(d) Mark Wahlberg\nAnswer: ",
    "Beyonce was originally part of which girl group?\n(a) Destiny's Child\n(b) TLC\n(c) Spice Girls\n(d) Pussycat Dolls\nAnswer: ",
    "Who sung the one hit wonder, 'Breakfast At Tiffany's'?\n(a) Semisonic\n(b) Fountains of Wayne\n(c) Deep Blue Something\n(d) Wheatus\nAnswer: ",
    "Who sings the rock song, 'You Shook Me All Night Long'?\n(a) AC/DC\n(b) Kiss\n(c) Aerosmith\n(d) Guns N' Roses\nAnswer: "
]

game_questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "d"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "c"),
    Question(question_prompts[9], "a")
]