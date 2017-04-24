import chord_writer
import random

def writeBassLine():

    pass

import chord_writer
#import chorale_writer

# main() function
def main():

    # initialize variables
    chordArray = []

    #####################################################################
    # CREATE MEASURES 1-4
    #####################################################################
    # start with a I chord
    chordArray.append(1)

    # create random destination for measure 4: I, IV, V, or vi
    num1 = random.random()
    if num1 < 0.25:
        destination = 1
    elif num1 < 0.5:
        destination = 4
    elif num1 < 0.75:
        destination = 5
    else:
        destination = 6

    # calculate number of chords that need to be filled
    chordsNeeded = 3

    # fill in the missing chords
    for i in range(0, chordsNeeded):
        # get the next chord. pass 3 params:
        # 1. the number of remaining chords, found by (chordsNeeded - i)
        # 2. the destination chord
        # 3. the previous chord, found by chordArray[-1]
        nextChord = chord_writer.getNextChord((chordsNeeded - i), destination, chordArray[-1])
        chordArray.append(nextChord)

    # display chordArray
    print(chordArray)

    # create a 2D note matrix
    # x dimensions:
    #   1. notes in current chord
    #   2. note data: pitch, duration, direction, interval, chord root, 7th chord,
    #        tonality, inversion, prev chord root, pickup, beat, measure
    # y dimension = chords
    noteMTX = [[0 for x in range(12)] for y in range(16)]

    # create a list of the note matrices
    #   broken down by chord
    noteMTXList = []

    # fill in the chords:
    for j in range(4):
        noteMTX[j][4] = chordArray[j]
        noteMTX[j][10] = 1      # hard-coded for chorale_writer
        noteMTX[j][11] = j+1    # hard-coded for chorale_writer
        print(noteMTX[j][:])
        noteMTXList.append(noteMTX[j][:])

    # display noteMTXList
    print(noteMTXList)


    #####################################################################
    # CREATE MEASURES 5-8
    #####################################################################
    # start with I, IV, V, or vi
    chordArray.append(chordArray[-1])  # to enter loop below (no python do-while)
    while chordArray[3] == chordArray[-1]:
        num1 = random.random()
        if num1 < 0.25:
            chordArray[4] = 1
        elif num1 < 0.5:
            chordArray[4] = 4
        elif num1 < 0.75:
            chordArray[4] = 5
        else:
            chordArray[4] = 6

    # set measure 8 destination to V, measure 9 will repeat first section
    destination = 5

    # get 3 more chords
    chordsNeeded = 2

    # fill in the missing chords
    for i in range(0, chordsNeeded):
        # get the next chord. pass 3 params:
        # 1. the number of remaining chords, found by (chordsNeeded - i)
        # 2. the destination chord
        # 3. the previous chord, found by chordArray[-1]
        nextChord = chord_writer.getNextChord((chordsNeeded - i), destination, chordArray[-1])
        chordArray.append(nextChord)

    # add the destination chord to the end of the chordArray after filling it
    # hard-coded to 1 to return
    chordArray.append(5)

    # display chordArray
    print(chordArray)

    # note data: pitch, duration, direction, interval, chord root, 7th chord,
    # tonality, inversion, prev chord root, pickup, beat, measure
    # print(noteMTX)

    # fill in the chords:
    for k in range(4,8):
        noteMTX[k][4] = chordArray[k]
        noteMTX[k][10] = 1
        noteMTX[k][11] = k + 1
        noteMTXList.append(noteMTX[k][:])

    # display noteMTXList
    print(noteMTXList)

    #####################################################################
    # CREATE MEASURES 9-12
    #####################################################################












    # fill in the bass
    # fill in the soprano
    # fill in the tenor/alto


# call main()
main()
