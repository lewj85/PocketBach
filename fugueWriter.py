import makeMatrix as mm
import getNextNote as gnn
import numToPitch as ntp
import orchestrate as orch
import createLily as cl
import getRhythm as gr
import numpy as np
import random
#import os

# https://en.wikipedia.org/wiki/Fugue#Musical_outline

# fugueWriter(noteMTX) function takes arguments from the recorded melody
def fugueWriter(key = 'C', major = 1, timesig = list([4, 4])):  # NOTE: took subjectMTX out of params
                                                                # TO DO: re-add subjectMTX

    # initialize variables
    chordArray = []
    chordsPerMeasure = 1
    beatsPerMeasure = 4
    measures = 32
    maxVoices = 3


    #####################################################################
    # CREATE MEASURES 1-2 - Tonic (I)
    # NOTE: default harmonies set to I-IV
    # Soprano - rest
    # Alto - Subject
    # Bass - rest
    #####################################################################

    # NOTE: newNote here is a 1-voice matrix. it will change below to contain additional voices
    newNote = mm.makeMatrix(1)  # now we can use np.concatenate([subjectMTX, newNote],1) to add a new note

    # if no user-generated melody is provided, make one up
    try:
        subjectMTX  # NOTE: took subjectMTX out of params temporarily
    except NameError:
        subjectMTX = mm.makeMatrix(1)

        # for easy reference:
        #   12 note data types: pitch, duration, direction, interval, chord root,
        #       7th chord, tonality, inversion, prev chord root, distance, beat, measure

        # get rhythms
        r1 = gr.getRhythm()  # get 1st measure
        r2 = gr.getRhythm()  # get 2nd measure

        # add them to the matrix, as well as note data
        # NOTE: we automatically write for a I-IV subject
        for i in range(len(r1)):
            if i > 0:
                np.concatenate([subjectMTX, newNote], 1)  # add a new note
            subjectMTX[0][i][1] = r1[i]     # duration
            subjectMTX[0][i][4] = 1         # chordRoot
            #subjectMTX[0][i][10] = ?        # TO DO: beat
            subjectMTX[0][i][11] = 1        # measure
        for i in range(len(r2)):
            np.concatenate([subjectMTX, newNote], 1)  # add a new note
            subjectMTX[0][i][1] = r1[i]     # duration
            subjectMTX[0][i][4] = 4         # chordRoot
            subjectMTX[0][i][8] = 1         # prevRoot
            # subjectMTX[0][i][10] = ?       # TO DO: beat
            subjectMTX[0][i][11] = 2        # measure

        # make up notes for them, in the alto
        pitches = gnn.getNextNoteArr()  # need params
        for i in range(subjectMTX.shape[1]):
            subjectMTX[0][i][0] = pitches[i]

    # if we got subjectMTX as a param but it has only 2 dimensions, give it a third
    if len(subjectMTX.shape) == 2:
        subjectMTX = np.expand_dims(subjectMTX, 0)  # add the 3rd dimension as new 1st dimension

    # create finalMTX
    finalMTX = mm.makeMatrix(maxVoices)

    print(type(subjectMTX))
    print(subjectMTX.shape)

    # fill finalMTX's Alto with subjectMTX's values
    for i in range(subjectMTX.shape[1]):
        for j in range(maxVoices):
            for k in range(12):
                if j != 1:
                    finalMTX[j][i][k] = subjectMTX[0][i][k]
                    if subjectMTX[0][i][11] == 2:
                        finalMTX[j][i][8] = 1       # prevRoot

    finalMTX[0][0][0] = 'r'  # pitch (rest)
    finalMTX[0][0][1] = '1'  # duration
    finalMTX[2][0][0] = 'r'  # pitch (rest)
    finalMTX[2][0][1] = '1'  # duration


    #####################################################################
    # CREATE MEASURES 3-4 - Dominant (V)
    # NOTE: default harmonies set to V-I
    # Soprano - Answer
    # Alto - Counter-Subject 1
    # Bass - rest
    #####################################################################

    newNote = mm.makeMatrix(maxVoices)  # now we can use np.concatenate([finalMTX, newNote],1) to add a new note

    # for easy reference:
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure

    # use same rhythms as subject for Answer
    notes = finalMTX.shape[1]
    for i in range(notes, notes*2):
        np.concatenate([finalMTX, newNote], 1)
        finalMTX[2][i][1] = subjectMTX[0][i][1]             # duration
        finalMTX[2][i][2] = subjectMTX[0][i][2]             # direction
        finalMTX[2][i][4] = 5                               # chordRoot
        finalMTX[2][i][8] = subjectMTX[0][i - notes][8]     # prevChordRoot
        finalMTX[2][i][10] = subjectMTX[0][i - notes][10]   # beat
        finalMTX[2][i][11] = subjectMTX[0][i - notes][11]   # measure

    # get pitches that fit the new harmony
    # NOTE: interval and distance(+4) will be the same

    print(finalMTX)


    #####################################################################
    # CREATE MEASURE 5
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


# call it
print('Fugue Writer - by Jesse Lew')
fugueWriter()
