import json #imports data file 
import difflib #imports standard python module - using for sequence matcher
from difflib import get_close_matches 

data = json.load(open("/Users/trippjohnson/Udemy/Project 1_Dictionary/data.json"))

def lookup(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes, or N for no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist. Please double check your spelling."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exit. Please double check it."

word = input("Enter word: ")

output = lookup(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)