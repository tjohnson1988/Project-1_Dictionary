import json #imports data file 
#import difflib #imports standard python module - using for sequence matcher

data = json.load(open("/Users/trippjohnson/Udemy/Project 1_Dictionary/data.json"))

def lookup(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exit. Please double check it."

word = input("Enter word: ")

print(lookup(word))