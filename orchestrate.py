# orchestrate() fleshes out all voices for a given chord matrix

import numpy as np
import random
import getNextNote as gnn
import defineChord as dc
import pitchToNum as ptn

def orchestrate(key, major, noteMTX, chordsPerMeasure, beatsPerMeasure, measures, maxVoices):
    # 3 dimensional matrix finalMTX contains the fully orchestrated chorale
    # x = time (16 chords)
    # y = note (12 note and chord data)
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
    # z = voice (3 voices)
    #   0 = bass, 1 = alto/tenor, 2 = soprano
    finalMTX = np.array(range(16*12*3))
    finalMTX.fill(0)                # fill it with 0s
    finalMTX.shape = (16, 12, 3)    # define dimensions

    ################################################################
    # initialize the first chord
    ################################################################
    # bass
    finalMTX[0][0][0] = 1
    finalMTX[0][1][0] = chordsPerMeasure    # TO DO: fix this for non-4/4
    finalMTX[0][4][0] = 1
    finalMTX[0][10][0] = 1
    finalMTX[0][11][0] = 1
    # alto/tenor
    chordNotes = [1, 3, 5]  # create array for random to choose from below
    finalMTX[0][0][1] = chordNotes[random.randint(1, 3)-1]  # pick 1, 3, or 5
    finalMTX[0][1][1] = chordsPerMeasure    # TO DO: fix this for non-4/4
    finalMTX[0][4][1] = 1
    finalMTX[0][10][1] = 1
    finalMTX[0][11][1] = 1
    # soprano
    if finalMTX[0][0][1] == 1:      # if 2 roots, must pick 3rd
        finalMTX[0][0][2] = 3
    elif finalMTX[0][0][1] == 3:    # if root and 3rd, can pick 1 or 5
        chordNotes = [1, 5]
        finalMTX[0][0][2] = chordNotes[random.randint(1, 2)-1]
    else:                           # if root and 5th, must pick 3rd
        finalMTX[0][0][2] = 3
    finalMTX[0][1][2] = chordsPerMeasure    # TO DO: fix this for non-4/4
    finalMTX[0][4][2] = 1
    finalMTX[0][10][2] = 1
    finalMTX[0][11][2] = 1

    ################################################################
    # orchestrate the remaining chords
    ################################################################
    # NOTE: check for parallel 5ths, parallel octaves, tri-tones - redo a chord that fails check

    for i in range(1, measures):

        # TO DO: add while loop around each voice for validation until acceptable note is chosen
        #   if no acceptable note available, decrement i and rewrite previous choices

        # bass
        finalMTX[i][0][0] = gnn.getNextNote(key, major, noteMTX, finalMTX, i, measures, 0, maxVoices)
        # fill out inversion column for the other voices to follow rules
        chordArr = dc.defineChord(key, major, noteMTX[i][4], noteMTX[i][5], noteMTX[i][6])
        if finalMTX[i][0][0] == ptn.pitchToNum(chordArr[0]):
            finalMTX[i][7][0] = 0
        elif finalMTX[i][0][0] == ptn.pitchToNum(chordArr[1]):
            finalMTX[i][7][0] = 1
        elif finalMTX[i][0][0] == ptn.pitchToNum(chordArr[2]):
            finalMTX[i][7][0] = 2
        else:
            finalMTX[i][7][0] = 3  # 7th chords have 3rd inversion

        # soprano
        finalMTX[i][0][2] = gnn.getNextNote(key, major, noteMTX, finalMTX, i, measures, 2, maxVoices)  # soprano

        # alto/tenor:
        finalMTX[i][0][1] = gnn.getNextNote(key, major, noteMTX, finalMTX, i, measures, 1, maxVoices)  # alto/tenor

        # set all columns for i-th row of finalMTX using noteMTX
        #   12 note data types: pitch, duration, direction, interval, chord root,
        #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
        for voice in range(3):
            finalMTX[i][1][voice] = chordsPerMeasure    # duration

            # voice 0 interval
            if finalMTX[i][0][voice] == 1 or finalMTX[i][0][voice] == 2:    # interval, must check for 'wrapping'
                if finalMTX[i-1][0][voice] == 6 or finalMTX[i-1][0][voice] == 7:
                    temp = finalMTX[i][0][voice] - finalMTX[i-1][0][voice]
                    while temp < 0:
                        temp += 7
                    finalMTX[i][3][0] = temp
                else:
                    finalMTX[i][3][voice] = finalMTX[i][0][voice] - finalMTX[i-1][0][voice]
            elif finalMTX[i][0][voice] == 6 or finalMTX[i][0][voice] == 7:
                if finalMTX[i-1][0][voice] == 1 or finalMTX[i-1][0][voice] == 2:
                    temp = finalMTX[i][0][voice] - finalMTX[i-1][0][voice]
                    while temp > 0:
                        temp -= 7
                    finalMTX[i][3][voice] = temp
                else:
                    finalMTX[i][3][voice] = finalMTX[i][0][voice] - finalMTX[i-1][0][voice]
            else:
                finalMTX[i][3][voice] = finalMTX[i][0][voice] - finalMTX[i-1][0][voice]

            if finalMTX[i][3][voice] == 0:                              # direction
                finalMTX[i][2][voice] = 0
            elif finalMTX[i][3][voice] > 0:
                finalMTX[i][2][voice] = 1
            else:
                finalMTX[i][2][voice] = -1

            finalMTX[i][4][voice] = noteMTX[i][4]                       # chord root
            finalMTX[i][5][voice] = noteMTX[i][5]                       # 7th chord
            finalMTX[i][6][voice] = noteMTX[i][6]                       # tonality

            chordArr = dc.defineChord(key, major, noteMTX[i][4], noteMTX[i][5], noteMTX[i][6])  # inversion
            if finalMTX[i][0][voice] == ptn.pitchToNum(chordArr[0]):
                finalMTX[i][7][voice] = 0
            elif finalMTX[i][0][voice] == ptn.pitchToNum(chordArr[1]):
                finalMTX[i][7][voice] = 1
            elif finalMTX[i][0][voice] == ptn.pitchToNum(chordArr[2]):
                finalMTX[i][7][voice] = 2
            else:
                finalMTX[i][7][voice] = 3  # 7th chords have 3rd inversion

            finalMTX[i][8][voice] = noteMTX[i-1][4]                     # prev chord root
            finalMTX[i][9][voice] = 0                                   # pickup, none in bass
            finalMTX[i][10][voice] = noteMTX[i][10]                     # beat
            finalMTX[i][11][voice] = noteMTX[i][11]                     # measure


    #print(finalMTX)
    return finalMTX
