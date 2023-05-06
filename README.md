# Let's Make Bank 

## Referenced Material
___
As a reference for this terminal application, *Who Wants to Be a Millionaire?* is the basis for this concept.
There are a few rounds of trivia questions where the ultimate end game is to win a lot of money.
With each question asked, four possible answers are generated and the user picks their answer. As the user progresses, they are required to play more rounds. If the player answers incorrectly, the game is over.

## Link to Source Control Repo
___
Here is the [GitHub Link](https://github.com/kelshardy/Terminal_Application) to Let's Make Bank.

## Code Styling / Styling Conventions
___
The Google Python Style Guide has been the implemented styling convention.
It focuses on spacing out the code, running a linter to identify style issues and simplicity in coding.
It also specifies indentations, the use of lists over some loop functions and the use of imports for functions.
I have tried to follow this guide line with this terminal application to keep it clean and easy to read.

## Features
___
 
- The terminal application will include a name input from the user. This will be a featured variable that personalizes the experience for the user.
- It will feature a menu function. This will require user input to choose a category listed within the game to drive the range of trivia question. After the successful completion of answered questions in the category, the function will then loop to choose the next category.
- The menu function will also contain a variable to keep track of the user's progress, once the user has achieved 3 successful category completions, they will win the game.
- Another loop will be utilised in the questions function to play through a series of 5 questions in each of the categories. This will play through each question after a correct input is entered for each and close off after answering all 5 correctly.
- The trivia questions (which there are 10 of for each category in the code) will play 5 questions at random to keep the content different for each playthrough.
- If the user enters an incorrect response, the code will break to end the game with a 'Thanks for playing' ending. With user response, if an invalid input is made (for instance, the user inputs 'x' to an a, b, c or d only answer), the app will explain the error and request a new input.

## Implentation Plan
___
### How each feature will be implemented. Provide a time indicator and checklist of tasks for each feature - 

* Menu Function: This will drive the category selection and restart loop for next option. This will be introduced alongside the 'game host' (by 30th April)
    * Set while loop to run if statements to match user input to category
    * Create an exit option for user to voluntarily end game
    * Have if statements match question categories
    * Include .lower() for if user inputs capital lettering
    * Error handling for invalid input
* Questions Function: This will provide the trivia questions to the user for the gameplay. The questions and function will be created in conjunction with each other (by 2nd May)
    * Utilize a loop to continue through questions individually
    * Output 'correct/incorrect response' each time
    * Input to be assigned to a, b, c or d
    * Error handling for invalid input
    * Limit question playthrough to 5 question each time (use index)
* User progression will be implemented to control the amount of categories, so the code doesn't repeat itself and to avoid a potentially really long gameplay (by 4th May)
    * Create a variable to track loop turns
    * Assign += 1 code
    * Variable to be set at 0
    * Attach the code to each category for same output
    * If user progress is 3 correct categories, print win 
* Error handling will be included within the two looped functions to ensure the code doesn't break upon user playthrough (by 4th May)
    * Create for menu function
    * Create for question function
    * Print explanation
    * Repeat request for user input
    * Use else to help combat errors
* Random shuffle feature to be implemented into the questions function to avoid repeat questions asked (by 1st May)
    * Import 'random' function
    * Assign in questions function
    * Make sure there are more questions than random cap
    * Test feature to confirm it is working
* user_name feature: This will be requested at the start of the application so that it can be used throughout the game. This can be done within the first day of writing code, the initial commit (by 25th April)
    * Set Variable
    * Apply Variable to introduction
    * Include in endgame
    * Apply f in necessary strings



Here is the link to the [Trello Board](https://trello.com/b/Apz6utPT/terminal-app)
## Help Documentation
___
### *How to Install*

To install this file, access can be achieved from the green button ```<>Code``` in the top right-hand corner of the GitHub Repo, and clicking on the ```Download ZIP``` button. Alternatively click on this link [here](/Terminal_Application-main.zip).
This file can be install and executed by entering the bash script ```./run.sh``` in the terminal, which will prompt a series of commands, including installing the required packages for this application.


### *Dependencies*

As this is a Python-based terminal application, it will require the latest version of Python3 to be installed before it can run.
The following Python packages should be installed before running this code:
- art
- ascii-magic
- colorama
- colored
- iniconfig
- packaging
- Pillow
- pluggy
- pytest

### *System / Hardware Requirements*
The terminal application will run on most operating systems.
It is recommended that the terminal have 40 lines available as this will look best for the display of this app. 
This can be achieved using ```tput lines``` in the command line, which will measure out the height of the terminal.
As this Terminal Application was created with a dark theme, it would be best displayed that way.

### *How to Play*

To start 'Let's Make Bank' the player is prompted to Press Enter to begin. The application then requests the user name for a personalized experience.

The player then keys in a category to take part in a small trivia quiz based on the subject. During this, the player chooses a response to each question using either a, b, c or d. 

If the player answers incorrectly, the terminal application thanks the user for playing and closes.
If the player answers the five questions in the category correctly, they are prompted to choose another category and answer the next series of questions.
The player must correctly answer 3 categories to win the game.





