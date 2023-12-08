import random

def story_generate (char1, char2, v1, v2):
    story1 = f""" 
    Once upon a time, there was a person whose name is {char1.capitalize()}. {char1.capitalize()} loves {v1.lower()}ing so 
    much.This human has an other friend which name is {char2.capitalize()}. 
    """
    story2 = f""" 
    This story is happening on Venus. 
    Once upon a time, there was a person whose name is {char1.capitalize()}. {char1.capitalize()} hates {v1.lower()}ing so 
    much.This alien has an other friend which name is {char2.capitalize()}. 
    """

    storylist = [story1, story2]
    told_story= random.choice(storylist)

    return told_story

