# Constants
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

def mad_libs():
    # Get user input
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")

    # Create the sentence
    sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"

    # Print the sentence
    print(sentence)

mad_libs()
