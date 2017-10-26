# getRhythm returns an array of note durations for 1 full measure (rather than 1 note at a time)

import random

def getRhythm(finalMTX, measure, measures, timeSig, voice=0, maxVoices=3, choraleOrFugue=0, subject=[]):
    rhythmArr = []
    newArr = []
    if measure == measures:  # if on the last measure, return a whole note
        return '1'
    elif measure == 1:  # if on the first measure
        if choraleOrFugue == 0:  # if a chorale
            num1 = random.random()
            # pick a random (common) rhythm
            randRhythm(timeSig, 0, 1)
            # TODO: fill this section
            pass

        else:  # if a fugue
            # TO DO: fill this section
            pass  # use subject

    else:
        num1 = random.random()
        if choraleOrFugue == 0:  # if a chorale
            if measure in [9,10,11,12]:  # measures 9-12
                # get index of current measure-8
                k = 0
                while finalMTX[maxVoices-1][k][11] != measure-8:
                    k+=1
                if num1 < 0.6:  # 60% chance to copy the same rhythms from measures 1-4
                    while finalMTX[maxVoices-1][k][11] == measure-8:  # while on the same measure
                        rhythmArr.append(finalMTX[maxVoices-1][k][1])
                        k+=1
                elif num1 < 0.9:  # 30% chance to pick a similar rhythm from measures 1-4
                    while finalMTX[maxVoices-1][k][11] == measure-8:
                        newArr.append(finalMTX[maxVoices-1][k][1])
                    rhythmArr = similarRhythm(newArr)
                else:  # just randomize
                    rhythmArr = randRhythm(timeSig, finalMTX[maxVoices-1][measure][3])  # pass interval
            else:  # just randomize
                rhythmArr = randRhythm(timeSig, finalMTX[maxVoices-1][measure][3])  # pass interval

    return rhythmArr


def randRhythm(timeSig, interval = 0, common = 0, numOfNotes = 0):
    choices = []
    num1 = random.random()
    if timeSig == [4,4]:
        ##########################################################################
        # NOTE: PRIORITY GOES TO numOfNotes OVER ANYTHING ELSE!
        # IF numOfNotes IS SPECIFIED IN PARAMS, WE MUST RETURN THAT NUMBER OF RHYTHMS!
        # random number of notes is decided in numOfNotes generator, not randRhythm()
        ##########################################################################
        if common == 1:
            if numOfNotes == 1:
                return ['1']
            elif numOfNotes == 2:
                return ['2', '2']
            elif numOfNotes == 3:
                choices = [['2', '4', '4'], ['4', '4', '2']]
            elif numOfNotes == 4:
                return ['4', '4', '4', '4']
            else:
                choices = [['1'], ['2', '2'], ['2', '4', '4'], ['4', '4', '2'], ['4', '4', '4', '4']]
        else:
            if numOfNotes == 1:
                return ['1']
            elif numOfNotes == 2:
                choices = [['2~', '4', '4'], ['2', '2']]
            elif numOfNotes == 3:
                choices = [['2~', '4', '8', '8'], ['2~', '8', '8', '4'], ['2', '4~', '8', '8'], ['2', '4', '4'],
                           ['4~', '8', '8', '2'], ['4', '4~', '4', '4'], ['4', '4', '2']]
            elif numOfNotes == 4:
                choices = [['2~', '8', '8', '8', '8'], ['2', '4', '8', '8'], ['2', '8', '8', '4'],
                           ['4~', '8', '8', '4~', '8', '8'], ['4~', '8', '8', '4', '4'], ['4', '4~', '4', '8', '8'],
                           ['4', '4~', '8', '8', '4'], ['4', '4', '4~', '8', '8'], ['4', '4', '4', '4'],
                           ['4', '8', '8', '2'], ['8', '8', '4~', '4', '4'], ['8', '8', '4', '2']]
            elif numOfNotes == 5:
                choices = [['2', '8', '8', '8', '8'], ['4~', '8', '8', '4', '8', '8'], ['4~', '8', '8', '8', '8', '4'],
                           ['4', '4~', '8', '8', '8', '8'], ['4', '4', '4', '8', '8'], ['4', '4', '8', '8', '4'],
                           ['4', '8', '8', '4~', '8', '8'], ['4', '8', '8', '4', '4'], ['8', '8', '4~', '4', '8', '8'],
                           ['8', '8', '4~', '8', '8', '4'], ['8', '8', '4', '4~', '8', '8'], ['8', '8', '4', '4', '4'],
                           ['8', '8', '8', '8', '2']]
            elif numOfNotes == 6:
                choices = [['4~', '8', '8', '8', '8', '8', '8'], ['4', '4', '8', '8', '8', '8'],
                           ['4', '8', '8', '4', '8', '8'],
                           ['4', '8', '8', '8', '8', '4'], ['8', '8', '4~', '8', '8', '8', '8'],
                           ['8', '8', '4', '4', '8', '8'],
                           ['8', '8', '4', '8', '8', '4'], ['8', '8', '8', '8', '4~', '8', '8'],
                           ['8', '8', '8', '8', '4', '4']]
            elif numOfNotes == 7:
                choices = [['4', '8', '8', '8', '8', '8', '8'], ['8', '8', '4', '8', '8', '8', '8'],
                           ['8', '8', '8', '8', '4', '8', '8'],
                           ['8', '8', '8', '8', '8', '8', '4']]
            elif numOfNotes == 8:
                choices = [['8', '8', '8', '8', '8', '8', '8', '8']]

            # ELSE NO numOfNotes SET, SO CONSIDER interval INSTEAD - HERE, WE CAN BE RANDOM
            else:
                # NOTE: the 'else' here shouldn't occur anymore - reduced interval requests in writeSubject to -3:4
                if interval == 0:
                    choices = [['2~', '4', '4'], ['2~', '8', '8', '8', '8'],
                               ['2', '2'], ['2', '4', '8', '8'], ['2', '8', '8', '4'],
                               ['4~', '8', '8', '4~', '8', '8'], ['4~', '8', '8', '4', '4'], ['4~', '8', '8', '8', '8', '8', '8'],
                               ['4', '4~', '4', '8', '8'], ['4', '4~', '8', '8', '4'], ['4', '4', '4~', '8', '8'], ['4', '4', '4', '4'],
                               ['4', '4', '8', '8', '8', '8'], ['4', '8', '8', '2'], ['4', '8', '8', '4', '8', '8'], ['4', '8', '8', '8', '8', '4'],
                               ['8', '8', '4~', '4', '4'], ['8', '8', '4~', '8', '8', '8', '8'], ['8', '8', '4', '2'], ['8', '8', '4', '4', '8', '8'],
                               ['8', '8', '4', '8', '8', '4'], ['8', '8', '8', '8', '4~', '8', '8'], ['8', '8', '8', '8', '4', '4'],
                               ['8', '8', '8', '8', '8', '8', '8', '8']]
                elif interval == 1 or interval == -1:
                    choices = [['1'],
                               ['2~', '4', '8', '8'], ['2~', '8', '8', '4'],
                               ['2', '4~', '8', '8'], ['2', '4', '4'], ['2', '8', '8', '8', '8'],
                               ['4~', '8', '8', '2'], ['4~', '8', '8', '4', '8', '8'], ['4~', '8', '8', '8', '8', '4'],
                               ['4', '4~', '4', '4'], ['4', '4~', '8', '8', '8', '8'], ['4', '4', '2'], ['4', '4', '4', '8', '8'],
                               ['4', '4', '8', '8', '4'], ['4', '8', '8', '4~', '8', '8'], ['4', '8', '8', '4', '4'], ['4', '8', '8', '8', '8', '8', '8'],
                               ['8', '8', '4~', '4', '8', '8'], ['8', '8', '4~', '8', '8', '4'], ['8', '8', '4', '4~', '8', '8'],
                               ['8', '8', '4', '4', '4'], ['8', '8', '4', '8', '8', '8', '8'], ['8', '8', '8', '8', '2'],
                               ['8', '8', '8', '8', '4', '8', '8'], ['8', '8', '8', '8', '8', '8', '4']]
                elif interval == 2 or interval == -2:
                    choices = [['2~', '4', '4'], ['2~', '8', '8', '8', '8'],
                               ['2', '2'], ['2', '4', '8', '8'], ['2', '8', '8', '4'],
                               ['4~', '8', '8', '4~', '8', '8'], ['4~', '8', '8', '4', '4'], ['4~', '8', '8', '8', '8', '8', '8'],
                               ['4', '4~', '4', '8', '8'], ['4', '4~', '8', '8', '4'], ['4', '4', '4~', '8', '8'], ['4', '4', '4', '4'],
                               ['4', '4', '8', '8', '8', '8'], ['4', '8', '8', '2'], ['4', '8', '8', '4', '8', '8'],
                               ['4', '8', '8', '8', '8', '4'],
                               ['8', '8', '4~', '4', '4'], ['8', '8', '4~', '8', '8', '8', '8'], ['8', '8', '4', '2'], ['8', '8', '4', '4', '8', '8'],
                               ['8', '8', '4', '8', '8', '4'], ['8', '8', '8', '8', '4~', '8', '8'], ['8', '8', '8', '8', '4', '4'],
                               ['8', '8', '8', '8', '8', '8', '8', '8']]
                elif interval == 3 or interval == -3:
                    choices = [['2~', '4', '8', '8'], ['2~', '8', '8', '4'],
                               ['2', '4~', '8', '8'], ['2', '4', '4'], ['2', '8', '8', '8', '8'],
                               ['4~', '8', '8', '2'], ['4~', '8', '8', '4', '8', '8'], ['4~', '8', '8', '8', '8', '4'],
                               ['4', '4~', '4', '4'], ['4', '4~', '8', '8', '8', '8'], ['4', '4', '2'], ['4', '4', '4', '8', '8'],
                               ['4', '4', '8', '8', '4'], ['4', '8', '8', '4~', '8', '8'], ['4', '8', '8', '4', '4'],
                               ['4', '8', '8', '8', '8', '8', '8'],
                               ['8', '8', '4~', '4', '8', '8'], ['8', '8', '4~', '8', '8', '4'], ['8', '8', '4', '4~', '8', '8'],
                               ['8', '8', '4', '4', '4'], ['8', '8', '4', '8', '8', '8', '8'], ['8', '8', '8', '8', '2'],
                               ['8', '8', '8', '8', '4', '8', '8'], ['8', '8', '8', '8', '8', '8', '4']]
                elif interval == 4 or interval == -4:
                    # same as interval == 2 / -2 except for ['2~', '4', '4'], ['2', '2']
                    choices = [['2~', '8', '8', '8', '8'],
                               ['2', '4', '8', '8'], ['2', '8', '8', '4'],
                               ['4~', '8', '8', '4~', '8', '8'], ['4~', '8', '8', '4', '4'], ['4~', '8', '8', '8', '8', '8', '8'],
                               ['4', '4~', '4', '8', '8'], ['4', '4~', '8', '8', '4'], ['4', '4', '4~', '8', '8'], ['4', '4', '4', '4'],
                               ['4', '4', '8', '8', '8', '8'], ['4', '8', '8', '2'], ['4', '8', '8', '4', '8', '8'],
                               ['4', '8', '8', '8', '8', '4'],
                               ['8', '8', '4~', '4', '4'], ['8', '8', '4~', '8', '8', '8', '8'], ['8', '8', '4', '2'], ['8', '8', '4', '4', '8', '8'],
                               ['8', '8', '4', '8', '8', '4'], ['8', '8', '8', '8', '4~', '8', '8'], ['8', '8', '8', '8', '4', '4'],
                               ['8', '8', '8', '8', '8', '8', '8', '8']]
                else:  # otherwise just use a random choice
                    print('interval greater than +/-4, going with random choice')
                    choices = [['1'],
                               ['2~', '4', '4'], ['2~', '4', '8', '8'], ['2~', '8', '8', '4'], ['2~', '8', '8', '8', '8'],
                               ['2', '2'], ['2', '4~', '8', '8'], ['2', '4', '4'], ['2', '4', '8', '8'], ['2', '8', '8', '4'], ['2', '8', '8', '8', '8'],
                               ['4~', '8', '8', '2'], ['4~', '8', '8', '4~', '8', '8'], ['4~', '8', '8', '4', '4'],
                               ['4~', '8', '8', '4', '8', '8'], ['4~', '8', '8', '8', '8', '4'], ['4~', '8', '8', '8', '8', '8', '8'],
                               ['4', '4~', '4', '4'], ['4', '4~', '4', '8', '8'], ['4', '4~', '8', '8', '4'],
                               ['4', '4~', '8', '8', '8', '8'], ['4', '4', '2'], ['4', '4', '4~', '8', '8'], ['4', '4', '4', '4'],
                               ['4', '4', '4', '8', '8'], ['4', '4', '8', '8', '4'], ['4', '4', '8', '8', '8', '8'], ['4', '8', '8', '2'],
                               ['4', '8', '8', '4~', '8', '8'], ['4', '8', '8', '4', '4'], ['4', '8', '8', '4', '8', '8'],
                               ['4', '8', '8', '8', '8', '4'], ['4', '8', '8', '8', '8', '8', '8'],
                               ['8', '8', '4~', '4', '4'], ['8', '8', '4~', '4', '8', '8'], ['8', '8', '4~', '8', '8', '4'],
                               ['8', '8', '4~', '8', '8', '8', '8'], ['8', '8', '4', '2'], ['8', '8', '4', '4~', '8', '8'], ['8', '8', '4', '4', '4'],
                               ['8', '8', '4', '4', '8', '8'], ['8', '8', '4', '8', '8', '4'], ['8', '8', '4', '8', '8', '8', '8'],
                               ['8', '8', '8', '8', '2'], ['8', '8', '8', '8', '4~', '8', '8'], ['8', '8', '8', '8', '4', '4'],
                               ['8', '8', '8', '8', '4', '8', '8'], ['8', '8', '8', '8', '8', '8', '4'], ['8', '8', '8', '8', '8', '8', '8', '8']]


    index = random.randint(0,len(choices)-1)

    # add beat numbers and downbeat bools to each value before returning list
    final = addBeatData(choices[index])

    return final


def addBeatData(rhythms):
    newRhythms = []
    total = 0
    # first convert to decimals with dictionary
    for i in rhythms:
        value = {
            '1': 4,
            '2~': 3,
            '2': 2,
            '4~': 1.5,
            '4': 1,
            '8~': 0.75,
            '8': 0.5,
            '16': 0.25
        }.get(i, -1)
        downbeat = 0
        if total == int(total):
            downbeat = 1
        accented = 0
        if total == 0 or total == 2:
            accented = 1
        newRhythms.append([i, int(total)+1, downbeat, accented])
        total += value
    return newRhythms


def similarRhythm(oldRhythm):

    # based on old rhythm, look up an array of similar rhythms
    # NOTE: must put spaces after commas in keys!!! I tested this.
    choices = {
        "['1']": [['1'],['2','2'],['2~','4','4']],
        "['2','2']": [['2','2'],['2~','4','4'],['2','4','4']]
        # TO DO: add more keys and similar rhythms
    }.get(str(oldRhythm),[oldRhythm,])  # NOTE: we have to default to [oldRhythm,] instead of just oldRhythm
                                        #   or indexing below will cause an error

    # pick a random similar rhythm from the list
    return choices[random.randint(0,len(choices)-1)]
