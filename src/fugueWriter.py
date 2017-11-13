#from lib import makeMatrix as mm
#from lib import createLily as cl
from lib import getNotes as gn
#from lib import writeCountersubject as wc
from lib import musicObjects as mo
from lib import distanceToTonal as dtt
import numpy as np
import random
import os

# https://en.wikipedia.org/wiki/Fugue#Musical_outline

# fugueWriter() function takes arguments from the recorded melody
def fugueWriter(subjectMTX=None, key = 'C', major = 1, timesig = None):

    if not timesig:
        timesig = [4,4]

    # initialize variables
    chordArray = []
    chordsPerMeasure = 1
    beatsPerMeasure = 4
    measures = 32
    maxVoices = 3
    #print(subjectMTX)


    # DEBUGGING
    # newMusic = mo.Music()
    # newChord = mo.Chord(newMusic.key, newMusic.major, newMusic.timesig, 1)
    # newNote1 = mo.Note(newChord.key, newChord.major, newChord.timesig, newChord.root, newChord.tonality, newChord.seventh, newChord.inversion, newChord.secondary, newChord.secondaryRoot, 'f', 55, '8', 0)
    # newNote2 = mo.Note(newChord.key, newChord.major, newChord.timesig, newChord.root, newChord.tonality, newChord.seventh, newChord.inversion, newChord.secondary, newChord.secondaryRoot, 'g', 56, '8', 0)
    # newCell = mo.Cell(newChord,[1],[newNote1,newNote2])
    #
    # # create finalMTX - a 2D array of 2D arrays (lists) of Cells - because each measure can hold 1-4 Cells
    # finalMTX = np.empty((maxVoices, measures), dtype=object)
    #
    # finalMTX[0][0] = [newCell]
    # finalMTX[0][0].append(newCell)
    #
    # print(finalMTX)
    # print(finalMTX[0][0][0].notes[0].pitch)
    # print(finalMTX[0][0][0].notes[1].pitch)


    # create finalMTX - a 2D array of 2D arrays (lists) of Cells - because each measure can hold 1-4 Cells
    finalMTX = np.empty((maxVoices, measures), dtype=object)


    #####################################################################
    # CREATE MEASURES 1-2 - Tonic (I)
    # NOTE: default harmonies pick from: I-I, I-IV, I-V
    # Soprano - rest
    # Alto - Subject
    # Bass - rest
    #####################################################################

    # if no user-generated melody is provided, make one up
    if subjectMTX is None:
        # NOTE: 2 measures
        subjectMTX = np.empty((maxVoices, 2), dtype=object)

        # pick from default harmonies: I-I, I-IV, I-V
        # NOTE: all move to a V chord in the 3rd measure
        firstChords = [[1,1,5],[1,4,5],[1,5,5]]
        chordChoices = random.choice(firstChords)
        print('chords for measures 1-3 are : '+str(chordChoices))

        #debugging
        #chordChoices = [1,2,3,4,5]


        # get notes, rhythms, and destination
        notes, destination = gn.getNotes(chordChoices[0], chordChoices[1], [1,2,3,4])
        newCell = mo.Cell(newChord, notes)
        finalMTX[0][0] = []





    # free memory and let us re-use variable names
    del subjectMTX
    #del noteArray

    #####################################################################
    # CREATE MEASURES 3-4 - Dominant (V)
    # NOTE: default harmonies set to V-I
    # Soprano - Answer
    # Alto - Counter-Subject 1
    # Bass - rest
    #####################################################################

    newNote = mm.makeMatrix(maxVoices)  # now we can use np.concatenate([finalMTX, newNote],1) to add a new note

    # use noteArray above to create a countersubject - TODO: create noteArray if a subjectMTX was passed above
    #noteArray2 = wc.writeCountersubject([finalMTX[1][0][4]+4, finalMTX[1][-2][4]+4], noteArray)  # NOTE: -2 because -1 has 3rd measure whole note



    # for easy reference:
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure

    # use same rhythms as subject for Answer
    # notes = finalMTX.shape[1]
    # for i in range(notes, notes*2):
    #     np.concatenate([finalMTX, newNote], 1)
    #     finalMTX[2][i][1] = subjectMTX[0][i][1]             # duration
    #     finalMTX[2][i][2] = subjectMTX[0][i][2]             # direction
    #     finalMTX[2][i][4] = 5                               # chordRoot
    #     finalMTX[2][i][8] = subjectMTX[0][i - notes][8]     # prevChordRoot
    #     finalMTX[2][i][10] = subjectMTX[0][i - notes][10]   # beat
    #     finalMTX[2][i][11] = subjectMTX[0][i - notes][11]   # measure

    # get pitches that fit the new harmony
    # NOTE: interval and distance(+4) will be the same

    print('finalMTX is:')
    print(finalMTX)


    #####################################################################
    # CREATE MEASURE 5
    # NOTE: default harmonies set to ii-V, each with a half-note
    # Soprano - Codetta
    # Alto - Codetta
    # Bass - rest
    #####################################################################

    # for easy reference:
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure


    #####################################################################
    # CREATE MEASURES 6-7 - Tonic (I)
    # Soprano - Counter-Subject 1
    # Alto - Counter-Subject 2
    # Bass - Subject
    #####################################################################

    # for easy reference:
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure


    #####################################################################
    # CREATE MEASURES 8-9 - Dominant (V)
    # Soprano - Counter-Subject 2
    # Alto - Answer
    # Bass - Counter-Subject 1
    #####################################################################

    # for easy reference:
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure

    #####################################################################
    # CREATE MEASURES 10-12
    # Soprano - Episode
    # Alto - Episode
    # Bass - Episode
    #####################################################################

    # for easy reference:
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure

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
    cl.createLily(key, major, finalMTX, measures, maxVoices)
    # cl.createLily(key, major, finalMTX, measures, maxVoices, 2)  # second species
    # TO DO: add other species
    # not using regex so don't need this anymore, keeping for legacy
    # copyfile('newScore.ly','newScore2.ly')


    # create the pdf score
    print("Creating .pdf file(s) with LilyPond...")
    filename = 'Fugue.ly'
    os.system(filename)
    # time.sleep(3)


# debugging
print('Fugue Writer - by Jesse Lew')
fugueWriter()
