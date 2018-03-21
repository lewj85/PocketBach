from lib import musicObjects as mo
from lib import getNextChord as gnc
from lib import tonalToPitch as ttp
from lib import orchestrate as orch
from lib import createLily as cl
from lib import speciesCP as scp
import numpy as np
import random
import os
#import time
#from shutil import copyfile


# choraleWriter() function
def choraleWriter(music = None):

    # initialize variables
    if music is None:
        music = mo.Music()

    chordArray = []
    species = 1
    measures = 16
    # maxVoices = -1
    # while maxVoices != 3 or maxVoices != 4:
    #    maxVoices = int(input("Enter 3 or 4 voices: "))
    maxVoices = 3

    # TODO: change chordArray to hold [[1], [4]...] rather than [1,4...] for other species

    #####################################################################
    # CREATE MEASURES 1-4
    #####################################################################
    print('writing measures 1-4')
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
        nextChord = gnc.getNextChord((chordsNeeded - i), destination, chordArray)
        chordArray.append(nextChord[0])


    #####################################################################
    # CREATE MEASURES 5-8
    #####################################################################
    print('writing measures 5-8')
    #print(chordArray)
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
        nextChord = gnc.getNextChord((chordsNeeded - i), destination, chordArray)
        chordArray.append(nextChord[0])

    # add the hard-coded V destination to bring us back to I in measure 9
    chordArray.append(5)


    #####################################################################
    # CREATE MEASURES 9-12
    #####################################################################
    print('writing measures 9-12')
    #print(chordArray)
    # repeat first 4 measures
    for m in range(4):
        chordArray.append(chordArray[m])


    #####################################################################
    # CREATE MEASURES 13-16
    #####################################################################
    print('writing measures 13-16')
    #print(chordArray)
    # set destination to I
    destination = 1

    # 40% the time start with 1, other 60% can do anything
    num1 = random.random()
    if num1 < 0.4:
        chordArray.append(1)
        chordsNeeded = 1
    else:
        chordsNeeded = 2

    # fill in the missing chords
    for i in range(0, chordsNeeded):
        # get the next chord. pass 3 params:
        # 1. the number of remaining chords, found by (chordsNeeded - i)
        # 2. the destination chord
        # 3. the previous chord, found by chordArray[-1]
        nextChord = gnc.getNextChord((chordsNeeded - i), destination, chordArray)
        chordArray.append(nextChord[0])
        # NOTE: NO INVERSIONS FOR LAST 4 MEASURES EXCEPT FOR POSSIBLE I64-V-I
        # if len(chordArray) == 14 and nextChord[0] == 1 and nextChord[1] == 2:
        #     noteMTX[13][7] = 2

    # add the hard-coded V-I cadence to end the chorale
    chordArray.append(5)
    chordArray.append(1)

    # display chordArray, both in numbers and pitches
    chordArray2 = []
    for c in range(len(chordArray)):
        # TODO: remove the [] around the chords, build species properly
        chordArray2.append([mo.Chord(chordArray[c])])

    print(chordArray)

    #####################################################################
    # MAGIC
    #####################################################################

    # orchestrate the voices
    finalMTX = orch.orchestrate(music, chordArray2, maxVoices)
    # print(noteMTX)
    #print(finalMTX)

    # create .ly files for each species
    cl.createLily(music, finalMTX, measures, maxVoices, 1)  # first species
    #cl.createLily(music, finalMTX, measures, maxVoices, 2)  # second species
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
