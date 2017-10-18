import json

oldData = open('hooktheoryData.json', 'r')
oldStr = oldData.read()
oldData.close()
#print(oldStr)

oldJson = json.loads(oldStr)
#print(oldJson[155])
# {'chord_ID': '464', 'chord_HTML': 'IV<sup>6</sup><sub>4</sub>', 'probability': 0.003, 'child_path': '3,464'}
#print(oldJson[155]["child_path"])
# 3,464
#print(len(oldJson))
# 8646


# NOTE: THE NEW DICTIONARY DOES NOT GIVE PERCENTAGES FOR FIRST CHORDS
#   it only returns probabilities for chords after the first!!!!
#   another way to put it: a child_path must exist

newDict = dict()

for i in oldJson:
    #print(i)
    if i is not None:
        if ',' in i["child_path"]:
            newKey = i["child_path"]
            chordKey = newKey[newKey.rindex(',')+1:]  # save the last chord
            newKey2 = newKey[0:newKey.rindex(',')]  # cut off the last chord
            print(chordKey)
            print(newKey2)

            newData = i["probability"]
            # if the child_path doesn't exist yet, add it as a new dictionary
            if not(newKey2 in newDict):
                newDict[newKey2] = dict()
            # then we can add key:value pairs to it
            newDict[newKey2][chordKey] = newData


fileNew = open('hooktheoryData2.json', 'w')
json.dump(newDict, fileNew)
fileNew.close()

# check to see if it's working
fileCheck = open('hooktheoryData2.json', 'r')
checkStr = fileCheck.read()
fileCheck.close()
jsonCheck = json.loads(checkStr)
print(jsonCheck["7,6,7,6"])
