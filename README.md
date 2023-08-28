This is a summer project study on building a simple command-line application.

To play:
* create virtual environment with python -m venv .env 
* activate .env with source venv/bin/activate 
* install rich with python -m pip install rich
* now the command python myWordle.py will start the game



Project has helped me learn to:
* work step by step to create a command-line application, starting from a basic model then
honing in on more complex details
* use Rich's console to create an attractive user interface in the terminal
* read and validate user input
* work with different representations of data (as strings, lists, dictionaries, etc)
* work with data stored in text files




Shortcomings
* user is allowed to enter words that don't exist
* when words are read from the input file is read, there is no check that they exist
* error messages could be more specific
* could change to let user enter a path for a text file to read words from
