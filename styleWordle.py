from rich.console import Console
from rich.theme import Theme
from string import ascii_letters, ascii_uppercase
import time


themes = {
    "warning": "bold red on white",
    "message": "bold yellow on blue",
    "answer": "bold white on green"
}
user_warnings = {
    "length": "Input is not the correct length. Please try again.",
    "invalid": "User has entered an invalid letter. Please use English letters.",
    "word_len_ValueError": "User failed to enter proper value. Word length has been set to the default, 5 letters.",
    "word_len_error": "An error occurred. Word length has been set to the default, 5 letters.",
    "no_words": "No words of length 5 are in the word list."
}
user_messages = {
    "quit": "\nUser has exited game.",
    "repeat": "User has already guessed this word before. Please guess something different.",
    "correct": "Correct! Nice job!",
    "guesses_used": "User has used up all guesses."
}


console = Console(width=80, theme=Theme(themes)) # was initially width=40




def c_print(theme, key):
    """
    Console prints given statement based on theme and key

    Arguments:
    theme -- either "warning" or "message"
    key -- str dictionary key for desired statement to print

    Return:
    """
    dict = user_warnings if theme=="warning" else user_messages
    
    console.print(dict[key], style=theme)
    time.sleep(1.5)


def refresh(guesses, secretWord, guess):
    """
    Refreshes console to output updated visualization of current guesses,
        along with each guess's correct, misplaced, and incorrect letters
        
    Arguments:
    guesses -- array of all guesses
    secretWord -- the answer word
    guess -- which guess the user is/was on
    
    ### potential refreshes when:
    1) beginning of while loop (guess = guessCount+1)
    after while loop:
    2) player quit (guess = guessCount+1)
    3) player ran out of turns (guess = guessCount)
    4) player guessed correctly (guess = guessCount)
    """
    console.clear()

    headline = f"Guess {guess}"
    console.rule(f":tulip::tulip: " + "[bold white on green]"+headline+"[/]" + " :tulip::tulip:")

    show_guesses(guesses, secretWord)


def show_guesses(guesses, secretWord):
    """
    Outputs a visualization of current guesses,
        along with each guess's correct, misplaced, and incorrect letters,
        and a line showing the status of each letter in the alphabet
        
    Arguments:
    guesses - array of all guesses
    secretWord - the answer word
    
    Returns:
    """
    # line of all letters and their status
    letter_status = {letter: letter for letter in ascii_uppercase}

    # categorize letters in guess
    for guess in guesses:
        styled_guess = []
        for letter, answer in zip(guess, secretWord):
            # correct
            if letter == answer:
                style = "bold white on green"
            # misplaced
            elif letter in secretWord:
                style = "bold white on yellow"
            # incorrect
            elif letter in ascii_letters:
                style = "white on #666666"
            # unused guess
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")

            if letter != "_":
                letter_status[letter] = f"[{style}]{letter}[/]"
        console.print("".join(styled_guess), justify="center")
    console.print("\n"+"".join(letter_status.values()),justify="center")


def game_over():
    """
    Display a "GAME OVER" headline over the ending game board
    """
    console.clear()
    console.rule(f":tulip::tulip: " + "[bold white on green] GAME OVER [/]" + " :tulip::tulip:")
