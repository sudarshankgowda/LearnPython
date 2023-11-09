import random
import string

from words import words
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    print(f"Choosed word is :{word}")
    word_letters = set(word)
    print(f"Letters in the word {word} are {word_letters}")
    alphabets = set(string.ascii_uppercase)
    print(f"content of alphbets is {alphabets}")
    used_letters = set()
    print(f"Used letters are : {used_letters}")

    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print(f'You have only {lives} lives left and You have used these letters : ', ' '.join(used_letters))

        #word_list = [letter if letter in used_letters else '-' for letter in word]
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('-')

        print('Current word : ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabets - used_letters:
            #print(user_letter)
            used_letters.add(user_letter)
            #print(f"Used letters are : {used_letters}")
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                #print(f"Remaining word_letters after guessing are : {word_letters}")
            else:
                lives = lives-1
                print("Letter is not in word")
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again. ")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print('You died, Sorry. The word was ', word)
    else:
        print('You guessed the word ', word, '!!')
hangman()


