"""weightedProbability() extracts a new chord from a dictionary with weighted probabilities using child_paths"""
import random
import json

# pass it the past 1-4 chords = "child_path"
def weightedProbability(keyStr):
    # create random num from 0-1
    num1 = random.random()

    # extract the json data
    filename = "../data/hooktheoryfiles/hooktheoryData2.json"
    f = open(filename, 'r')
    checkStr = f.read()
    f.close()
    newDict = json.loads(checkStr)
    #print(newDict["7,6,7,6"])

    probs = newDict[keyStr]
    print(probs)

    for i in probs:
        #print('num1 is '+str(num1)+'. checking '+i+'.')
        # if num1 < first key's value return key
        if num1 <= probs[i]:
            #print('returning '+i)
            return i
        # else subtract that key's value from num1
        else:
            num1 -= probs[i]

    # if there's a problem, return -1 so we know
    return -1


# tests
#weightedProbability('1')
#weightedProbability('7,6,7,6')
