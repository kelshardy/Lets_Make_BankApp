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

music_questions = [
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

question_prompts = [
    "How long is a quarter of an NBA game?\n(a) 20 minutes\n(b) 12 minutes\n(c) 15 minutes\n(d) 10 minutes\nAnswer: ",
    "In what sport do they play off for the Stanley Cup?\n(a) NFL\n(b) Golf\n(c) EPL\n(d) NHL\nAnswer: ",
    "Who has the most superbowl titles in NFL history?\n(a) Tom Brady\n(b) Dallas Cowboys\n(c) Pittsburgh Steelers\n(d) New England Patriots\nAnswer: ",
    "How many players are on the pitch at one time in a game of football/soccer?\n(a) 10\n(b) 11\n(c) 12\n(d) 13\nAnswer: ",
    "What is the record for the most points scored by a single player in a game of NBA?\n(a) 71\n(b) 91\n(c) 100\n(d) 81\nAnswer: ",
    "In what year did the VFL become the AFL?\n(a) 1988\n(b) 1989\n(c) 1990\n(d) 1991\nAnswer: ",
    "The first ever FIFA world cup was won by which country?\n(a) England\n(b) France\n(c) Brazil\n(d) Uruguay\nAnswer: ",
    "How old was Tiger Woods when he won The Masters for the first time?\n(a) 21\n(b) 19\n(c) 17\n(d) 23\nAnswer: ",
    "In NFL, a touchdown is worth how many points?\n(a) 5\n(b) 6\n(c) 7\n(d) 8\nAnswer: ",
    "What is Canada's national sport?\n(a) Ice Hockey\n(b) Shooting\n(c) Handball\n(d) Lacrosse\nAnswer: "
]

sport_questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "d"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "d")
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
                           {fg('dark_orange_3a')}.@@&B#@!    GGGGG#J  :JG&.                       {attr('reset')}/             Pick your Category:
                            {fg('dark_orange_3a')}G@@@@#      .~^.   ~ :.~G:                     {attr('reset')}/         Movies, TV, Music, Games or Sports
            {fg('light_pink_1')}.^:.            P!:~BY      :#~    !?#^..7J:{attr('reset')}                 <<              Win 3 Rounds for
           {fg('light_pink_1')}.Y. !~          :G  !.     .   .:7^.  ...:7:7Y    {fg('234')}.:^:.{attr('reset')}         \             a total of $500k!
           {fg('light_pink_1')}.Y  J.           ?7:7:   ^B?.    ^~..    .?. ^G {fg('234')}^GG#GBGG~{attr('reset')}        \          type Exit to Quit Game
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
            print(f"""{fg('71')}
888       888 d8b                                    888 
888   o   888 Y8P                                    888 
888  d8b  888                                        888 
{fg('2')}888 d888b 888 888 88888b.  88888b.   .d88b.  888d888 888 
888d88888b888 888 888 "88b 888 "88b d8P  Y8b 888P"   888 
88888P Y88888 888 888  888 888  888 88888888 888     Y8P 
{fg('29')}8888P   Y8888 888 888  888 888  888 Y8b.     888      "  
888P     Y888 888 888  888 888  888  "Y8888  888     888
{attr('reset')}""")
            input("You've completed 3 rounds with every answer correct!\nPress Enter:")
            print(f"""{fg('dark_orange_3a')}
                                             .~:..                              
                                              YB5JGPY.                          
                                :~J5GB###&&&&#B#B5YG&@^                         
                            .7B@@@@&BBGGB##&@@@@&##@@&:                         
                           :@@&&@@@@@@&&#&&@@@@@@@&#?                           {attr('reset')}============================================
                           {fg('dark_orange_3a')}?@@BP#&J~77?5B&&&&P^:!?PJ                         {attr('reset')}/                                                 
                           {fg('dark_orange_3a')}.@@&B#@!    GGGGG#J  :JG&.                       {attr('reset')}/          You have won the grand prize 
                            {fg('dark_orange_3a')}G@@@@#      .~^.   ~ :.~G:                     {attr('reset')}/             of an imaginary $500k! 
            {fg('light_pink_1')}.^:.            P!:~BY      :#~    !?#^..7J:{attr('reset')}                 <<          ...just let your bank know.
           {fg('light_pink_1')}.Y. !~          :G  !.     .   .:7^.  ...:7:7Y    {fg('234')}.:^:.{attr('reset')}         \        Don't spend it all at once!     
           {fg('light_pink_1')}.Y  J.           ?7:7:   ^B?.    ^~..    .?. ^G {fg('234')}^GG#GBGG~{attr('reset')}        \        Thanks for playing, {your_name}!      
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
            return

        user_decision = input(
            "What category would you like to play? Movies / TV / Music / Games / Sport: ")

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

        if (user_decision.lower() == "tv"):
            os.system('clear')
            ask_questions(tv_questions)
            Helper.congrats()
            correct_categories += 1
            continue

        if (user_decision.lower() == "music"):
            os.system('clear')
            ask_questions(music_questions)
            Helper.congrats()
            correct_categories += 1
            continue

        if (user_decision.lower() == "sport"):
            os.system('clear')
            ask_questions(sport_questions)
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
