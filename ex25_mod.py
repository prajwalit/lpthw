""" Exercise 25 - Module """

def break_words (string):
    """This function will break words for us."""
    return string.split(' ')
    
def sort_words (words):
    """Sorts the words."""
    return sorted (words)

def print_first (words):
    """Prints first word after popping it off."""
    word = words.pop(0)
    print word

def print_last (words):
    """Prints last word after popping it off."""
    word = words.pop(-1)
    print word
    
def sort_sentence (sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words (sentence)
    return sort_words (words)

def print_first_and_last (sentence):
    """Prints first and last words of the sentence."""
    words = break_words (sentence)
    print_first (words)
    print_last (words)

def print_first_and_last_sorted (sentence):
    """Prints first and last words of the sentence after sorting it."""
    words = sort_sentence (sentence)
    print_first (words)
    print_last (words)
