# Chord Writer
# Jesse Lew
# This program takes chords from input and appends appropriate chords to it.

import random

# getNextChord chooses which chord should be next based on the number of
# chords remaining, the destination chord, and various weights. it makes
# use of the random() function when there are multiple options.
def getNextChord(chordsRemaining, destination, previousChord):
    if chordsRemaining == 1:      # if on last chord
        if destination == 1:      # if destination is tonic I
            return 5              # return dominant V
        elif destination == 5:    # if destination is dominant V
            num1 = random.random()
            if num1 < 0.5:        # return random predominant ii or IV
                return 4
            else:
                return 2
        elif destination == 4:    # if destination is IV
            return 1              # return V/IV, which is I
    elif chordsRemaining == 2:    # if on second to last chord
        if destination == 1:      # if destination is tonic I
            num1 = random.random()
            if num1 < 0.5:        # return random predominant ii or IV
                return 4
            else:
                return 2
        if destination == 5:
            num1 = random.random()
            # return random predominant ii/V or IV/V, which is vi or I
            # NOTE: need to consider previous chord to prevent repeating
            # chords. it's allowable, but weights will make it uncommon
            if previousChord == 1:
                if num1 < 0.1:    # only 10% chance to repeat
                    return 1
                else:
                    return 6
            elif previousChord == 6:
                if num1 < 0.1:    # only 10% chance to repeat
                    return 6
                else:
                    return 1
            else:
                if num1 < 0.5:    # otherwise normal 50% chance to return
                    return 6      # ii/V or IV/V (vi or I)
                else:
                    return 1
    else:
        num1 = random.random()    # return a random chord with specific weights
        # NOTE: these weights should be adjusted based on composer profile data
        # NOTE: this section should be rewritten with weights based on previous
        # chord. ie. if previousChord == 1, 44% chance to go up a fourth, but
        # if previousChord == 5, 62% chance to go up a fourth
        if num1 < 0.4:            # 40% chance to move up a fourth
            newChord = previousChord + 3
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        elif num1 < 0.6:          # 20% chance to move up a sixth
            newChord = previousChord + 5
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        elif num1 < 0.75:         # 15% chance to move up a fifth
            newChord = previousChord + 4
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        elif num1 < 0.85:         # 10% chance to move up a second
            newChord = previousChord + 1
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        elif num1 < 0.9:          # 5% chance to move up a third
            newChord = previousChord + 2
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        elif num1 < 0.95:         # 5% chance to move up a seventh
            newChord = previousChord + 6
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        else:                     # 5% chance to stay the same
            return previousChord



# main() function
def main():

    # get the rate of chord movement
    numMeasures = int(input("Enter number of measures: "))
    chordsPerMeasure = int(input("Enter the number of chords per measure: "))

    # get first chord or first few chords
    chordArray = [int(x) for x in input("Enter the array of chords: ").split()]
    # if no previous chords are provided, the first chord is defaulted to 1
    if chordArray == []:
        chordArray.append(1)
    print(chordArray)

    # get destination
    try:
        destination = int(input("Enter the destination chord: "))
    # if no destination is provided, the destination is defaulted to 1
    except:
        destination = 1

    #key = input("Enter the key: ")  # commented out until key library is used

    # calculate number of chords that need to be filled
    chordsNeeded = (numMeasures * chordsPerMeasure) - len(chordArray)

    # fill in the missing chords
    for i in range(0, chordsNeeded):
        # get the next chord. pass 3 params:
        # 1. the number of remaining chords, found by (chordsNeeded - i)
        # 2. the destination chord
        # 3. the previous chord, found by chordArray[-1]
        nextChord = getNextChord((chordsNeeded - i), destination, chordArray[-1])
        chordArray.append(nextChord)

    # add the destination chord to the end of the chordArray after filling it
    chordArray.append(destination)

    # display chordArray
    print(chordArray)


# call main()
main()
