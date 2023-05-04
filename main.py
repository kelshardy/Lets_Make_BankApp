import os
import random
import sys
import time
from colored import fg, bg, attr


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


def ask_questions(questions):
    random.shuffle(questions)
    for question in questions[0:5]:

        answer = ""
        while answer.lower() not in ["a", "b", "c", "d"]:
            answer = input(question.prompt)
            if answer == question.answer:
                print(f"{fg('green')}Correct! Next Question{attr('reset')}")
                input()
                os.system('clear')
            elif answer != question.answer and answer.lower() not in ["a", "b", "c", "d"]:
                os.system('clear')
                print(
                    f"{fg('214')}Oi mate, that's not a real answer!{attr('reset')}")
            else:
                print_slow(
                    f"{fg('red')}Unfortunately that is incorrect.\nYou will be making no bank today...{attr('reset')}")
                input()
                exit(f"Thanks for playing, {your_name}!")


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


class Helper:
    def congrats():
        print(f"""{fg('yellow')}
.-------------------------------------------------.
| {bg('91')}Congratulations! You've reached the next level!{attr('reset')}{fg('yellow')} |
'-------------------------------------------------'
{attr('reset')}""")


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.08)


def press_start():
    print(f"""{fg('gold_3b')}
  888              888    d8b              888b     d888          888                    888888b.                     888      
  888              888    88P              8888b   d8888          888                    888  "88b                    888      
  888              888    8P               88888b.d88888          888                    888  .88P                    888      
  {fg('gold_1')}888      .d88b.  888888 "  .d8888b       888Y88888P888  8888b.  888  888  .d88b.       8888888K.   8888b.  88888b.  888  888 
  888     d8P  Y8b 888       88K           888 Y888P 888     "88b 888 .88P d8P  Y8b      888  "Y88b     "88b 888 "88b 888 .88P 
  888     88888888 888       "Y8888b.      888  Y8P  888 .d888888 888888K  88888888      888    888 .d888888 888  888 888888K  
  {fg('yellow')}888     Y8b.     Y88b.          X88      888   "   888 888  888 888 "88b Y8b.          888   d88P 888  888 888  888 888 "88b 
  88888888 "Y8888   "Y888     88888P'      888       888 "Y888888 888  888  "Y8888       8888888P"  "Y888888 888  888 888  888 
                                                                                                                              
                                                                                                                              
                                                                                                                              
  {attr('reset')}""")
    print_slow("Press Enter to Start...")
    input()

press_start()

os.system('clear')

print(f"""{fg('dark_orange_3a')}
                                             .~:..                              
                                              YB5JGPY.                          
                                :~J5GB###&&&&#B#B5YG&@^                         
                            .7B@@@@&BBGGB##&@@@@&##@@&:                         
                           :@@&&@@@@@@&&#&&@@@@@@@&#?                           {attr('reset')}============================================
                           {fg('dark_orange_3a')}?@@BP#&J~77?5B&&&&P^:!?PJ                         {attr('reset')}/                                                 
                           {fg('dark_orange_3a')}.@@&B#@!    GGGGG#J  :JG&.                       {attr('reset')}/       Hello! Welcome to Let's Make Bank! 
                            {fg('dark_orange_3a')}G@@@@#      .~^.   ~ :.~G:                     {attr('reset')}/                                                        
            {fg('light_pink_1')}.^:.            P!:~BY      :#~    !?#^..7J:{attr('reset')}                 <<     The aim of the game is to answer questions          
           {fg('light_pink_1')}.Y. !~          :G  !.     .   .:7^.  ...:7:7Y    {fg('234')}.:^:.{attr('reset')}         \    correctly for the chance to win a lot of money! 
           {fg('light_pink_1')}.Y  J.           ?7:7:   ^B?.    ^~..    .?. ^G {fg('234')}^GG#GBGG~{attr('reset')}        \       I'm you're host, Frank, and you are? 
         {fg('light_pink_1')}..?!  !^            :@B.   .5:::::. .:^~^~^:    &{fg('234')}^&BGG5G5GB~{attr('reset')}        \\
     {fg('light_pink_1')}:~^!:^P    :J            #B     7&P7^:......:7     ^G{fg('234')}^&BBG5BPBB7{attr('reset')}           =============================================
  {fg('light_pink_1')}.Y7~:!: .?~.  {fg('23')}.&J           {fg('light_pink_1')}~B      J@&&&#B??Y^:.     G~ {fg('234')}?#&G#&#G#5{fg('light_pink_1')}!!?.{attr('reset')}       
  {fg('light_pink_1')}G~.:.~ ..     {fg('23')}P5G7           {fg('light_pink_1')}P.      ^GPYYPJ757. :   75    {fg('234')}:?#?!Y5.{fg('light_pink_1')}^7?7!{attr('reset')}      
  {fg('light_pink_1')}Y5:::::^{fg('23')}:JB&~?J!!#^         {fg('light_pink_1')}.Y#        .^~~~~^: .5  !5      {fg('234')}!~ .  P7 {fg('light_pink_1')}.~GJ{attr('reset')}    
   {fg('light_pink_1')}.:...  {fg('23')}^#B#57!7!?#.     .7PGJP#:               {fg('light_pink_1')}^J 7J        {fg('234')}Y^.~~G5J?. {fg('light_pink_1')}^5{attr('reset')}   
           {fg('23')}?G7!!777!JB::!YGGY7!!!GG7^            :!^BB         G&?  {fg('234')}.Y&?:?PB{attr('reset')}    
            {fg('23')}^BY!!!!!!?BGYJ7!!!!!!!G5?J?7!!~:  ..??!BB5P.      PP75:.YJ{fg('234')}?##Y75G~{attr('reset')}  
              {fg('23')}5G7!!77!!7!!7!!!77!!?G5GPG^::~P5~JP^.~G~?G!    P5!!7JP@B? {fg('234')}.5BP#Y{attr('reset')}  
               {fg('23')}^G57!!!!!!!!7JGB?7YJJ5JJB~:~7P&?PP!^?P?!!YP!!GY!!!!!7JGP   {fg('234')}.^.{attr('reset')}   
                 {fg('23')}~5PYJJJYY5J^PB!PB5BBP7?55BBBP!GGG55?B!7!7PP7!777!!YP~          
                   .:~!!~:   5P!7?JY5PP7!77!?YB&J77!PP!7!!!!!7!!75G7            
                             GY!!!!!!!!77!!7!!?GY!!!#P?!!!!!!!?PG?              
                             GJ!777777777777!GBGJ~~?P:J5YJJY5PY~                
                             B7!777777777777!JY#7!~#^   .^^:.                   
                            .&7!777777777777PGYG!!JB                            
                            .&?7!!!!!77777!7GPB?!!#~                            
                             :!YG5J?7!!!!!!!!JP775B                             
                                #5PGGGPPPPPPP##Y?!.                             
                                B7!!77?YJ?JJ?G5                                 
                                B7!!!7#&J!!!JG                                  
                                B7!!!7&#7!!?B.                                  
                                B7!!!Y#G!!!B^                                   
                               .#J?77GGP!7GJ                                    
                            {fg('232')}:JB@@@@@@BB@@@@@BJ^                                 
                         :G&@@@&#B&#G:~G##B&@@@@B7                              
{attr('reset')}""")

print_slow("Enter name: ")
your_name = input("")

os.system('clear')
print(f"""{fg('dark_orange_3a')}
                                             .~:..                              
                                              YB5JGPY.                          
                                :~J5GB###&&&&#B#B5YG&@^                         
                            .7B@@@@&BBGGB##&@@@@&##@@&:                         
                           :@@&&@@@@@@&&#&&@@@@@@@&#?                           {attr('reset')}============================================
                           {fg('dark_orange_3a')}?@@BP#&J~77?5B&&&&P^:!?PJ                         {attr('reset')}/                                                 
                           {fg('dark_orange_3a')}.@@&B#@!    GGGGG#J  :JG&.                       {attr('reset')}/              G-Day, {your_name}! 
                            {fg('dark_orange_3a')}G@@@@#      .~^.   ~ :.~G:                     {attr('reset')}/      For each round, we'll pick a different
            {fg('light_pink_1')}.^:.            P!:~BY      :#~    !?#^..7J:{attr('reset')}                 <<     category. Answer correctly and you're still         
           {fg('light_pink_1')}.Y. !~          :G  !.     .   .:7^.  ...:7:7Y    {fg('234')}.:^:.{attr('reset')}         \        in the game. If you're wrong, 
           {fg('light_pink_1')}.Y  J.           ?7:7:   ^B?.    ^~..    .?. ^G {fg('234')}^GG#GBGG~{attr('reset')}        \       it's Game Over... here we go! 
         {fg('light_pink_1')}..?!  !^            :@B.   .5:::::. .:^~^~^:    &{fg('234')}^&BGG5G5GB~{attr('reset')}        \\
     {fg('light_pink_1')}:~^!:^P    :J            #B     7&P7^:......:7     ^G{fg('234')}^&BBG5BPBB7{attr('reset')}           =============================================
  {fg('light_pink_1')}.Y7~:!: .?~.  {fg('23')}.&J           {fg('light_pink_1')}~B      J@&&&#B??Y^:.     G~ {fg('234')}?#&G#&#G#5{fg('light_pink_1')}!!?.{attr('reset')}       
  {fg('light_pink_1')}G~.:.~ ..     {fg('23')}P5G7           {fg('light_pink_1')}P.      ^GPYYPJ757. :   75    {fg('234')}:?#?!Y5.{fg('light_pink_1')}^7?7!{attr('reset')}      
  {fg('light_pink_1')}Y5:::::^{fg('23')}:JB&~?J!!#^         {fg('light_pink_1')}.Y#        .^~~~~^: .5  !5      {fg('234')}!~ .  P7 {fg('light_pink_1')}.~GJ{attr('reset')}    
   {fg('light_pink_1')}.:...  {fg('23')}^#B#57!7!?#.     .7PGJP#:               {fg('light_pink_1')}^J 7J        {fg('234')}Y^.~~G5J?. {fg('light_pink_1')}^5{attr('reset')}   
           {fg('23')}?G7!!777!JB::!YGGY7!!!GG7^            :!^BB         G&?  {fg('234')}.Y&?:?PB{attr('reset')}    
            {fg('23')}^BY!!!!!!?BGYJ7!!!!!!!G5?J?7!!~:  ..??!BB5P.      PP75:.YJ{fg('234')}?##Y75G~{attr('reset')}  
              {fg('23')}5G7!!77!!7!!7!!!77!!?G5GPG^::~P5~JP^.~G~?G!    P5!!7JP@B? {fg('234')}.5BP#Y{attr('reset')}  
               {fg('23')}^G57!!!!!!!!7JGB?7YJJ5JJB~:~7P&?PP!^?P?!!YP!!GY!!!!!7JGP   {fg('234')}.^.{attr('reset')}   
                 {fg('23')}~5PYJJJYY5J^PB!PB5BBP7?55BBBP!GGG55?B!7!7PP7!777!!YP~          
                   .:~!!~:   5P!7?JY5PP7!77!?YB&J77!PP!7!!!!!7!!75G7            
                             GY!!!!!!!!77!!7!!?GY!!!#P?!!!!!!!?PG?              
                             GJ!777777777777!GBGJ~~?P:J5YJJY5PY~                
                             B7!777777777777!JY#7!~#^   .^^:.                   
                            .&7!777777777777PGYG!!JB                            
                            .&?7!!!!!77777!7GPB?!!#~                            
                             :!YG5J?7!!!!!!!!JP775B                             
                                #5PGGGPPPPPPP##Y?!.                             
                                B7!!77?YJ?JJ?G5                                 
                                B7!!!7#&J!!!JG                                  
                                B7!!!7&#7!!?B.                                  
                                B7!!!Y#G!!!B^                                   
                               .#J?77GGP!7GJ                                    
                            {fg('232')}:JB@@@@@@BB@@@@@BJ^                                 
                         :G&@@@&#B&#G:~G##B&@@@@B7                              
{attr('reset')}""")

input("Press Enter to continue")
os.system('clear')
print(f"""{fg('dark_orange_3a')}
                                             .~:..                              
                                              YB5JGPY.                          
                                :~J5GB###&&&&#B#B5YG&@^                         
                            .7B@@@@&BBGGB##&@@@@&##@@&:                         
                           :@@&&@@@@@@&&#&&@@@@@@@&#?                           {attr('reset')}============================================
                           {fg('dark_orange_3a')}?@@BP#&J~77?5B&&&&P^:!?PJ                         {attr('reset')}/                                                 
                           {fg('dark_orange_3a')}.@@&B#@!    GGGGG#J  :JG&.                       {attr('reset')}/          Round 1: Pick your Category: 
                            {fg('dark_orange_3a')}G@@@@#      .~^.   ~ :.~G:                     {attr('reset')}/      Movies / TV / Music / Games / Sports / Books
            {fg('light_pink_1')}.^:.            P!:~BY      :#~    !?#^..7J:{attr('reset')}                 <<          Answer all correct in each category         
           {fg('light_pink_1')}.Y. !~          :G  !.     .   .:7^.  ...:7:7Y    {fg('234')}.:^:.{attr('reset')}         \             for a total of $200k! 
           {fg('light_pink_1')}.Y  J.           ?7:7:   ^B?.    ^~..    .?. ^G {fg('234')}^GG#GBGG~{attr('reset')}        \            type Exit to Quit Game 
         {fg('light_pink_1')}..?!  !^            :@B.   .5:::::. .:^~^~^:    &{fg('234')}^&BGG5G5GB~{attr('reset')}        \\
     {fg('light_pink_1')}:~^!:^P    :J            #B     7&P7^:......:7     ^G{fg('234')}^&BBG5BPBB7{attr('reset')}           =============================================
  {fg('light_pink_1')}.Y7~:!: .?~.  {fg('23')}.&J           {fg('light_pink_1')}~B      J@&&&#B??Y^:.     G~ {fg('234')}?#&G#&#G#5{fg('light_pink_1')}!!?.{attr('reset')}       
  {fg('light_pink_1')}G~.:.~ ..     {fg('23')}P5G7           {fg('light_pink_1')}P.      ^GPYYPJ757. :   75    {fg('234')}:?#?!Y5.{fg('light_pink_1')}^7?7!{attr('reset')}      
  {fg('light_pink_1')}Y5:::::^{fg('23')}:JB&~?J!!#^         {fg('light_pink_1')}.Y#        .^~~~~^: .5  !5      {fg('234')}!~ .  P7 {fg('light_pink_1')}.~GJ{attr('reset')}    
   {fg('light_pink_1')}.:...  {fg('23')}^#B#57!7!?#.     .7PGJP#:               {fg('light_pink_1')}^J 7J        {fg('234')}Y^.~~G5J?. {fg('light_pink_1')}^5{attr('reset')}   
           {fg('23')}?G7!!777!JB::!YGGY7!!!GG7^            :!^BB         G&?  {fg('234')}.Y&?:?PB{attr('reset')}    
            {fg('23')}^BY!!!!!!?BGYJ7!!!!!!!G5?J?7!!~:  ..??!BB5P.      PP75:.YJ{fg('234')}?##Y75G~{attr('reset')}  
              {fg('23')}5G7!!77!!7!!7!!!77!!?G5GPG^::~P5~JP^.~G~?G!    P5!!7JP@B? {fg('234')}.5BP#Y{attr('reset')}  
               {fg('23')}^G57!!!!!!!!7JGB?7YJJ5JJB~:~7P&?PP!^?P?!!YP!!GY!!!!!7JGP   {fg('234')}.^.{attr('reset')}   
                 {fg('23')}~5PYJJJYY5J^PB!PB5BBP7?55BBBP!GGG55?B!7!7PP7!777!!YP~          
                   .:~!!~:   5P!7?JY5PP7!77!?YB&J77!PP!7!!!!!7!!75G7            
                             GY!!!!!!!!77!!7!!?GY!!!#P?!!!!!!!?PG?              
                             GJ!777777777777!GBGJ~~?P:J5YJJY5PY~                
                             B7!777777777777!JY#7!~#^   .^^:.                   
                            .&7!777777777777PGYG!!JB                            
                            .&?7!!!!!77777!7GPB?!!#~                            
                             :!YG5J?7!!!!!!!!JP775B                             
                                #5PGGGPPPPPPP##Y?!.                             
                                B7!!77?YJ?JJ?G5                                 
                                B7!!!7#&J!!!JG                                  
                                B7!!!7&#7!!?B.                                  
                                B7!!!Y#G!!!B^                                   
                               .#J?77GGP!7GJ                                    
                            {fg('232')}:JB@@@@@@BB@@@@@BJ^                                 
                         :G&@@@&#B&#G:~G##B&@@@@B7                              
{attr('reset')}""")


def category_menu():
    correct_categories = 0

    while True:
        if correct_categories >= 3:
            print("You are the bread winner!")
            return

        user_decision = input("What category would you like to play?: ")

        if (user_decision.lower() == "games"):
            os.system('clear')
            ask_questions(game_questions)
            Helper.congrats()
            correct_categories += 1
            continue

        if (user_decision.lower() == "movies"):
            os.system('clear')
            ask_questions(movie_questions)
            Helper.congrats()
            correct_categories += 1
            continue

        if (user_decision.lower() == "exit"):
            return
        else:
            print("Error: Category doesn't exist.")
            print("Please enter a Category or type Exit")
            continue

category_menu()

print(f"Thanks for playing, {your_name}!")