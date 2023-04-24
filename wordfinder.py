"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """ Finds random words in the the dictionary.

    wf = WordFinder("simple.txt")
    3 words will be read

    wf.random() in["cat","dog","porcupine"]
    True"""
    
    def __init__(self,path):
        """ Read dictionary and return # of items read"""
        dict_file=open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    
    def parse(self,dict_file):
        """ Parse dict-file -> list of words"""
        return [w.strip() for w in dict_file]

    def random(self):
        """ Return random word."""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """ Specialized word finder that will exclude blank lines/comment
    swf = SpecialWordFinder("words.txt")
    
    swf.random() in ["pear", "carrot" , "kale"]
    True
    """
    def parse(self,dict_file):
        return [w.strip() for w in dict_file
            if w.strip() and not w.startswith("#")]
