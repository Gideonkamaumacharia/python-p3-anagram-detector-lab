# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word

    def match(self,word_list):
        anagrams = []
        for w in word_list:
            if sorted(w.lower()) == sorted(self.word.lower()) and w.lower() != self.word.lower():
                anagrams.append(w)
        return anagrams