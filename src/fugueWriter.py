from lib import createLily as cl
from lib import createXML as cx
from lib import getNotes as gn
from lib import musicObjects as mo
from lib import pitchToTonal as ptt
from lib import defineChord as dc
from lib import distanceToPitch as dtp
from lib import distanceToTonal as dtt
from lib import transposeDiatonically as td
import numpy as np
import random
#import os

# https://en.wikipedia.org/wiki/Fugue#Musical_outline

# fugueWriter() function takes arguments from the recorded melody
def fugueWriter(subjectMTX = None, music = None):

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
        print('chords for measures 1-3 are : '+str(destinationChords))

        # 1st measure
        print("*******************MEASURE 1 (alto)**********************")
        notes, destinationAlto = gn.getNotes(destinationChords[0], destinationChords[1], beats1234, None, None, alto)
        #print('notes:', notes)
        print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
        subjectMTX[0][0] = [mo.Cell(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, notes, destinationAlto, alto)]
        # 2nd measure
        print("*******************MEASURE 2 (alto)**********************")
        notes, destinationAlto = gn.getNotes(destinationChords[1], destinationChords[2], beats1234, destinationAlto, None, alto)
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
    # 3rd measure
    print("*******************MEASURE 3 (alto)**********************")
    notes, destinationAlto = gn.getNotes(destinationChords[0], destinationChords[1], beats1234, destinationAlto, None, alto)
    #print('notes:', notes)
    print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
    finalMTX[2][1] = [mo.Cell(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, notes, destinationAlto, alto)]
    # 4th measure
    print("*******************MEASURE 4 (alto)**********************")
    notes, destinationAlto = gn.getNotes(destinationChords[1], destinationChords[2], beats1234, destinationAlto, None, alto)
    #print('notes:', notes)
    print('destinationAlto:', destinationAlto, dtp.distanceToPitch(destinationAlto))
    finalMTX[3][1] = [mo.Cell(mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), beats1234, notes, destinationAlto, alto)]

    # Soprano - Answer
    # 3rd measure - get pitches that fit the new harmony
    print("*******************MEASURE 3 (soprano)**********************")
    finalMTX[2][2] = []
    for cell in finalMTX[0][1]:
        notes, destinationSoprano = td.transposeDiatonically(cell, mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]))
        finalMTX[2][2].append(mo.Cell(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, notes, destinationSoprano, soprano))
    # 4th measure - get pitches that fit the new harmony
    print("*******************MEASURE 4 (soprano)**********************")
    finalMTX[3][2] = []
    for cell in finalMTX[1][1]:
        notes, destinationSoprano = td.transposeDiatonically(cell, mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]))
        finalMTX[3][2].append(mo.Cell(mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), beats1234, notes, destinationSoprano, soprano))


    #print('finalMTX is:')
    #print(finalMTX)

    # debugging
    for measure in range(measures):
        for voice in range(maxVoices):
            if finalMTX[measure][voice]:
                #print(finalMTX[voice][measure])
                for cell in finalMTX[measure][voice]:
                    #print(cell)
                    if cell:
                        print(measure, voice, cell.notes)


    #####################################################################
    # CREATE MEASURE 5
    # NOTE: default harmony set to V
    # Soprano - Codetta
    # Alto - Codetta
    # Bass - rest
    #####################################################################



    #####################################################################
    # CREATE MEASURES 6-7 - Tonic (I)
    # Soprano - Counter-Subject 1
    # Alto - Counter-Subject 2
    # Bass - Subject
    #####################################################################



    #####################################################################
    # CREATE MEASURES 8-9 - Dominant (V)
    # Soprano - Counter-Subject 2
    # Alto - Answer
    # Bass - Counter-Subject 1
    #####################################################################


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
    filename = 'Fugue.ly'
    #os.system(filename)  # commented out while fugueWriter is being written
    # time.sleep(3)


# debugging
print('Fugue Writer - by Jesse Lew')
fugueWriter()
