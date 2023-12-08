from storygenerator import story_generate

def main():
    noun_1 = get_word('character\'s 1 name')
    noun_2 = get_word('character\'s 2 name')
    verb_1 = get_word('a verb in the present tense')
    verb_2 = get_word('another verb in the present tense')
    story= story_generate(noun_1,noun_2,verb_1,verb_2)
    print('###################### Here is your story ####################################')
    print(story)

def get_word(wordtype:str):
    word= input(f'enter {wordtype}: ')
    return word



if __name__ == '__main__':
    main()