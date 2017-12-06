# orchestrate() fleshes out all voices for a given chord matrix

from lib import makeMatrix as mm
from lib import getNextNote as gnn
from lib import pitchToTonal as ptt
from lib import tonalToPitch as ttp
import numpy as np
import random

def orchestrate(key, major, noteMTX, chordsPerMeasure, beatsPerMeasure, measures, maxVoices):
    # 3 dimensional matrix finalMTX contains the fully orchestrated chorale
    # x = time (16 chords)
    # y = note (12 note and chord data)
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure
    # z = voice (3 voices)
    #   0 = bass, 1 = alto/tenor, 2 = soprano

    # OLD CRAP I TRIED - keeping for legacy
    #finalMTX = [[['r', 'r', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16] * 3  # THIS DOESN'T WORK, USE NUMPY
    #finalMTX.fill(0)                # fill it with 0s, this will make everything an int though...
    #finalMTX.shape = (16, 12, 3)    # define dimensions

    # NOTE: THE NEW WAY OF DOING THIS USES LISTS TO ALLOW MULTIPLE TYPES INTO THE MATRIX.
    #       this 'removes' the note data dimension, though it can still be accessed with finalMTX[voice][note][data]
    finalMTX = mm.makeMatrix(maxVoices)
    newNote = finalMTX
    for i in range(measures - 1):
        finalMTX = np.concatenate((finalMTX, newNote), 1)  # add 15 blank notes, for 16 total
    #print(finalMTX.shape)

    ################################################################
    # initialize the first chord
    ################################################################
    # bass
    finalMTX[0][0][0] = '1'
    finalMTX[0][0][1] = str(chordsPerMeasure)    # TO DO: fix this for non-4/4
    finalMTX[0][0][4] = 1
    finalMTX[0][0][10] = 1
    finalMTX[0][0][11] = 1
    # alto/tenor
    chordNotes = [1, 3, 5]  # create array for random to choose from below
    finalMTX[1][0][0] = str(chordNotes[random.randint(1, 3)-1])  # pick 1, 3, or 5
    finalMTX[1][0][1] = str(chordsPerMeasure)    # TO DO: fix this for non-4/4
    finalMTX[1][0][4] = 1
    finalMTX[1][0][10] = 1
    finalMTX[1][0][11] = 1
    # soprano
    if finalMTX[1][0][0] == '1':      # if 2 roots, must pick 3rd
        finalMTX[2][0][0] = '3'
    elif finalMTX[1][0][0] == '3':    # if root and 3rd, can pick 1 or 5
        chordNotes = [1, 5]
        finalMTX[2][0][0] = str(chordNotes[random.randint(1, 2)-1])
    else:                           # if root and 5th, must pick 3rd
        finalMTX[2][0][0] = '3'
    finalMTX[2][0][1] = str(chordsPerMeasure)    # TO DO: fix this for non-4/4
    finalMTX[2][0][4] = 1
    finalMTX[2][0][10] = 1
    finalMTX[2][0][11] = 1

    ################################################################
    # orchestrate the remaining chords
    ################################################################
    # NOTE: check for parallel 5ths, parallel octaves, tri-tones - redo a chord that fails check
    attempts = 0
    totalFailures = 0

    # save for overwrite prevention
    i64 = (noteMTX[13][7] == 2)

    i = 1
    while i < measures:  # NOTE: this used to be a for loop from 1 to 'measures', but i changed to
                        # a while loop so we could add checks for tritones and reset 'i' to re-write
                        # any 'bad' measures

        # bass
        finalMTX[0][i][0] = str(gnn.getNextNote(key, major, noteMTX, finalMTX, i, measures, 0, maxVoices))

        # manually set last measure's bass to 1, apparently this wasn't a thing already...
        if i == measures - 1:
            finalMTX[0][i][0] = str(noteMTX[i][4])

        # fill out inversion column for the other voices to follow rules
        if int(finalMTX[0][i][0]) == noteMTX[i][4]:
            noteMTX[i][7] = 0
            finalMTX[0][i][7] = 0
        elif int(finalMTX[0][i][0]) == noteMTX[i][4]+2 or int(finalMTX[0][i][0]) == noteMTX[i][4]-5:  # wrapping 1-7
            #print('1st')
            noteMTX[i][7] = 1
            finalMTX[0][i][7] = 1
        elif int(finalMTX[0][i][0]) == noteMTX[i][4]+4 or int(finalMTX[0][i][0]) == noteMTX[i][4]-3:  # wrapping 1-7
            #print('2nd')
            noteMTX[i][7] = 2
            finalMTX[0][i][7] = 2
        else:
            #print('3rd')
            noteMTX[i][7] = 3
            finalMTX[0][i][7] = 3  # 7th chords have 3rd inversion

        # keeping all these old comments for legacy
        #chordArr = dc.defineChord(key, major, noteMTX[i][4], noteMTX[i][5], noteMTX[i][6], finalMTX[0][i][0])
        #print(chordArr)
        #print(str(int(finalMTX[0][i][0])))
        #print(ptt.pitchToTonal(key, chordArr[0]))
        #print(str(int(finalMTX[0][i][0])) == ptt.pitchToTonal(key, chordArr[0]))
        # FOUND A BUG: after converting to structs, need to remove the "b'value'" from first 2 columns...
        # TO DO: CHORALEWRITER'S GETNEXTCHORD IS CURRENTLY DECIDING WHETHER OR NOT TO ADD INVERSIONS, BUT
        #       GETNEXTNOTE ABOVE REALLY OUGHT TO BE THE THING DECIDING IF THERE ARE INVERSIONS (except for 164 cadences)
        #       so FIX IT - use the code below, not #finalMTX[0][i][7] = noteMTX[i][7] (except for 164 cadences...)
        # choraleWriter creates inversions now, so replace everything above with this?
        #finalMTX[0][i][7] = noteMTX[i][7]

        # manually reset 164 if it was overwritten
        if i == 13 and i64 == True:
            #print('overwriting')
            noteMTX[13][0] = str(noteMTX[0][4]+4)
            if int(noteMTX[13][0]) > 7:
                noteMTX[13][0] = str(int(noteMTX[13][0]) - 7)
            finalMTX[0][13][0] = noteMTX[13][0]
            noteMTX[13][7] = 2
            finalMTX[0][13][7] = 2

        # soprano
        finalMTX[2][i][0] = str(gnn.getNextNote(key, major, noteMTX, finalMTX, i, measures, 2, maxVoices))  # soprano

        # alto/tenor:
        finalMTX[1][i][0] = str(gnn.getNextNote(key, major, noteMTX, finalMTX, i, measures, 1, maxVoices))  # alto/tenor

        # check for tritones, parallel 5ths, and parallel octaves. if any are found, rewrite the whole measure
        if (int(finalMTX[0][i][0]) == 4 and int(finalMTX[0][i - 1][0]) == 7) or \
            (int(finalMTX[0][i][0]) == 7 and int(finalMTX[0][i - 1][0]) == 4) or \
            (int(finalMTX[1][i][0]) == 4 and int(finalMTX[1][i - 1][0]) == 7) or \
            (int(finalMTX[1][i][0]) == 7 and int(finalMTX[1][i - 1][0]) == 4) or \
            (int(finalMTX[2][i][0]) == 4 and int(finalMTX[2][i - 1][0]) == 7) or \
            (int(finalMTX[2][i][0]) == 7 and int(finalMTX[2][i - 1][0]) == 4) or \
            (int(finalMTX[0][i][0]) == (int(finalMTX[1][i][0]) + 3) % 7 + 1) and (
        int(finalMTX[0][i - 1][0]) == (int(finalMTX[1][i - 1][0]) + 3) % 7 + 1) or \
            (int(finalMTX[0][i][0]) == (int(finalMTX[2][i][0]) + 3) % 7 + 1) and (
        int(finalMTX[0][i - 1][0]) == (int(finalMTX[2][i - 1][0]) + 3) % 7 + 1) or \
            (int(finalMTX[1][i][0]) == (int(finalMTX[2][i][0]) + 3) % 7 + 1) and (
        int(finalMTX[1][i - 1][0]) == (int(finalMTX[2][i - 1][0]) + 3) % 7 + 1) or \
            (int(finalMTX[0][i][0]) == int(finalMTX[1][i][0]) and int(finalMTX[0][i - 1][0]) == int(finalMTX[1][i - 1][0])) or \
            (int(finalMTX[0][i][0]) == int(finalMTX[2][i][0]) and int(finalMTX[0][i - 1][0]) == int(finalMTX[2][i - 1][0])) or \
            (int(finalMTX[1][i][0]) == int(finalMTX[2][i][0]) and int(finalMTX[1][i - 1][0]) == int(finalMTX[2][i - 1][0])):

            # increment
            attempts += 1
            totalFailures += 1

            if totalFailures < 40:  # only try to go back if we're not caught in an endless loop
                i -= attempts  # rewrite the last few measures, the more failures, the farther back we go
            elif totalFailures >= 40:  # otherwise we probably ended up in an endless loop so try changing noteMTX
                print("Changing the matrix. Measure "+str(i + 1)+" is now a I chord.")
                noteMTX[i][4] = 1
                i -= 1  # reattempt current measure with new noteMTX
                totalFailures = 0

            if i < 0: # just in case we go back too far or get caught in a loop, start at measure 2
                i = 0
                attempts = 0
            #print("Attempt #" + str(attempts) + ". Rewriting measure " + str(i + 1) + ".")

        else:
            attempts = 0  # reset
            # set all columns for i-th row of finalMTX using noteMTX
            #   12 note data types: pitch, duration, direction, interval, chord root,
            #       7th chord, tonality, inversion, prev chord root, distance, beat, measure
            for voice in range(3):
                finalMTX[voice][i][1] = chordsPerMeasure    # duration

                # voice 0 interval
                if finalMTX[voice][i][0] == '1' or finalMTX[voice][i][0] == '2':    # interval, must check for 'wrapping'
                    if finalMTX[voice][i-1][0] == '6' or finalMTX[voice][i-1][0] == '7':
                        temp = int(finalMTX[voice][i][0]) - int(finalMTX[voice][i-1][0])
                        if temp < 0:
                            temp += 7
                        finalMTX[0][i][3] = temp
                    else:
                        finalMTX[voice][i][3] = finalMTX[voice][i][0] - finalMTX[voice][i-1][0]
                elif finalMTX[voice][i][0] == '6' or finalMTX[voice][i][0] == '7':
                    if finalMTX[voice][i-1][0] == '1' or finalMTX[voice][i-1][0] == '2':
                        temp = int(finalMTX[voice][i][0]) - int(finalMTX[voice][i-1][0])
                        if temp > 0:
                            temp -= 7
                        finalMTX[voice][i][3] = temp
                    else:
                        finalMTX[voice][i][3] = int(finalMTX[voice][i][0]) - int(finalMTX[voice][i-1][0])
                else:
                    finalMTX[voice][i][3] = int(finalMTX[voice][i][0]) - int(finalMTX[voice][i-1][0])

                if finalMTX[voice][i][3] == 0:                              # direction
                    finalMTX[voice][i][2] = 0
                elif finalMTX[voice][i][3] > 0:
                    finalMTX[voice][i][2] = 1
                else:
                    finalMTX[voice][i][2] = -1

                finalMTX[voice][i][4] = noteMTX[i][4]                       # chord root
                finalMTX[voice][i][5] = noteMTX[i][5]                       # 7th chord
                finalMTX[voice][i][6] = noteMTX[i][6]                       # tonality

                # chordArr = dc.defineChord(key, major, noteMTX[i][4], noteMTX[i][5], noteMTX[i][6], noteMTX[i][7])  # inversion
                # if str(int(finalMTX[voice][i][0])) == ptt.pitchToTonal(key, chordArr[0]):
                #     finalMTX[voice][i][7] = 0
                # elif str(int(finalMTX[voice][i][0])) == ptt.pitchToTonal(key, chordArr[1]):
                #     finalMTX[voice][i][7] = 1
                # elif str(int(finalMTX[voice][i][0])) == ptt.pitchToTonal(key, chordArr[2]):
                #     finalMTX[voice][i][7] = 2
                # else:
                #     finalMTX[voice][i][7] = 3  # 7th chords have 3rd inversion
                # replace everything above with this
                finalMTX[voice][i][7] = noteMTX[i][7]                       # inversion

                finalMTX[voice][i][8] = noteMTX[i-1][4]                     # prev chord root
                finalMTX[voice][i][9] = 0                                   # distance, none in bass
                finalMTX[voice][i][10] = noteMTX[i][10]                     # beat
                finalMTX[voice][i][11] = noteMTX[i][11]                     # measure

        i += 1  # move on to the next measure

    #print(finalMTX)
    return finalMTX
