"""weightedProbability() extracts a new chord from a dictionary with weighted probabilities using child_paths"""
import random
import json

# pass it the past 1-4 chords = "child_path"
def weightedProbability(keyStr):
    # create random num from 0-1
    num1 = random.random()

    # extract the json data
    filename = "../data/hooktheory/hooktheoryData2.json"
    f = open(filename, 'r')
    checkStr = f.read()
    f.close()
    newDict = json.loads(checkStr)
    #print(newDict["7,6,7,6"])

    # need to remove any inversions from the keyStr so

    probs = newDict.get(keyStr,0)
    #print(probs)

    if not probs:
        return 0

    for chord in probs:
        #print('num1 is '+str(num1)+'. checking '+i+'.')
        # if num1 < first key's value return key
        if num1 <= probs[chord]:
            #print('returning '+i)
            return chord
        # else subtract that key's value from num1
        else:
            num1 -= probs[chord]


# tests
#weightedProbability('1')
#weightedProbability('7,6,7,6')
