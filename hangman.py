import random


stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

user_lives = 6
print("welcome to the hangman game")

word_list = ["astronaut", "awkward", "bagpipes", "bicycle", "blizzard", "campfire", "concept", "crypt", "dolphin", "dragonfly", "dwarf", "echo", "eclipse", "flamingo", "fjord", "galaxy", "garden", "gossip", "haiku", "horizon", "ivory", "jacket", "jigsaw", "jockey", "journey", "khaki", "kingdom", "kitten", "labyrinth", "luxury", "monster", "mystery", "naphtha", "octopus", "oxygen", "phantom", "pizza", "planet", "pyramid", "puzzling", "quartz", "rhythm", "rocket", "safari", "shadow", "sphinx", "summer", "swivel", "tornado", "turtle", "twelfth", "unknown", "volcano", "vortex", "wave", "whisper", "wizard", "yacht", "zephyr" ]
guess_word = random.choice(word_list)

#print(guess_word)

place_holder = ""
for i in range(len(guess_word)):
    place_holder += "_"
    
print(place_holder)

loop = False
extra_list = []

while not loop :
    user_guess = input("guess a word: ").lower() 

    if user_guess in extra_list:
        print(f"you have already guessed {user_guess} !!!!!!!!")

    display = ""


    for i in guess_word:
        if i == user_guess:
            display += i
            extra_list.append(i)

        elif i in extra_list:
            display += i

        else:
            display += "_"
            
    print(display)

    if user_guess not in guess_word:
        user_lives -= 1
        print(f"*************** wrong you have {user_lives} lives left/6 ******************")
    else:
        print("correct guess!")


    print((stages[6 - user_lives]))
    

    if user_lives == 0:
        loop = True
        print(f"********************************** game over! Better luck next time. the word was: {guess_word}*****************************")
 
    elif "_" not in display:
      loop = True
      print("*************************************** congratulations! you win!!! *******************************************************")
