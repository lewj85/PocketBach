import io
import json

oldData = open('hooktheoryData.json', 'r')
oldStr = oldData.read()
oldData.close()
#print(oldStr)

oldJson = json.loads(oldStr)
print(oldJson[155])
print(oldJson[155]["child_path"])
print(len(oldJson))

newDict = {}
newDict["child_path"] = {}

for i in oldJson:
    print(i)
    if i != None:
        if ',' in i["child_path"]:
            newKey = i["child_path"]
            chordKey = newKey[newKey.rindex(',')+1:]  # save the last chord
            newKey2 = newKey[0:newKey.rindex(',')]  # cut off the last chord
            print(chordKey)
            print(newKey2)

            newData = i["probability"]
            # add the new
            newDict[newKey2][chordKey] = newData



#newData = open('hooktheoryData2.json', 'w')

