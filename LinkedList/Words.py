# This is the words class
class Words:
    def __init__(self, word, count = 1):
        self._word = str(word)
        self._count = int(count)

    @property
    def word(self):
        return self._word
    @word.setter
    def word(self, word):
        self._word = word
    @property
    def count(self):
        return self._count
    #@count.setter
    def count_set(self, count):
        self._count = count
        
    def __str__(self):
        return self._word
    
    
    
        