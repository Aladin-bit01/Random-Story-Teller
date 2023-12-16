# My Baby Projects 


![image](https://github.com/Aladin-bit01/Random-Story-Teller/assets/144846441/a1b86a29-53eb-4b24-83c9-5ac9512ef27a)

If you are reading this now, this probably means that you are in the computer science, software, cyber, data science, etc. big family. Whether you are a friend, a a classmate, a teacher, an employer, a dummy CS student or anybody else, I would like to tell you welcome to my baby projects zone. Yes, yes, you are going to discover my first personal projects here (Date while I am writning this is *8 Dec 2023* ). These projects are so simple and so beginner friendly. They helped me consolidate simple but crucial notions in the `PYTHON` language specifically and in programming in general. 

Hope you enjoy your trip Here !


##  Random-Story-Teller
Hey you !! Do you have little kids in your family ? Are they between 5 and 9 years old ? Do they have the before sleep story ritual ? Are you having hard time satisfying their curiosity and coming up with new fun and creative story ?
Don't search no more. You have the solution here. 


When you run our code , you will be asked to enter several words: including names of characters, adjectives and some verbs and boom , you get out a story. Yes, it's that simple.


Enjoy your trip in our world of creativity, adventures and fun !! 🎢🎭
 
### Part 1 ( Storygenerator.py)

The function `story_generate` takes 4 parameters (char1, char2, v1, v2). Those strings will be inserted in the four stories we created using `f_strings`. 
A `storylist` is created then with those four stories. 

The function will call the `random.choice(storylist)` which will choose randomly one of the stories to return.


### Part 2 (main.py)

`get_word` fucntion will ask the user for a specific input

The `main()` function will then call the `get_word` function four times to get the 4 different variables, which will be handed to the `story_generate` module. Finally, the return value of `story_generate` will be printed in the console. 


## Guess the Number 

In this baby project: two functions do all the job. The first one `get_the_range` asks the user to give it two inputs (the lowest and highest number) which will be used by the other function. Errors are handled using `Try-Except`to make sure the user is giving integers as input. 

The second function `guessing_game` uses both of the user's inputs of `get_the_range` to generate a random number in between those integers (Using the `random` module). The user is asked to guess this number and has three chances to guess it. In order to tell the user if he guessed the answer right or not, an interesting ascii art nmodule is used `cowsay`. If the user guessed right the answer, a tirex will appear and tell him that he won. In the other case, a cow will announce him the news that he lost. 
