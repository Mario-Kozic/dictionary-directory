import json
from difflib import get_close_matches

data = json.load(open('data.json'))



# setting up out function

def translate(w):
    # condition that will look for out word in data set
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))> 0:
        # our prompt in case user error/ miss spelling
        yesOrNo = input('Did you mean %s instead? Enter Y if yes, or N if no: ' % get_close_matches(w, data.keys())[0])
        if yesOrNo == 'Y':
            return  data[get_close_matches(w, data.keys())[0]]
        elif yesOrNo == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

# variables

word = input('Enter word: ')
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)