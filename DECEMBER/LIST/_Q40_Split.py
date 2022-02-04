#Split a list based on first character of word
from itertools import groupby
from operator import itemgetter
class List_problems():
    def split_word(self):
        print("")
        print("Q40.SPLIT A LIST BASED ON FIRST CHARECTER OF WORD")
        word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
                     'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

        for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
            print(letter)
            for word in words:
                print(word)

res = List_problems()
res.split_word()