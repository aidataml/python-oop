"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    *** Used to find random words in a dictionary ***
    
    - WordFinder is instantiated with a path to a file on disk that contains words, one word per line
    - It reads that file, and makes an attribute of a list of those words
    - It prints out “[num-of-words-read] words read”
    - It provides a method, random(), which returns a random word from that list of words
    
    >>> word_find = WordFinder("words.txt")
    # words read

    >>> word_find.random() in ["applesauce", "simple", "lazybird"]
    True
    
    """
    
    def __init__(self, path):
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        return [w.strip() for w in dict_file]

    def random(self):
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """
    *** Class of WordFinder that removes blank lines, as well as lines that start with a '#' symbol.
    
    >>> special_word_find = SpecialWordFinder("words.txt")
    # words read

    >>> special_word_find.random() in ["applesauce", "simple", "lazybird"]
    True

    """

    def parse(self, dict_file):

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
