# getRhythm returns an array of note durations for 1 full measure (rather than 1 note at a time)

import random

def getRhythm(finalMTX, measure, measures, timeSig=[4,4], choraleOrFugue=0, subjectLength=2, voice=0, maxVoices=3):

    if measure == measures:  # if on the last measure, return a whole note
        return '1'
    elif measure == 1:  # if on the first measure, pick a random (common) rhythm
        num1 = random.random()
        rhythmArr = []

        # blah

    else:
        num1 = random.random()
        rhythmArr = []

        if choraleOrFugue == 0:
            # 80% chance to copy the same rhythms from measures 1-4 to 9-12
            for i in range(9, 13):
                j = 0
                while finalMTX[j][11][maxVoices] == measure:  # while on the same measure
                    if num1 < 0.8:
                        rhythmArr.append(finalMTX[j][1][maxVoices])
                    else:
                        rhythmArr = randRhythm()

    return rhythmArr


def randRhythm(timesig):
    Choices = []
    if timesig == [4,4]:
        Choices = [['1'], ['2~','4','4'], ['2~','4','8','8'], ['2~','8','8','4'], ['2~','8','8','8','8'],
                   ['2','2'], ['2','4','4'], ['2','4','8','8'], ['2','8','8','4'], ['2','4','8','8'],
                   ['2','8','8','8','8'], ['4.','8','2'], ['4.','8','4.','8'], ['4.','8','4','4'],
                   ['4.','8','4','8','8'], ['4.','8','8','8','4'], ['4.','8','8','8','8','8'], ['4','4~','2'],
                   ['4','4~','4','4'], ['4','4~','4','8','8'], ['4','4~','8','8','4'], ['4','4~8','8','8','8'],
                   ['4','4','2'], ['4','4','4.','8'], ['4','4','4','4'], ['4','4','4','8','8'],
                   ['4','4','8','8','4'], ['4','4','8','8','8','8'], ['4','8','8','2'], ['4','8','8','4.','8'],
                   ['4','8','8','4','4'], ['4','8','8','4','8','8'], ['4','8','8','8','8','4'],
                   ['4','8','8','8','8','8','8'], ['8','8','4~','8','4'],     ]
    index = random.randint(len(Choices))  # note: randint(a, b) b is inclusive
    return Choices[index]

DurArray = [4,3,2,1,.5]
for i in DurArray:
    while









    # try:
#     print('opening a file')
#     o = open('banana.txt')
# except IOError as nameitwhatever:
#     print(nameitwhatever)
# except Exception as anothername:
#     print(anothername)
# finally:
#     print('why does this belong here?')