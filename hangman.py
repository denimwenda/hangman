import random
from words import word


def get_valid_word(words):
    words = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in words:
        words = random.choice(words)

    return word

def hangman(string, words):
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # Getting user input.
    while len(word_letters) > 0:
        # Letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have used this letters: ', ' '.join(used_letters))

        # What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]        
        used_letter = input("Guess a letter: ").upper()
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if used_letter in word_letters:
                word_letters.remove(used_letter)

        elif used_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')


hangman()