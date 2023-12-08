# Random-Story-Teller


![image](https://github.com/Aladin-bit01/Random-Story-Teller/assets/144846441/dea11b73-fa8f-438c-a3c2-7d18128cda38)


Hey you !! Do you have little kids in your family ? Are they between 5 and 9 years old ? Do they have the before sleep story ritual ? Are you having hard time satisfying their curiosity and coming up with new fun and creative story ?
Don't search no more. You have the solution here. 


When you run our code , you will be asked to enter several words: including names of characters, adjectives and some verbs and boom , you get out a story. Yes, it's that simple.


Enjoy your trip in our world of creativity, adventures and fun !! 🎢🎭

 
## Part 1 ( Storygenerator.py)

The function `story_generate` takes 4 parameters (char1, char2, v1, v2). Those strings will be inserted in the four stories we created using `f_strings`. 
A `storylist` is created then with those four stories. 

The function will call the `random.choice(storylist)` which will choose randomly one of the stories to return.


## Part 2 (main.py)

`get_word` fucntion will ask the user for a specific input

The `main()` function will then call the `get_word` function four times to get the 4 different variables, which will be handed to the `story_generate` module. Finally, the return value of `story_generate` will be printed in the console. 


