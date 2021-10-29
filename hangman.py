from os import replace
from os import system
import random

# clear Screen Function


def clear(): return system('clear')


clear()

# Banner


def banner():
    print("""
     _                                                   _______
    | |                                                 |/      |
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __       |      (_)
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \      |      /|\\
    | | | | (_| | | | | (_| | | | | | | (_| | | | |     |       |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     |      / \\
                        __/ |                           |
                       |___/                        ____|____
    """)
    menu = {
        1: "Start Game",
        2: "How to Play",
        3: "Rules",
        0: "Quit"
    }
    for num, val in menu.items():
        print(f"\t\t{num}: {val}")

    x = input("Enter: ")

    while(not x.isnumeric()):
        if(not x.isnumeric()):
            x = input("Please Enter a valid input ! : ")

    return int(x)


x = banner()

# Hangman Tries
hangman = {7: """\t\t     _______
\t\t    |/      |
\t\t    |     
\t\t    |      
\t\t    |       
\t\t    |      
\t\t    |
\t\t____|____""",
           6: """\t\t     _______
\t\t    |/      |
\t\t    |      (_)
\t\t    |      
\t\t    |      
\t\t    |      
\t\t    |
\t\t____|____""",
           5: """\t\t    _______
\t\t    |/      |
\t\t    |      (_)
\t\t    |       |
\t\t    |       
\t\t    |      
\t\t    |
\t\t____|____""",
           4: """\t\t     _______
\t\t    |/      |
\t\t    |      (_)
\t\t    |       |
\t\t    |       |
\t\t    |      
\t\t    |
\t\t____|____""",
           3: """\t\t     _______
\t\t    |/      |
\t\t    |      (_)
\t\t    |       |/
\t\t    |       |
\t\t    |      
\t\t    |
\t\t____|____""",
           2: """\t\t     _______
\t\t    |/      |
\t\t    |      (_)
\t\t    |      \|/
\t\t    |       |
\t\t    |      
\t\t    |
\t\t____|____""",
           1: """\t\t     _______
\t\t    |/      |
\t\t    |      (_)
\t\t    |      \|/
\t\t    |       |
\t\t    |      / 
\t\t    |
\t\t____|____""",
           0: """\t\t     _______
\t\t    |/      |
\t\t    |      (_)
\t\t    |      \|/
\t\t    |       |
\t\t    |      / \
\t\t    |
\t\t____|____""", }

# Import wordlist
words = []


def wordlist(path="wordlist.txt"):
    with open(path) as file_in:
        for word in file_in:
            words.append(word.rstrip())


wordlist()

# Getting a random word from the list


def randWord():
    rando = words[random.randint(0, (len(words)-1))]
    return rando


word_after_guess = ''


def game():
    clear()
    # important variables
    rand = randWord()
    randCp = rand

    # converted the string into a list to replace the letters
    global main_word_to_show
    main_word_to_show = list('*'*(len(rand)))

    accepted_letters = list(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    tries = 7

    # Defined this list here so that it is not appended over and over
    listss = list(enumerate(randCp))
    print("Let's Start!!\nSave the hitman from getting hanged by guessing what the word is. . .\n")
    print(hangman.get(7, "Hangman is on vacation !"))
    global word_after_guess
    word_after_guess = ''.join(main_word_to_show)
    print('\n\t\t'+word_after_guess)

    while(tries != 0):
        guessedLetter = input("\nGuess the letter: ")

        # Main Logic
        # find the index of the letter in the word
        # replace the corresponding index of the ******** with the letter from the copy of that word
        # then remove the replaced letter from the copy
        if guessedLetter in randCp and main_word_to_show and accepted_letters:
            for index, char in listss:
                if char == guessedLetter:
                    main_word_to_show[(index)] = guessedLetter
                    randCp = randCp.replace('', guessedLetter)

            word_after_guess = ''.join(main_word_to_show)
            if(word_after_guess == rand):
                clear()
                print("Hooray!! You Won ! The Hitman was saved !")
                print(f"The word was {rand}\n")
                break

            print('\n\t\t'+word_after_guess)

        elif guessedLetter not in accepted_letters:
            print("\n\nPlease enter a valid letter !\n\n")
            print(hangman.get(tries, "Hangman is on vacation !"))
            print('\n\t\t'+word_after_guess)

        elif guessedLetter not in randCp:
            tries -= 1
            print(f"\n\nOoops ! Wrong Guess ! \nYou have {tries} guesses left")
            print(hangman.get(tries, "Hitman is on vacation !"))
            print('\n\t\t'+word_after_guess)

    if(tries == 0):
        clear()
        print("You Lost :( \nPlease try again !")
        print(f"\nThe word was {rand}")


# Menu Traversal
while(x != 0):

    # Start Game
    if(x == 1):
        game()
        x = banner()

    # How to Play
    elif(x == 2):
        clear()
        print("*"*110)
        print("""\t\t    __  __                   __                   __             
\t\t   / / / /____  _      __   / /_ ____     ____   / /____ _ __  __
\t\t  / /_/ // __ \| | /| / /  / __// __ \   / __ \ / // __ `// / / /
\t\t / __  // /_/ /| |/ |/ /  / /_ / /_/ /  / /_/ // // /_/ // /_/ / 
\t\t/_/ /_/ \____/ |__/|__/   \__/ \____/  / .___//_/ \__,_/ \__, /  
\t\t                                      /_/               /____/   
\t\t""")
        print("*"*110)
        print('''You have to guess the word in order to save the hitman who was given a death sentence. You can use the\nfollowing strategies to increase your chances of winning the game.The fact that the twelve most commonly occurring\nletters in the English language are e-t-a-o-i-n-s-h-r-d-l-u(from most to least), along with other letter-frequency\n lists, can be used by you to increase your odds.\n\nBut, you may get a word from the list that deliberately avoids common letters(e.g. rhythm or zephyr) or one\nthat contains rare letters(e.g. jazz).\n\nAnother common strategy is to guess vowels first, as English only has five vowels(a, e, i, o, and u ) and\nalmost every word has at least one. ''')
        y = input("\n\nEnter 00 to go back  : ")
        while(y != '00'):
            if(y != '00'):
                y = input("\n\nPlease enter 00 to go back: ")
        clear()
        x = banner()

    # Rules
    elif(x == 3):
        clear()
        print("*"*100)
        print("""\t\t\t\t   _____ __  __ / /___   _____
\t\t\t\t  / ___// / / // // _ \ / ___/
\t\t\t\t / /   / /_/ // //  __/(__  ) 
\t\t\t\t/_/    \__,_//_/ \___//____/  
\t\t\t\t                              """)
        print("*"*100)
        print("\n\nA word I randomly picked from a wordlist; and the player tries to guess what it is one letter at a time.\n\nThe computer draws a number of dashes equivalent to the number of letters in the word. If a guessing\nplayer suggests a letter that occurs in the word, the computer fills in the blanks with that lette\nin the right places.")
        z = input("\n\nEnter 00 to go back  : ")
        while(z != '00'):
            if(z != '00'):
                z = input("\n\nPlease enter 00 to go back: ")
        clear()
        x = banner()

    else:
        clear()
        print("Please enter a valid option.")
        x = banner()

print("\n\nBye bye !! ;)\n\n\n")
exit()
