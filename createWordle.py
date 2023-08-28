import random
from string import ascii_letters
import styleWordle as style
import time



### pre-game
def request_word_length(max=7, min=2):
    """
    Requests user to input a word length between min and max letters long (inclusive)

    Arguments:
    max -- maximum length of the word
    min -- minimum length of the word

    Returns:
    word_len -- chosen word length (or default length of 5 if user did not properly enter length)
    """
    word_len = 0

    while (word_len < min or word_len > max):
        try:
            word_len = int(input(f"Input an integer word length between {min} and {max} (^C to quit): "))
        except ValueError:
            style.c_print("warning", "word_len_ValueError")
            time.sleep(1.5)
            word_len = 5
            break
        except KeyboardInterrupt:
            early_exit()
        except:
            style.c_print("warning","word_len_error")
            time.sleep(1.5)
            word_len = 5
            break
        
    return word_len


def choose_randm_word(input_file, word_len):
    """
    Retrieves a random word of correct length from given input txt file
    
    Arguments:
    input_file -- str path of file containing list of possible words
    word_len -- length chosen by user that secretWord must be
    
    Returns:
    secretWord -- random word from wordlist_file to be guessed during the game
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        if words := [
            word.upper()
            for word in f.read().split()
            if len(word) == word_len and all(letter in ascii_letters for letter in word)
        ]:
            return random.choice(words)
        else: # check to make sure word list file is not empty
            style.c_print("warning","no_words")
            raise SystemExit()


def get_word(input_file):
    """
    Asks user for a word length then chooses a random word of given length from input_file
    
    Arguments:
    input_file -- str path of file containing list of possible words

    Returns:
    secretWord -- randomly chosen word from the input word list that will be used as the game's secret word
    word_len -- the inputed word length
    """
    word_len = request_word_length()
    secretWord = choose_randm_word(input_file, word_len)

    return secretWord, word_len
    
    





### during game
def initialize_params(word_len):
    """
    Initialize variables to be used for wordle game

    Arguments:
    word_len -- length of the secret word

    Return:
    correctGuess -- boolean for whether the word has been guessed (initialize to False)
    guessCount -- number of guesses made (initialize to 0)
    guesses -- list of size 6 to contain user's guesses
    """
    correctGuess = False
    guessCount = 0
    guesses = ["_"*word_len] * 6

    return correctGuess, guessCount, guesses

def validate_guess(tempGuess, word_len, guesses):
    """
    Determine if user has entered a valid guess
    
    Arguments:
    tempGuess -- user's guess
    word_len -- expected length of user input
    guesses -- list of user's previous guesses

    Return:
    isValid -- boolean representing if user entered valid input or not
    """
    isValid = False

    if (len(tempGuess) != word_len) :
        style.c_print("warning","length")
    elif any((invalid := letter) not in ascii_letters for letter in tempGuess):
        style.c_print("warning","invalid")
    elif tempGuess in guesses:
        style.c_print("message","repeat")
    else:
        isValid = True
    
    return isValid







### after game
def game_over(correctGuess, guessCount, secretWord, guesses):
    """
    Perform the appropriate actions depending on if the guess is correct/incorrect
        or the user desires to quit

    Arguments:
    correctGuess -- boolean representing if the user has correctly guessed
    guessCount -- the number of times the user has guessed
    secretWord -- the true word, unknown to user
    guesses -- list of all guesses made by user

    Return:
    """
    style.game_over()
    style.show_guesses(guesses, secretWord)

    if (correctGuess):
        style.c_print("message","correct")

    if (not correctGuess and guessCount >= 6):
        style.c_print("message","guesses_used")
    
    style.console.print("The word was " + secretWord + ".", style="answer")


def early_exit():
    """
    Inform user that they have quit and reveal the secret word
    """
    style.game_over()
    style.c_print("message","quit")
    raise SystemExit()
