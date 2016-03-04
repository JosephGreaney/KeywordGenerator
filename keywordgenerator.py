# This program generates a list of keywords to be used as prompts to find
# a new book to read each month. The first two words are taken from a list of the most 
# common scrabble dictionary words. The next two words are taken from a list of
# the most common words from science fiction and fantasy novels. The third list
# takes from uncommonly used scrabble words. The words are written to the text
# file keywords.txt

__author__ = "Joe"
__date__ = "$Mar 4, 2016 11:38:21 AM$"

import csv
import random
import datetime

class FileReader:
    
    def __init__(self, name):
        'Creates a csv reader to read the file to list'
        self.name = name
        self.list = []
        with open(self.name, newline = '') as csvfile:
            input = csv.reader(csvfile, delimiter=',')
            for row in input:
                self.list.append(row[0].lower())
    
    def getRandomWord(self):
        'returns a random word from the list'
        return random.choice(self.list)

if __name__ == "__main__":
    keywords = []
    
    # get the current month and year
    today = datetime.datetime.now()
    month = today.strftime("%B") + " " + str(today.year)
    
    print(month)
    # create filereaders for each of our files
    easyWords = FileReader("words/easy.csv")
    commonWords = FileReader("words/commonwords.csv")
    hardWords = FileReader("words/hard.csv")
    
    keywords.append(easyWords.getRandomWord())
    keywords.append(easyWords.getRandomWord())
    keywords.append(commonWords.getRandomWord())
    keywords.append(commonWords.getRandomWord())
    keywords.append(hardWords.getRandomWord())
    keywords.append(hardWords.getRandomWord())
    
    # append to keywords file
    with open("Keywords.txt", "a") as f:
        f.write(month + "\n")
        f.write(', '.join(keywords) + "\n\n")
        
    print(keywords)