"""orchestrate() fleshes out all voices for a given chord matrix"""

from lib import musicObjects as mo
from lib import makeMatrix as mm
from lib import getNextNote as gnn
from lib import pitchToTonal as ptt
from lib import pitchToDistance as ptd
from lib import tonalToDistance as ttd
from lib import tonalToPitch as ttp
import numpy as np
import random

def orchestrate(music, chordArray, maxVoices, species = 1):

    if maxVoices == 3:
        bass = 0
        tenor = 1
        soprano = 2
    else:
        bass = 0
        tenor = 1
        soprano = 2
        alto = 3  # keeping as 3 instead of swapping with soprano - easier to add into current code

    beats1234 = [1,2,3,4]
    beats12 = [1,2]
    beats34 = [3,4]

    measures = len(chordArray)
    # create finalMTX - a 2D array of 1D arrays (lists) of Cells - because each measure can hold 1-4 Cells
    finalMTX = np.empty((measures, maxVoices), dtype=object)

    ################################################################
    # orchestrate the first chord
    ################################################################
    # bass
    finalMTX[0][bass] = []
    for chord in range(len(chordArray[0])):
        # if 1 chord in the measure
        if len(chordArray[0]) == 1:
            finalMTX[0][bass].append(mo.Cell(chordArray[0][0], chordArray[1][0], beats1234, [mo.Note(ttp.tonalToPitch(chordArray[0][0].root), ttd.tonalToDistance(chordArray[0][0].root), 1, False, chordArray[0][0].root)], None, bass))
    # TODO: add other species

    chordNotes = [1, 3, 5]  # create array for random to choose from below

    # alto/tenor
    finalMTX[0][tenor] = []
    for chord in range(len(chordArray[0])):
        # if 1 chord in the measure
        if len(chordArray[0]) == 1:
            pitch = ttp.tonalToPitch(random.choice(chordNotes))  # pick 1, 3, or 5
            finalMTX[0][tenor].append(mo.Cell(chordArray[0][0], chordArray[1][0], beats1234, [mo.Note(pitch, ptd.pitchToDistance(pitch, tenor), 1, False, chordArray[0][0].root)], None, tenor))
    # TODO: add other species

    # soprano
    finalMTX[0][soprano] = []
    if finalMTX[0][tenor][0].notes[0].pitch == music.key:  # if 2 roots, must pick 3rd
        pitch = finalMTX[0][tenor][0].chord.getPitches()[1] # 3rd of chord
    elif finalMTX[0][tenor][0].notes[0].pitch == mo.Chord(ptt.pitchToTonal(music.key)).getPitches()[1]:  # if root and 3rd, can pick 1 or 5
        chordNotes = [1, 5]
        pitch = ttp.tonalToPitch(random.choice(chordNotes))
    else:  # if root and 5th, must pick 3rd
        pitch = finalMTX[0][tenor][0].chord.getPitches()[1]  # 3rd of chord
    finalMTX[0][soprano].append(mo.Cell(chordArray[0][0], chordArray[1][0], beats1234, [mo.Note(pitch, ptd.pitchToDistance(pitch, soprano), 1, False, chordArray[0][0].root)], None, soprano))
    # TODO: add other species


    ################################################################
    # orchestrate the remaining chords
    ################################################################
    # NOTE: check for parallel 5ths, parallel octaves, tri-tones - redo a chord that fails check
    attempts = 0
    totalFailures = 0

    # save for overwrite prevention
    i64 = (chordArray[13][0].root == 1) # .inversion == 2

    i = 1
    while i < measures:
        """NOTE: this used to be a for loop from 1 to 'measures', but i changed to a while loop so we 
        could add checks for tritones and reset 'i' to re-write any 'bad' measures"""

        # bass
        notes = []
        for s in range(species):
            # TODO: CONTINUE FROM HERE *******make getNextNote() return Note classes instead of ints*********
            notes.append(gnn.getNextNote(music, chordArray, finalMTX, i, measures, bass, maxVoices))
        finalMTX[i][0][0] = mo.Cell(blah)

        # manually set last measure's bass to 1
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


        # manually reset 164 if it was overwritten
        if i == 13 and i64:
            #print('overwriting')
            noteMTX[13][0] = str(noteMTX[0][4]+4)
            if int(noteMTX[13][0]) > 7:
                noteMTX[13][0] = str(int(noteMTX[13][0]) - 7)
            finalMTX[0][13][0] = noteMTX[13][0]
            for j in range(maxVoices):
                finalMTX[i][j][0].chord.inversion = 2

        # soprano
        finalMTX[2][i][0] = str(gnn.getNextNote(music, noteMTX, finalMTX, i, measures, 2, maxVoices))  # soprano

        # alto/tenor:
        finalMTX[1][i][0] = str(gnn.getNextNote(music, noteMTX, finalMTX, i, measures, 1, maxVoices))  # alto/tenor

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
                finalMTX[voice][i][7] = noteMTX[i][7]                       # inversion
                finalMTX[voice][i][8] = noteMTX[i-1][4]                     # prev chord root
                finalMTX[voice][i][9] = 0                                   # distance, none in bass
                finalMTX[voice][i][10] = noteMTX[i][10]                     # beat
                finalMTX[voice][i][11] = noteMTX[i][11]                     # measure

        i += 1  # move on to the next measure

    #print(finalMTX)
    return finalMTX
