# orchestrate() fleshes out all voices for a given chord matrix

import numpy as np
import random
import getNextNote as gnn
import defineChord as dc
import pitchToNum as ptn

def orchestrate(key, major, noteMTX, chordsPerMeasure, beatsPerMeasure, measures):
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
    finalMTX[0][1][0] = beatsPerMeasure/chordsPerMeasure
    finalMTX[0][4][0] = 1
    finalMTX[0][10][0] = 1
    finalMTX[0][11][0] = 1
    # alto/tenor
    chordNotes = [1, 3, 5]  # create array for random to choose from below
    finalMTX[0][0][1] = chordNotes[random.randint(1, 3)-1]  # pick 1, 3, or 5
    finalMTX[0][1][1] = beatsPerMeasure/chordsPerMeasure
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
    finalMTX[0][1][2] = beatsPerMeasure/chordsPerMeasure
    finalMTX[0][4][2] = 1
    finalMTX[0][10][2] = 1
    finalMTX[0][11][2] = 1

    ################################################################
    # orchestrate the remaining chords
    ################################################################
    # NOTE: check for parallel 5ths, parallel octaves, tri-tones - redo a chord that fails check

    ################################################################
    # bass line first
    ################################################################
    voice = 0
    for i in range(1, measures):
        if i < measures-1:
            nextChord = noteMTX[i+1][4]
        else:
            nextChord = 1
        # TO DO: add while loop here for validation until acceptable note is chosen
        #   if no acceptable note available, decrement i and replace previous choices
        finalMTX[i][0][0] = gnn.getNextNote(key, major, noteMTX, finalMTX, i, measures, voice)

        # set all columns for i-th row of finalMTX using noteMTX
        #   12 note data types: pitch, duration, direction, interval, chord root,
        #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
        finalMTX[i][1][0] = beatsPerMeasure/chordsPerMeasure    # duration

        if finalMTX[i][0][0] == 1 or finalMTX[i][0][0] == 2:    # interval, must check for 'wrapping'
            if finalMTX[i-1][0][0] == 6 or finalMTX[i-1][0][0] == 7:
                temp = finalMTX[i][0][0] - finalMTX[i-1][0][0]
                while temp < 0:
                    temp += 7
                finalMTX[i][3][0] = temp
            else:
                finalMTX[i][3][0] = finalMTX[i][0][0] - finalMTX[i-1][0][0]
        elif finalMTX[i][0][0] == 6 or finalMTX[i][0][0] == 7:
            if finalMTX[i-1][0][0] == 1 or finalMTX[i-1][0][0] == 2:
                temp = finalMTX[i][0][0] - finalMTX[i-1][0][0]
                while temp > 0:
                    temp -= 7
                finalMTX[i][3][0] = temp
            else:
                finalMTX[i][3][0] = finalMTX[i][0][0] - finalMTX[i-1][0][0]
        else:
            finalMTX[i][3][0] = finalMTX[i][0][0] - finalMTX[i-1][0][0]

        if finalMTX[i][3][0] == 0:                              # direction
            finalMTX[i][2][0] = 0
        elif finalMTX[i][3][0] > 0:
            finalMTX[i][2][0] = 1
        else:
            finalMTX[i][2][0] = -1

        finalMTX[i][4][0] = noteMTX[i][4]                       # chord root
        finalMTX[i][5][0] = noteMTX[i][5]                       # 7th chord
        finalMTX[i][6][0] = noteMTX[i][6]                       # tonality

        if finalMTX[i][0][0] == noteMTX[i][4]:                  # inversion
            finalMTX[i][7][0] = 0
        else:
            chordArr = dc.defineChord(key, major, finalMTX[i][4][0], finalMTX[i][5][0], finalMTX[i][6][0], 0)
            if finalMTX[i][0][0] == ptn.pitchToNum(chordArr[1]):
                finalMTX[i][7][0] = 1
            elif finalMTX[i][0][0] == ptn.pitchToNum(chordArr[2]):
                finalMTX[i][7][0] = 2
            else:
                finalMTX[i][7][0] = 3  # 7th chords have 3rd inversion

        finalMTX[i][8][0] = noteMTX[i-1][4]                     # prev chord root
        finalMTX[i][9][0] = 0                                   # pickup, none in bass
        finalMTX[i][10][0] = noteMTX[i][10]                     # beat
        finalMTX[i][11][0] = noteMTX[i][11]                     # measure

        # NOTE: keep soprano and alto/tenor inside this loop so the program writes
        #   one measure at a time rather than the whole bass line followed by the
        #   whole soprano, etc
        ################################################################
        # soprano (melody) 2nd
        ################################################################
        # RULES:
        # can't be 3rd+3rd
        # can't be 5th+5th
        # no parallel 5ths or octaves
        voice = 2

        # TO DO: add while loop here for validation until acceptable note is chosen
        #   if no acceptable note available, decrement i and replace previous choices
        finalMTX[i][0][2] = gnn.getNextNote(key, major, noteMTX, finalMTX, i, measures, voice)
        # TO DO: fill rest of matrix for [][][2]

        ################################################################
        # alto/tenor last
        ################################################################
        # RULES:
        # if root+root, must be 3rd
        # if root+3rd, can be root or 5th
        # if root+5th, must be 3rd
        # if 3rd+root, can be root or 5th
        # can't be 3rd+3rd
        # if 3rd+5th, must be root
        # if 5th+root, must be 3rd
        # if 5th+3rd, must be root
        # can't be 5th+5th
        # no parallel 5ths or octaves
        voice = 1

        # TO DO: add while loop here for validation until acceptable note is chosen
        #   if no acceptable note available, decrement i and replace previous choices
        finalMTX[i][0][1] = gnn.getNextNote(key, major, noteMTX, finalMTX, i, measures, voice)
        # TO DO: fill rest of matrix for [][][1]


    #print(finalMTX)
    return finalMTX

