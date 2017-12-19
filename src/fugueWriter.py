from lib import createLily as cl
from lib import createXML as cx
from lib import getNotes as gn
from lib import musicObjects as mo
#from lib import pitchToTonal as ptt
#from lib import defineChord as dc
from lib import distanceToPitch as dtp
#from lib import distanceToTonal as dtt
from lib import transposeCellDiatonically as tcd
#from lib import transposeDistance as td
import numpy as np
import random
#import os

# https://en.wikipedia.org/wiki/Fugue#Musical_outline

# TODO: go through all cell-creation for-loops and replace beats1234 with correct length of cells

# fugueWriter() function takes arguments from the recorded melody
def fugueWriter(subjectMTX = None, music = None):

    # # debugging
    # a = mo.Note('e', 43, 2, False, 1)
    # b = mo.Note('g', 46, 2, False, 1)
    # c = mo.Cell(mo.Chord(1), mo.Chord(5), [1, 2, 3, 4], [a, b], 39, 2)
    # #d = tcd.transposeCellDiatonically(c, mo.Chord(2), mo.Chord(6))
    # print(td.transposeDistance(a.distance, mo.Chord(1), mo.Chord(3), -1))
    # print(td.transposeDistance(b.distance, mo.Chord(1), mo.Chord(3), 1))
    # for x in d.notes:
    #     print(x.pitch, x.distance, d.destination)
    # print("end debugging")


    if music is None:
        music = mo.Music()

    # initialize variables
    measures = 32
    beats1234 = [1, 2, 3, 4]
    beats12 = [1, 2]
    beats34 = [3, 4]
    #maxVoices = 1
    #while maxVoices != 3 and maxVoices != 4:
    #    maxVoices = int(input("Enter 3 or 4 voices: "))
    maxVoices = 3
    if maxVoices == 3:
        bass = 0
        alto = 1
        soprano = 2
    else:
        bass = 0
        tenor = 1
        alto = 2
        soprano = 3


    # create finalMTX - a 2D array of 1D arrays (lists) of Cells - because each measure can hold 1-4 Cells
    finalMTX = np.empty((measures, maxVoices), dtype=object)


    #####################################################################
    # CREATE MEASURES 1-2 - Tonic (I)
    # NOTE: default harmonies pick from: I-I, I-IV, I-V
    # Soprano - rest
    # Alto - Subject
    # Bass - rest
    #####################################################################

    # if no user-generated melody is provided, make one up
    if subjectMTX is None:
        # NOTE: 2 measures, 1 voice
        subjectMTX = np.empty((2, 1), dtype=object)

        # pick from default harmonies: I-I, I-IV, I-V
        # NOTE: all move to a V chord in the 3rd measure
        firstChords = [[1,1,5],[1,4,5],[1,5,5]]
        destinationChords = random.choice(firstChords)
        print('chords for measures 1-3 are :', str(destinationChords))

        # 1st measure
        print("*******************MEASURE 1 (alto)**********************")
        notes, destinationAlto = gn.getNotes(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, None, None, alto)
        #print('notes:', notes)
        print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
        subjectMTX[0][0] = [mo.Cell(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, notes, destinationAlto, alto)]
        # 2nd measure
        print("*******************MEASURE 2 (alto)**********************")
        notes, destinationAlto = gn.getNotes(mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), beats1234, destinationAlto, None, alto)
        #print('notes:', notes)
        print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
        subjectMTX[1][0] = [mo.Cell(mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), beats1234, notes, destinationAlto, alto)]

        # free memory
        del firstChords, notes

    else:
        destinationAlto = subjectMTX[0][-1].destination

    # assign subjectMTX values to finalMTX
    # TODO: add for loop (subjectMTX.size[1]) to allow for subjects that are not exactly 2 measures long
    finalMTX[0][1] = subjectMTX[0][0]
    finalMTX[1][1] = subjectMTX[1][0]

    # free memory
    del subjectMTX

    # 1st and 2nd measure for other voices
    print("*******************MEASURE 1 (bass)**********************")
    finalMTX[0][0] = [mo.Cell(finalMTX[0][1][0].chord, finalMTX[0][1][0].nextChord, finalMTX[0][1][0].beats, [mo.Note('r', 88, 1, False, 1)], None, bass)]
    print("*******************MEASURE 2 (bass)**********************")
    finalMTX[1][0] = [mo.Cell(finalMTX[0][1][0].chord, finalMTX[0][1][0].nextChord, finalMTX[0][1][0].beats, [mo.Note('r', 88, 1, False, 1)], None, bass)]
    print("*******************MEASURE 1 (soprano)**********************")
    finalMTX[0][2] = [mo.Cell(finalMTX[0][1][0].chord, finalMTX[0][1][0].nextChord, finalMTX[0][1][0].beats, [mo.Note('r', 88, 1, False, 1)], None, soprano)]
    print("*******************MEASURE 2 (soprano)**********************")
    finalMTX[1][2] = [mo.Cell(finalMTX[0][1][0].chord, finalMTX[0][1][0].nextChord, finalMTX[0][1][0].beats, [mo.Note('r', 88, 1, False, 1)], None, soprano)]

    #####################################################################
    # CREATE MEASURES 3-4 - Dominant (V)
    # NOTE: default harmonies set to first 2 measure chords +4, so I-V becomes V-ii
    # Soprano - Answer
    # Alto - Counter-Subject 1
    # Bass - rest
    #####################################################################

    # create destination pitches
    # TODO: remove default V in measure 5 to create some randomness, such as ii-V, IV-V, vi-V
    # TODO: add for loop to allow for subjects longer than 2 measures
    destinationChords = [(finalMTX[0][1][0].chord.root + 3) % 7 + 1, (finalMTX[1][1][0].chord.root + 3) % 7 + 1, 5]
    print('chords for measures 3-5 are : ' + str(destinationChords))

    # Bass - resting
    print("*******************MEASURE 3 (bass)**********************")
    finalMTX[2][0] = [mo.Cell(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), finalMTX[0][1][0].beats, [mo.Note('r', 88, 1, False, 1)], None, bass)]
    print("*******************MEASURE 4 (bass)**********************")
    finalMTX[3][0] = [mo.Cell(mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), finalMTX[0][1][0].beats, [mo.Note('r', 88, 1, False, 1)], None, bass)]

    # Alto - Countersubject
    print("*******************MEASURE 3 (alto)**********************")
    notes, destinationAlto = gn.getNotes(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, destinationAlto, None, alto)
    #print('notes:', notes)
    print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
    finalMTX[2][1] = [mo.Cell(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, notes, destinationAlto, alto)]
    print("*******************MEASURE 4 (alto)**********************")
    notes, destinationAlto = gn.getNotes(mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), beats1234, destinationAlto, None, alto)
    #print('notes:', notes)
    print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
    finalMTX[3][1] = [mo.Cell(mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), beats1234, notes, destinationAlto, alto)]

    # Soprano - Answer
    # get pitches that fit the new harmony
    print("*******************MEASURE 3 (soprano)**********************")
    finalMTX[2][2] = []
    for cell in finalMTX[0][1]:
        # leaving direction and newDistance defaulted - letting it find the new distance
        nextCell = tcd.transposeCellDiatonically(cell, mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), 1)
        nextCell.voice = soprano
        finalMTX[2][2].append(nextCell)
    # get pitches that fit the new harmony
    print("*******************MEASURE 4 (soprano)**********************")
    finalMTX[3][2] = []
    for cell in finalMTX[1][1]:
        # leaving direction and newDistance defaulted - letting it find the new distance
        nextCell = tcd.transposeCellDiatonically(cell, mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), 1)
        nextCell.voice = soprano
        finalMTX[3][2].append(nextCell)

    # # debugging
    # for measure in range(measures):
    #     for voice in range(maxVoices):
    #         if finalMTX[measure][voice]:
    #             #print(finalMTX[voice][measure])
    #             for cell in finalMTX[measure][voice]:
    #                 #print(cell)
    #                 if cell:
    #                     print(measure, voice, cell.notes)


    #####################################################################
    # CREATE MEASURE 5
    # NOTE: default harmony set to V
    # Soprano - Codetta
    # Alto - Codetta
    # Bass - rest
    #####################################################################

    # TODO: change all mo.Chord(1)s in this section to match whatever the first chord in the matrix is - not always a I chord
    # Bass - resting
    print("*******************MEASURE 5 (bass)**********************")
    finalMTX[4][0] = [mo.Cell(mo.Chord(5), mo.Chord(1), finalMTX[0][1][0].beats, [mo.Note('r', 88, 1, False, 1)], None, bass)]

    # Alto - Codetta
    print("*******************MEASURE 5 (alto)**********************")
    notes, destinationAlto = gn.getNotes(mo.Chord(5), mo.Chord(1), beats1234, destinationAlto, None, alto)
    #print('notes:', notes)
    print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
    finalMTX[4][1] = [mo.Cell(mo.Chord(5), mo.Chord(1), beats1234, notes, destinationAlto, alto)]

    # Soprano - Codetta
    print("*******************MEASURE 5 (soprano)**********************")
    notes, destinationSoprano = gn.getNotes(mo.Chord(5), mo.Chord(1), beats1234, finalMTX[3][2][-1].destination, None, soprano)
    # print('notes:', notes)
    print('destinationSoprano:', destinationSoprano, dtp.distanceToPitch(destinationSoprano))
    finalMTX[4][2] = [mo.Cell(mo.Chord(5), mo.Chord(1), beats1234, notes, destinationSoprano, soprano)]


    #####################################################################
    # CREATE MEASURES 6-7 - Tonic (I)
    # Soprano - Counter-Subject 1
    # Alto - Counter-Subject 2
    # Bass - Subject
    #####################################################################

    # Bass - Subject
    print("*******************MEASURE 6 (bass)**********************")
    for cell in finalMTX[0][1]:
        # drop alto an octave for bass
        nextCell = tcd.transposeCellDiatonically(cell, cell.chord, cell.nextChord, -1)
        nextCell.voice = bass
        finalMTX[5][0].append(nextCell)
    print("*******************MEASURE 7 (bass)**********************")
    for cell in finalMTX[1][1]:
        # drop alto an octave for bass
        nextCell = tcd.transposeCellDiatonically(cell, cell.chord, cell.nextChord, -1)
        nextCell.voice = bass
        finalMTX[6][0].append(nextCell)

    # Alto - Counter-Subject 2
    print("*******************MEASURE 6 (soprano)**********************")
    for cell in range(len(finalMTX[2][1])):
        notes, destinationAlto = gn.getNotes(finalMTX[0][1][cell].chord, finalMTX[0][1][cell].nextChord, beats1234, destinationAlto, None, alto)
        # print('notes:', notes)
        print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
        finalMTX[5][1] = [mo.Cell(finalMTX[0][1][cell].chord, finalMTX[0][1][cell].nextChord, beats1234, notes, destinationAlto, alto)]
    print("*******************MEASURE 7 (alto)**********************")
    for cell in range(len(finalMTX[3][1])):
        notes, destinationAlto = gn.getNotes(finalMTX[1][1][cell].chord, finalMTX[1][1][cell].nextChord, beats1234, destinationAlto, None, alto)
        # print('notes:', notes)
        print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
        finalMTX[5][1] = [mo.Cell(finalMTX[1][1][cell].chord, finalMTX[1][1][cell].nextChord, beats1234, notes, destinationAlto, alto)]

    # Soprano - Counter-Subject 1
    print("*******************MEASURE 6 (soprano)**********************")
    for cell in range(len(finalMTX[2][1])):
        # raise alto for soprano
        nextCell = tcd.transposeCellDiatonically(finalMTX[2][1][cell], finalMTX[0][1][cell].chord, finalMTX[0][1][cell].nextChord, 1)
        nextCell.voice = soprano
        finalMTX[5][0].append(nextCell)
    print("*******************MEASURE 7 (soprano)**********************")
    for cell in range(len(finalMTX[3][1])):
        # raise alto for soprano
        nextCell = tcd.transposeCellDiatonically(finalMTX[3][1][cell], finalMTX[1][1][cell].chord, finalMTX[1][1][cell].nextChord, 1)
        nextCell.voice = soprano
        finalMTX[6][0].append(nextCell)


    #####################################################################
    # CREATE MEASURES 8-9 - Dominant (V)
    # Soprano - Counter-Subject 2
    # Alto - Answer
    # Bass - Counter-Subject 1
    #####################################################################

    # Bass - Counter-Subject 1
    print("*******************MEASURE 8 (bass)**********************")
    for cell in finalMTX[0][1]:
        # drop alto an octave for bass
        nextCell = tcd.transposeCellDiatonically(cell, cell.chord, cell.nextChord, -1)
        nextCell.voice = bass
        finalMTX[7][0].append(nextCell)
    print("*******************MEASURE 9 (bass)**********************")
    for cell in finalMTX[1][1]:
        # drop alto an octave for bass
        nextCell = tcd.transposeCellDiatonically(cell, cell.chord, cell.nextChord, -1)
        nextCell.voice = bass
        finalMTX[8][0].append(nextCell)

    # Alto - Answer
    print("*******************MEASURE 8 (soprano)**********************")
    for cell in range(len(finalMTX[2][1])):
        notes, destinationAlto = gn.getNotes(finalMTX[0][1][cell].chord, finalMTX[0][1][cell].nextChord, beats1234, destinationAlto, None, alto)
        # print('notes:', notes)
        print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
        finalMTX[7][1] = [mo.Cell(finalMTX[0][1][cell].chord, finalMTX[0][1][cell].nextChord, beats1234, notes, destinationAlto, alto)]
    print("*******************MEASURE 9 (alto)**********************")
    for cell in range(len(finalMTX[3][1])):
        notes, destinationAlto = gn.getNotes(finalMTX[1][1][cell].chord, finalMTX[1][1][cell].nextChord, beats1234, destinationAlto, None, alto)
        # print('notes:', notes)
        print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
        finalMTX[8][1] = [mo.Cell(finalMTX[1][1][cell].chord, finalMTX[1][1][cell].nextChord, beats1234, notes, destinationAlto, alto)]

    # Soprano - Counter-Subject 2
    print("*******************MEASURE 8 (soprano)**********************")
    for cell in range(len(finalMTX[2][1])):
        # raise alto for soprano
        nextCell = tcd.transposeCellDiatonically(finalMTX[2][1][cell], finalMTX[0][1][cell].chord, finalMTX[0][1][cell].nextChord, 1)
        nextCell.voice = soprano
        finalMTX[7][0].append(nextCell)
    print("*******************MEASURE 9 (soprano)**********************")
    for cell in range(len(finalMTX[3][1])):
        # raise alto for soprano
        nextCell = tcd.transposeCellDiatonically(finalMTX[3][1][cell], finalMTX[1][1][cell].chord, finalMTX[1][1][cell].nextChord, 1)
        nextCell.voice = soprano
        finalMTX[8][0].append(nextCell)

    #####################################################################
    # CREATE MEASURES 10-12
    # Soprano - Episode
    # Alto - Episode
    # Bass - Episode
    #####################################################################


    #####################################################################
    # CREATE MEASURES 13-14 - Relative minor/major (vi)
    # Soprano - Subject
    # Alto - Counter-Subject 1
    # Bass - rest
    #####################################################################



    #####################################################################
    # CREATE MEASURES 15-16 - Dominant of relative minor/major (V/vi)
    # Soprano - Counter-Subject 1
    # Alto - Counter-Subject 2
    # Bass - Answer
    #####################################################################



    #####################################################################
    # CREATE MEASURES 17-20 - vi, ii, V, I
    # Soprano - Episode
    # Alto - Episode, Answer false entry measure 19
    # Bass - Episode
    #####################################################################



    #####################################################################
    # CREATE MEASURES 21-22 - Subdominant (IV)
    # Soprano - rest
    # Alto - Subject
    # Bass - Counter-Subject 2
    #####################################################################



    #####################################################################
    # CREATE MEASURES 23-24
    # Soprano - Episode
    # Alto - Episode
    # Bass - Episode
    #####################################################################



    #####################################################################
    # CREATE MEASURES 25-26 - Tonic (I)
    # Soprano - Subject
    # Alto - Counter-Subject 2
    # Bass - Counter-Subject 1
    #####################################################################



    #####################################################################
    # CREATE MEASURES 27-28 - Tonic (I)
    # Soprano - Free counterpoint
    # Alto - Counter-subject 1
    # Bass - Subject
    #####################################################################



    #####################################################################
    # CREATE MEASURES 29-32 - IV ii, V7, I sus43, I
    # Soprano - Coda, Answer false entry measure 30, hold 5th or 3rd measures 31 and 32
    # Alto - Coda, sus43 measures 30-31 with anticipation of final chord at end of 31
    # Bass - pickup-iii, IV ii, V low-V, I, I and low-I
    #####################################################################



    #####################################################################
    # CREATE FILES: .ly, .mxl
    #####################################################################
    #cl.createLily(music.key, music.major, finalMTX, measures, maxVoices)  # commented out while fugueWriter is being written
    # cl.createLily(key, major, finalMTX, measures, maxVoices, 2)  # second species
    # TO DO: add other species
    # not using regex so don't need this anymore, keeping for legacy
    # copyfile('newScore.ly','newScore2.ly')


    # create the pdf score
    print("Creating .pdf file(s) with LilyPond...")
    filename = "Fugue.ly"
    #os.system(filename)  # commented out while fugueWriter is being written
    # time.sleep(3)

    # create the xml file
    print("Creating .xml file(s)...")
    filename = "Fugue.xml"
    cx.createXML(filename, music.key, music.major, music.timesig, finalMTX, measures, maxVoices)


# debugging
print('Fugue Writer - by Jesse Lew')
fugueWriter()
