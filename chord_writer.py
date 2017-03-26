# Chord Writer
# Jesse Lew
# This program takes chords from input and appends appropriate chords to it.

import random

# getNextChord chooses which chord should be next based on the number of
# chords remaining, the destination chord, and various weights. it makes
# use of the random() function when there are multiple options.
def getNextChord(chordsRemaining, destination):
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
            if num1 < 0.5:        # return random predominant ii/V or IV/V
                return 6          # which is vi or I
            else:
                return 1
    else:
        num1 = random.random()    # return a random chord with specific weights
        # consider using previous chord as param to heavily weigh moving up a fourth
        pass


# main() function
def main():
    # get user input for variables
    numMeasures = int(input("Enter number of measures: "))
    chordsPerMeasure = int(input("Enter the number of chords per measure: "))
    chordArray = [int(x) for x in input("Enter the array of chords: ").split()]
    destination = int(input("Enter the destination chord: "))
    #key = input("Enter the key: ")  # commented out until key library is used

    # calculate number of chords that need to be filled
    chordsNeeded = (numMeasures * chordsPerMeasure) - len(chordArray)

    # fill in the missing chords
    for i in range(0, chordsNeeded):
        # get the next chord. pass remaining chords and destination as params
        chordArray.append(getNextChord((chordsNeeded-i), destination))

    # add the destination chord to the end of the chordArray after filling it
    chordArray.append(destination)

    # display chordArray
    print(chordArray)


# call main()
main()
