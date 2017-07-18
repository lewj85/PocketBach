import chord_writer
import random


# main() function
def main():

    # initialize variables
    chordArray = []
    chordsPerMeasure = 1
    beatsPerMeasure = 4


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
    #print(chordArray)

    # create a 2D note matrix
    # x dimension = chords
    # y dimensions:
    #   1. notes in current chord
    #   2. 12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
    noteMTX = [[0 for y in range(12)] for x in range(16)]  # hard-coded to 16 chords/measures

    # create a list of the note matrices
    #   broken down by chord
    noteMTXList = []

    # fill in the chords:
    for j in range(4):
        noteMTX[j][4] = chordArray[j]                       # chord root
        if j > 0:
            noteMTX[j][8] = noteMTX[j-1][4]                 # prev chord root
        noteMTX[j][10] = int((j % chordsPerMeasure) * (beatsPerMeasure / chordsPerMeasure)) + 1      # beats
        noteMTX[j][11] = int(j / chordsPerMeasure) + 1      # measure number
        noteMTXList.append(noteMTX[j][:])

    # display noteMTXList
    #print(noteMTXList)


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

    # get 2 more chords (V is set manually afterward)
    chordsNeeded = 2

    # fill in the missing chords
    for i in range(0, chordsNeeded):
        # get the next chord. pass 3 params:
        # 1. the number of remaining chords, found by (chordsNeeded - i)
        # 2. the destination chord
        # 3. the previous chord, found by chordArray[-1]
        nextChord = chord_writer.getNextChord((chordsNeeded - i), destination, chordArray[-1])
        chordArray.append(nextChord)

    # add the hard-coded V destination to bring us back to I in measure 9
    chordArray.append(5)

    # display chordArray
    #print(chordArray)

    # create a 2D note matrix
    # x dimension = chords
    # y dimensions:
    #   1. notes in current chord
    #   2. 12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
    # fill in the chords:
    for j in range(4, 8):
        noteMTX[j][4] = chordArray[j]                       # chord root
        noteMTX[j][8] = noteMTX[j-1][4]                     # prev chord root
        noteMTX[j][10] = int((j % chordsPerMeasure) * (beatsPerMeasure / chordsPerMeasure)) + 1      # beats
        noteMTX[j][11] = int(j / chordsPerMeasure) + 1      # measure number
        noteMTXList.append(noteMTX[j][:])

    # display noteMTXList
    #print(noteMTXList)


    #####################################################################
    # CREATE MEASURES 9-12
    #####################################################################
    # repeat first 4 measures
    for m in range(4):
        chordArray.append(chordArray[m])

    # display chordArray
    #print(chordArray)

    # create a 2D note matrix
    # x dimension = chords
    # y dimensions:
    #   1. notes in current chord
    #   2. 12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
    # fill in the chords:
    for j in range(8, 12):
        noteMTX[j][4] = chordArray[j]                       # chord root
        noteMTX[j][8] = noteMTX[j - 1][4]                   # prev chord root
        noteMTX[j][10] = int((j % chordsPerMeasure) * (beatsPerMeasure / chordsPerMeasure)) + 1  # beats
        noteMTX[j][11] = int(j / chordsPerMeasure) + 1      # measure number
        noteMTXList.append(noteMTX[j][:])

    # display noteMTXList
    #print(noteMTXList)


    #####################################################################
    # CREATE MEASURES 13-16
    #####################################################################
    # set destination to I
    destination = 1

    # for consistency, repeat chord from measure 9
    chordArray.append(chordArray[8])

    # get 2 more chords (V is set manually afterward)
    chordsNeeded = 2

    # fill in the missing chords
    for i in range(0, chordsNeeded):
        # get the next chord. pass 3 params:
        # 1. the number of remaining chords, found by (chordsNeeded - i)
        # 2. the destination chord
        # 3. the previous chord, found by chordArray[-1]
        nextChord = chord_writer.getNextChord((chordsNeeded - i), destination, chordArray[-1])
        chordArray.append(nextChord)

    # add the hard-coded I destination to end the chorale
    chordArray.append(1)

    # display chordArray
    print(chordArray)

    # create a 2D note matrix
    # x dimension = chords
    # y dimensions:
    #   1. notes in current chord
    #   2. 12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
    # fill in the chords:
    for j in range(12, 16):
        noteMTX[j][4] = chordArray[j]                       # chord root
        noteMTX[j][8] = noteMTX[j-1][4]                     # prev chord root
        noteMTX[j][10] = int((j % chordsPerMeasure) * (beatsPerMeasure / chordsPerMeasure)) + 1      # beats
        noteMTX[j][11] = int(j / chordsPerMeasure) + 1      # measure number
        noteMTXList.append(noteMTX[j][:])

    # display noteMTXList
    print(noteMTXList)




    # fill in the bass
    #getBass(noteMTXList)

    # fill in the soprano
    #getSoprano(noteMTXList)

    # fill in the tenor/alto
    #getTenor(noteMTXList)


# call main()
main()
