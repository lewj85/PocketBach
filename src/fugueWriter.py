import makeMatrix as mm
import createLily as cl
import writeSubject as ws
import numpy as np
import random
import os

# https://en.wikipedia.org/wiki/Fugue#Musical_outline

# fugueWriter() function takes arguments from the recorded melody
def fugueWriter(key = 'C', major = 1, timesig = list([4, 4]), subjectMTX=None):

    # initialize variables
    chordArray = []
    chordsPerMeasure = 1
    beatsPerMeasure = 4
    measures = 32
    maxVoices = 3
    #print(subjectMTX)



    # create finalMTX
    finalMTX = mm.makeMatrix(maxVoices)
    # NOTE: newNote here is a 1-voice matrix. it will change below to contain additional voices
    newNote = mm.makeMatrix(3)  # now we can use finalMTX = np.concatenate([finalMTX, newNote],1) to add a new note


    #####################################################################
    # CREATE MEASURES 1-2 - Tonic (I)
    # NOTE: default harmonies pick from: I-I, I-IV, I-V
    # Soprano - rest
    # Alto - Subject
    # Bass - rest
    #####################################################################

    # NOTE: newNote here is a 1-voice matrix. it will change below to contain additional voices
    newNoteSub = mm.makeMatrix(1)  # now we can use subjectMTX = np.concatenate([subjectMTX, newNoteSub],1) to add a new note

    # if no user-generated melody is provided, make one up
    if subjectMTX is None:
        subjectMTX = mm.makeMatrix(1)
        #print(subjectMTX.shape)

        # pick from default harmonies: I-I, I-IV, I-V
        # NOTE: all move to a V chord in the 3rd measure
        firstChords = [[1,1,5],[1,4,5],[1,5,5]]
        chordChoices = random.choice(firstChords)
        print('chords for measures 1-3 are : '+str(chordChoices))

        # get notes and rhythms
        noteArray = ws.writeSubject(chordChoices)
        print(noteArray)

        # for easy reference:
        #   12 note data types: pitch, duration, direction, interval, chord root,
        #       7th chord, tonality, inversion, prev chord root, distance, beat, measure

        # add data to the matrix
        for i in range(len(noteArray)):
            if i > 0:  # NOTE: the first note is created and defaulted already
                subjectMTX = np.concatenate([subjectMTX, newNoteSub], 1)  # add a new note
            #print(subjectMTX.shape)
            subjectMTX[0][i][0] = noteArray[i][0]     # pitch
            subjectMTX[0][i][1] = noteArray[i][1]     # duration
            subjectMTX[0][i][4] = chordChoices[noteArray[i][2]-1]     # chordRoot
            if noteArray[i][2] == 1:
                subjectMTX[0][i][8] = 0
            else:
                subjectMTX[0][i][8] = chordChoices[noteArray[i][2]-2] # prevRoot
            # subjectMTX[0][i][10] = ?       # TODO: beat
            subjectMTX[0][i][11] = noteArray[i][2]    # measure


    # # if we got subjectMTX as a param but it has only 2 dimensions, give it a third
    # if len(subjectMTX.shape) == 2:
    #     subjectMTX = np.expand_dims(subjectMTX, 0)  # add the 3rd dimension as new 1st dimension

    #print('subject matrix is:')
    #print(subjectMTX)
    #print(subjectMTX.shape)

    # fill finalMTX with subjectMTX's values
    i = 1
    for j in range(subjectMTX.shape[1]):
        if j > 0:  # NOTE: the first note is created and defaulted already
            finalMTX = np.concatenate((finalMTX, newNote), 1)
        for k in [0,1,2,3,9,10]:  # NOTE: fill only pitch, duration, direction, and distance in alto
            finalMTX[i][j][k] = subjectMTX[0][j][k]
    for i in range(maxVoices):
        for j in range(subjectMTX.shape[1]):
            for k in [4,5,6,7,8,11]:  # fill the rest for all voices
                finalMTX[i][j][k] = subjectMTX[0][j][k]


    finalMTX[0][0][0] = 'r'  # pitch (rest)
    finalMTX[0][0][1] = '1'  # duration
    finalMTX[2][0][0] = 'r'  # pitch (rest)
    finalMTX[2][0][1] = '1'  # duration

    # free memory and let us re-use variable names
    del subjectMTX
    del noteArray

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
