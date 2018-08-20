import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yes_no = input("Did you mean {} instead? Enter Y if yes, or N if No: ".format(get_close_matches(word, data.keys())[0])).upper()
        if yes_no == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yes_no == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
