import getNextChord as gnc
import numToPitch as ntp
import orchestrate as orch
import createLily as cl
import speciesCP as scp
import random
import os
#import time
#from shutil import copyfile


# choraleWriter() function
def choraleWriter():

    # initialize variables
    key = 'C'
    major = 1
    chordArray = []
    chordsPerMeasure = 1
    beatsPerMeasure = 4
    measures = 16
    maxVoices = 3

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
    firstInversionLocations = []
    secondInversionLocations = []

    # fill in the missing chords
    for i in range(0, chordsNeeded):
        # get the next chord. pass 3 params:
        # 1. the number of remaining chords, found by (chordsNeeded - i)
        # 2. the destination chord
        # 3. the previous chord, found by chordArray[-1]
        nextChord = gnc.getNextChord((chordsNeeded - i), destination, chordArray[-1])
        chordArray.append(nextChord[0])
        # if nextChord[1] == 1:
        #     firstInversionLocations.append(i+2)
        #     firstInversionLocations.append(i+10)  # add same inversions to measures 9-12 (really 10-12)
        # elif nextChord[1] == 2:
        #     secondInversionLocations.append(i+2)
        #     secondInversionLocations.append(i+10)  # add same inversions to measures 9-12 (really 10-12)

    # display chordArray
    #print(chordArray)

    # create a 2D note matrix
    # x dimension = chords
    # y dimensions:
    #   1. notes in current chord
    #   2. 12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure
    noteMTX = [[0 for y in range(12)] for x in range(16)]  # hard-coded to 16 chords/measures

    # create a list of the note matrices
    #   broken down by chord
    #noteMTXList = []

    # fill in the chords:
    for j in range(4):
        noteMTX[j][4] = chordArray[j]                       # chord root
        if j > 0:
            noteMTX[j][8] = noteMTX[j-1][4]                 # prev chord root
        noteMTX[j][10] = int((j % chordsPerMeasure) * (beatsPerMeasure / chordsPerMeasure)) + 1      # beats
        noteMTX[j][11] = int(j / chordsPerMeasure) + 1      # measure number
        #noteMTXList.append(noteMTX[j][:])

    # display noteMTXList
    #print(noteMTXList)


    #####################################################################
    # CREATE MEASURES 5-8
    #####################################################################
    # start with I, IV, V, or vi
    # NOTE: we want a different chord than previous so...
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
        nextChord = gnc.getNextChord((chordsNeeded - i), destination, chordArray[-1])
        chordArray.append(nextChord[0])
        # if nextChord[1] == 1:
        #     firstInversionLocations.append(i+6)  # NOTE: not i+5 because we start with a non-inversion on measure 5
        # elif nextChord[1] == 2:
        #     secondInversionLocations.append(i+6)  # NOTE: not i+5 because we start with a non-inversion on measure 5

    # add the hard-coded V destination to bring us back to I in measure 9
    chordArray.append(5)

    # display chordArray
    #print(chordArray)

    # create a 2D note matrix
    # x dimension = chords
    # y dimensions:
    #   1. notes in current chord
    #   2. 12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure
    # fill in the chords:
    for j in range(4, 8):
        noteMTX[j][4] = chordArray[j]                       # chord root
        noteMTX[j][8] = noteMTX[j-1][4]                     # prev chord root
        noteMTX[j][10] = int((j % chordsPerMeasure) * (beatsPerMeasure / chordsPerMeasure)) + 1      # beats
        noteMTX[j][11] = int(j / chordsPerMeasure) + 1      # measure number
        #noteMTXList.append(noteMTX[j][:])

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
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure
    # fill in the chords:
    for j in range(8, 12):
        noteMTX[j][4] = chordArray[j]                       # chord root
        #noteMTX[j][7] = noteMTX[j-8][7]                     # inversion - this is done at the end
        noteMTX[j][8] = noteMTX[j - 1][4]                   # prev chord root
        noteMTX[j][10] = int((j % chordsPerMeasure) * (beatsPerMeasure / chordsPerMeasure)) + 1  # beats
        noteMTX[j][11] = int(j / chordsPerMeasure) + 1      # measure number
        #noteMTXList.append(noteMTX[j][:])

    # display noteMTXList
    #print(noteMTXList)


    #####################################################################
    # CREATE MEASURES 13-16
    #####################################################################
    # set destination to I
    destination = 1

    # 40% the time start with 1, other 60% can do anything
    num1 = random.random()
    if num1 < 0.4:
        chordArray.append(1)
        chordsNeeded = 2
    else:
        chordsNeeded = 3

    # fill in the missing chords
    for i in range(0, chordsNeeded):
        # get the next chord. pass 3 params:
        # 1. the number of remaining chords, found by (chordsNeeded - i)
        # 2. the destination chord
        # 3. the previous chord, found by chordArray[-1]
        nextChord = gnc.getNextChord((chordsNeeded - i), destination, chordArray[-1])
        chordArray.append(nextChord[0])
        # NOTE: NO INVERSIONS FOR LAST 4 MEASURES EXCEPT FOR POSSIBLE I64-V-I
        if len(chordArray) == 14 and nextChord[0] == 1 and nextChord[1] == 2:
            noteMTX[13][7] = 2

    # add the hard-coded I destination to end the chorale
    chordArray.append(1)

    # display chordArray, both in numbers and pitches
    #print(chordArray)
    chordArray2 = []
    for c in range(len(chordArray)):
        chordArray2.append(ntp.numToPitch(key, chordArray[c]))
    #print(chordArray2)


    # create a 2D note matrix
    # x dimension = chords
    # y dimensions:
    #   1. notes in current chord
    #   2. 12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure
    # fill in the chords:
    for j in range(12, 16):
        noteMTX[j][4] = chordArray[j]                       # chord root
        noteMTX[j][8] = noteMTX[j-1][4]                     # prev chord root
        noteMTX[j][10] = int((j % chordsPerMeasure) * (beatsPerMeasure / chordsPerMeasure)) + 1      # beats
        noteMTX[j][11] = int(j / chordsPerMeasure) + 1      # measure number
        #noteMTXList.append(noteMTX[j][:])


    #####################################################################
    # MAGIC
    #####################################################################

    # orchestrate the 3 voices
    finalMTX = orch.orchestrate(key, major, noteMTX, chordsPerMeasure, beatsPerMeasure, measures, maxVoices)
    # print(noteMTX)
    #print(finalMTX)

    # create .ly files for each species
    cl.createLily(key, major, finalMTX, measures, maxVoices, 1)  # first species
    #cl.createLily(key, major, finalMTX, measures, maxVoices, 2)  # second species
    # TO DO: add other species
    # not using regex so don't need this anymore, keeping for legacy
    #copyfile('newScore.ly','newScore2.ly')


    # create the pdf score
    print("Creating .pdf file(s) with LilyPond...")
    filename = 'ChoraleFirstSpecies.ly'
    os.system(filename)
    #time.sleep(3)


# call it
print('Chorale Writer - by Jesse Lew')
choraleWriter()
