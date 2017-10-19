"""getNextChord() chooses which chord should be next based on the number of chords remaining, the destination chord, and various weights."""
# it makes use of the random() function when there are multiple options.
# NOTE: rearrange if statements so destination is outer if-else

import weightedProbability as wp
import defineChord as dc
import random

def getNextChord(chordsRemaining, destination, chordArray):
    ###############################################################
    # NEW HOOKTHEORY WAY
    ###############################################################
    # try to get a chord using weightedProbability
    # NOTE: if we fail (if the chord isn't one of the ones in defineChord), newChord will be set to -1
    attempts = 5
    found = 0
    #print(chordArray)
    while attempts and not found:
        attempts -= 1
        if len(chordArray) == 1:
            keyStr = str(chordArray[0])
        elif len(chordArray) == 2:
            keyStr = str(chordArray[0])+','+str(chordArray[1])
        elif len(chordArray) == 3:
            keyStr = str(chordArray[-3])+','+str(chordArray[-2])+','+str(chordArray[-1])
        elif len(chordArray) > 3:
            keyStr = str(chordArray[-4])+','+str(chordArray[-3])+','+str(chordArray[-2])+','+str(chordArray[-1])

        #print('keyStr is '+keyStr)
        newChord = wp.weightedProbability(keyStr)
        #print('newChord is '+str(newChord))
        # if we found a chord
        if newChord:
            # make sure it's a chord we allow!!!
            found = dc.defineChord('C', 1, 1, 0, 0, 0, newChord)
            #print('found is '+str(found))

        # if we allow it, return it along with the inversion, which is in found[1]
        # NOTE: before turning it into an int, pull out the first index with [0]
        # NOTE: this will remove the possibility of 7th chords...
        # TODO: fix the issue in the above NOTES - need to allow 7th chords
        if found:
            return [int(newChord[0]), found[1]]


    ###############################################################
    # OLD HARD-CODING WAY
    ###############################################################
    # if we don't return a value in the above while loop, just do it manually with hard-coded weights
    print('failed to getNextChord via weightedProbability. doing it manually.')

    previousChord = chordArray[-1]
    inversion = 0
    # NOTE: use actual data to derive percentages based on each composer's preferences
    #   pass these preferences as parameters
    if chordsRemaining == 1:      # if on last chord
        if destination == 1:      # if destination is tonic I
            newChord = 5          # return dominant V
        elif destination == 5:    # if destination is dominant V
            num1 = random.random()
            if num1 < 0.5:        # return random predominant ii or IV
                newChord = 4
            else:
                newChord = 2
        elif destination == 4:    # if destination is IV
            newChord = 1          # return V/IV, which is I
        else:
            num1 = random.random()
            if num1 < 0.4:  # 40% chance to move up a fourth
                newChord = previousChord + 3
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            elif num1 < 0.6:  # 20% chance to move up a sixth
                newChord = previousChord + 5
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            elif num1 < 0.75:  # 15% chance to move up a fifth
                newChord = previousChord + 4
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            elif num1 < 0.85:  # 10% chance to move up a second
                newChord = previousChord + 1
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            elif num1 < 0.9:  # 5% chance to move up a third
                newChord = previousChord + 2
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            elif num1 < 0.95:  # 5% chance to move up a seventh
                newChord = previousChord + 6
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            else:  # 5% chance to stay the same
                newChord = previousChord
    elif chordsRemaining == 2:    # if on second to last chord
        if destination == 1:      # if destination is tonic I
            num1 = random.random()
            if num1 < 0.4:        # return random predominant ii or IV
                newChord = 4
            elif num1 < 0.8:
                newChord = 2
            else:
                newChord = 1
                inversion = 2
                #print("I-6/4 chord")
        elif destination == 5:
            num1 = random.random()
            # return random predominant ii/V or IV/V, which is vi or I
            # NOTE: need to consider previous chord to prevent repeating
            # chords. it's allowable, but weights will make it uncommon
            if previousChord == 1:
                if num1 < 0.1:    # only 10% chance to repeat
                    newChord = 1
                else:
                    newChord = 6
            elif previousChord == 6:
                if num1 < 0.1:    # only 10% chance to repeat
                    newChord = 6
                else:
                    newChord = 1
            else:
                if num1 < 0.5:    # otherwise normal 50% chance to return
                    newChord = 6  # ii/V or IV/V (vi or I)
                else:
                    newChord = 1
        elif previousChord == 4:
            num1 = random.random()
            if num1 < 0.8:        # 80% chance to be V
                newChord = 5
            else:
                newChord = 1
        else:
            num1 = random.random()
            if num1 < 0.4:  # 40% chance to move up a fourth
                newChord = previousChord + 3
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            elif num1 < 0.6:  # 20% chance to move up a sixth
                newChord = previousChord + 5
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            elif num1 < 0.75:  # 15% chance to move up a fifth
                newChord = previousChord + 4
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            elif num1 < 0.85:  # 10% chance to move up a second
                newChord = previousChord + 1
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            elif num1 < 0.9:  # 5% chance to move up a third
                newChord = previousChord + 2
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            elif num1 < 0.95:  # 5% chance to move up a seventh
                newChord = previousChord + 6
                if newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
            else:  # 5% chance to stay the same
                newChord = previousChord
    else:
        num1 = random.random()    # return a random chord with specific weights
        # NOTE: these weights should be adjusted based on composer profile data
        # NOTE: this section should be rewritten with weights based on previous
        # chord. ie. if previousChord == 1, 44% chance to go up a fourth, but
        # if previousChord == 5, 62% chance to go up a fourth
        if num1 < 0.4:  # 40% chance to move up a fourth
            newChord = previousChord + 3
            if newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
        elif num1 < 0.6:  # 20% chance to move up a sixth
            newChord = previousChord + 5
            if newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
        elif num1 < 0.75:  # 15% chance to move up a fifth
            newChord = previousChord + 4
            if newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
        elif num1 < 0.85:  # 10% chance to move up a second
            newChord = previousChord + 1
            if newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
        elif num1 < 0.9:  # 5% chance to move up a third
            newChord = previousChord + 2
            if newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
        elif num1 < 0.95:  # 5% chance to move up a seventh
            newChord = previousChord + 6
            if newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
        else:  # 5% chance to stay the same
            newChord = previousChord
        # inversion randomizer
        # NOTE: REMOVED SO THAT GETNEXTNOTE HAS THE POWER TO FIND STEPWISE INVERSIONS - KEEPING 164 FOR CADENCES THOUGH
        #num2 = random.random()
        #if num2 > 0.8:
        #    inversion = random.randint(1,2)

    return [newChord, inversion]