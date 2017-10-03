"""weightedProbability() extracts a new chord from a dictionary with weighted probabilities using child_paths"""
import random
import json

# pass it the past 1-4 chords = "child_path"
def weightedProbability(keyStr):
    # create random num from 0-1
    num1 = random.random()

    # extract the json data
    filename = "/hooktheoryfiles/hooktheoryData2.json"
    f = open(filename, 'r')
    newDict = dict()
    json.dump(newDict, f)
    f.close()

    probs = newDict[keyStr]

    for i in probs:
        # if num1 < first key's value return key
        if num1 <= i["probability"]:
            return i.key
        # else subtract that key's value from num1
        else:
            num1 -= i["probability"]

    # shouldn't make it this far, but if there's a problem, just return '1'
    return '1'
