# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, words):
        sorted_word = sorted(self.word)
        matches = [word for word in words if sorted(word) == sorted_word]
        return matches
