import createWordle as create
import styleWordle as style

NUM_GUESSES = 6

def main():
    #wordlist_name = "/Users/hellen/vscode/myWordle/sonnet18.txt"
    wordlist_name = "./sonnet18.txt" # replace with your own list

    ### get secretWord and initialize parameters
    secretWord, word_len = create.get_word(wordlist_name)
    correctGuess, guessCount, guesses = create.initialize_params(word_len)

    while (guessCount < NUM_GUESSES):
        ### show guess board
        style.refresh(guesses, secretWord, guessCount+1)

        ### ask user for guess
        tempGuess = input(f"\nNext guess (^C to quit): ").upper()

        ### user did not enter a valid guess
        isValidGuess = create.validate_guess(tempGuess, word_len,guesses)
        if not isValidGuess:
            continue

        ### user has entered a valid guess
        guesses[guessCount] = tempGuess # guessCount starts at 0
        guessCount += 1

        ### correct guess
        if tempGuess == secretWord:
            correctGuess = True
            break

    create.game_over(correctGuess, guessCount, secretWord, guesses)




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        create.early_exit()

