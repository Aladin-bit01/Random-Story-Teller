import random

def story_generate (char1, char2, v1, v2):

    story1 = f""" 
        Once upon a time, in the enchanting kingdom of {char1.title()}, there lived a brave adventurer named {char1.title()}.
        {char1.title()} had a magical ability to {v1.lower()} with the wind, making them the hero of the land.
        One day, they crossed paths with {char2.title()}, a wise sorcerer known for their extraordinary {v2.lower()}ing powers.
        Together, they embarked on an epic quest to save the kingdom from a mysterious darkness that threatened to engulf everything.

        Along the way, {char1.title()} and {char2.title()} encountered mythical creatures, solved riddles, and forged unbreakable bonds.
        The journey was perilous, but their friendship and determination prevailed.
        In the heart of the dark forest, they discovered a hidden portal leading to a realm of everlasting sunshine.
        {char1.title()} and {char2.title()} returned to the kingdom, bringing with them the light of hope and a promise of a brighter future.

        The grateful citizens celebrated their triumphant return, and {char1.title()} and {char2.title()} were hailed as the saviors of the realm.
        From that day forward, their names were whispered in legends, and the tale of their courageous adventure was passed down through generations.
        """

    story2= f""" 
            In the vast cosmos, where stars twinkle like distant memories, there lived a daring astronaut named {char1.title()}.
            {char1.title()} dreamed of {v1.lower()}ing among the constellations and exploring the wonders of the universe.
            During a cosmic expedition, they encountered {char2.title()}, an extraterrestrial being with the ability to {v2.lower()} the language of the stars.
            Together, they embarked on a space odyssey, discovering new planets, encountering cosmic phenomena, and forging a cosmic friendship.

            Their journey brought them to the edge of a celestial nebula, where a cosmic gate awaited, promising untold adventures beyond imagination.
            {char1.title()} and {char2.title()} traversed wormholes and danced through asteroid belts, unlocking the secrets of the cosmos.
            As they returned to Earth, they brought with them the wisdom of the stars, enriching humanity with the knowledge of the universe.

            {char1.title()} and {char2.title()}'s interstellar tales echoed through the ages, inspiring future astronomers and space explorers.
            """


    story3 = f""" 
               In the bustling city of {char1.title()}, a talented athlete named {char1.title()} stood out among the crowd.
               Known for their exceptional {v1.lower()}ing skills, {char1.title()} became the star player of the local sports team.
               One day, they crossed paths with {char2.title()}, a legendary coach renowned for their unmatched {v2.lower()}ing strategies.
               Together, they formed an unstoppable team, aiming for victory in the championship and inspiring fans with their passion for the game.

               The championship game was a fierce battle, with {char1.title()} and {char2.title()}'s team facing formidable opponents.
               Through teamwork, determination, and a sprinkle of sportsmanship, they emerged triumphant, lifting the championship trophy high.
               The victory not only brought joy to the city but also ignited a love for sports, encouraging everyone to pursue their athletic dreams.

               {char1.title()} and {char2.title()}'s sportsmanship became a beacon of inspiration, motivating aspiring athletes for generations to come.
               """

    story4 = f""" 
           Once upon a time, in a world filled with wonder, there lived a brave soul named {char1.capitalize()}.
           {char1.capitalize()} possessed the unique ability to {v1.lower()} with the elements, harnessing the power of nature itself.
           One fateful day, {char1.capitalize()} crossed paths with {char2.capitalize()}, a wise sage known for {v2.lower()}ing ancient secrets.
           Together, they embarked on a quest to restore balance to the mystical realms, facing trials and unlocking the mysteries of the universe.

           Amidst the journey, {char1.capitalize()} and {char2.capitalize()} encountered mythical creatures and deciphered cryptic riddles.
           Their bond grew stronger with each challenge, and together, they overcame the darkness threatening to engulf the world.
           In the heart of the enchanted forest, they discovered a hidden portal leading to a realm of eternal harmony and {v2.lower()}ing light.
           {char1.capitalize()} and {char2.capitalize()} returned triumphant, their names echoing in the wind as legends of courage and friendship.

           The grateful inhabitants celebrated their heroes, and {char1.capitalize()} and {char2.capitalize()} were revered as champions of a new era.
           From that day forward, their stories were told around campfires, inspiring generations to come with tales of bravery and the magic of {v1.lower()}ing.
       """

    storylist = [story1, story2, story3, story4]
    told_story= random.choice(storylist)

    return told_story

