"""speciesCP's functions create new scores for the 5 types (species) of counterpoint"""

"""for second- through fifth-species, we have 3 options:
1) alter finalMTX's shape to XXx12x3 (after it finishes writing it as 16x12x3)
   then send the new matrix to matrixToLily (matrixToLily already uses a while
   loop exactly for this)
   NOTE: make sure to add measure numbers (last column) to the new notes for the
       while loop to work!
   NOTE: need to add if statements to beginning and end of the while loops for
       voice==2 (or voice==3 in 4-part harmony...) to set/reset j for each of the
       different species
   PROBLEM: fifth-species is a problem because we don't know the size of the matrix...
   NOTE: now that we converted to numpy struct matrices, we can use np.concatenate()
2) or partition, add to, and concatenate matrixToLily's finalString
   PROBLEM: we know indexes for the partitions in C major, but what if there are accidentals?
3) or use regex on the .ly file (easy-ish since each .ly is almost exactly the same)
   then add the new notes to the soprano lines in the file
   PROBLEM: none, everyone loves regex. right, guys? ...guys?

going with option #1 now that we can easily adjust the matrix for an unknown number of notes"""

#from lib import getRhythm as gr  # commented out for fugueWriter debugging
import random
import numpy as np
#import re

# NOTE: just as getNextChord has destination and chordsRemaining params, so should these
#   use 'destinationPitch' and 'notesRemaining' to assign new pitches. notesRemaining
#   is easy to calculate for second- to fourth-species. but for fifth-species, this must
#   come from getRhythm.py

def secondSpecies(finalMTX):
    # NOTE: using the f.seek() and f.write() methods led to too many problems such as
    #   python 3.2+ not supporting most seek() values and write() overwriting the file's data...
    #   the solution was to copy the file into a long string and simply edit the string where
    #   necessary, then rewrite the file using open(filename, 'w') with the new string.
    # NOTE: not doing option #3 anymore, so don't need this anymore, keeping for
    # f = open(filename, 'r')
    # lilyString = f.readlines()
    # f.close()
    # #print(lilyString)

    # double the size of the notes in the matrix (2nd dimension) using np.concatenate()

    # convert old note data to new locations (newindex = 2*oldindex)

    # copy all columns except the first (pitch) for all even indices into the next odd one

    # halve all duration values (2nd column of the 3rd dimension)

    # then find new pitches to go into the odd columns
    for i in range(0,29,2):  # even columns, but not the last even column (30) - we're not changing the last measure
        # check for repeated pitches first
        if finalMTX[2][i][0] == finalMTX[2][i+2][0]:
            num1 = random.random()
            if num1 < 0.5: # add a step up into column i+1
                pass
            else:  # add a step down into column i+1
                pass

        # check for +2/-5 (wrapping), just use passing tone
        elif int(finalMTX[2][i][0]) == int(finalMTX[2][i+2][0])+2 or int(finalMTX[2][i][0]) == int(finalMTX[2][i+2][0])-5:
            # add a step up
            pass
        # check for -2/+5 (wrapping), just use passing tone
        elif int(finalMTX[2][i][0]) == int(finalMTX[2][i+2][0])-2 or int(finalMTX[2][i][0]) == int(finalMTX[2][i+2][0])+5:
            # add a step down
            pass
        # otherwise just find the direction and pick the next chord tone in that direction
        else:
            direction = finalMTX[2][i+2][3]
            if direction > 0:
                pass
            else:
                pass

    return finalMTX


def thirdSpecies(finalMTX):
    # add rest to beginning in soprano
    # use defineChord on both current chord and next chord to try to prioritize
    #   suspension possibilities
    # add ties after each note, except last!!!
    pass

    return finalMTX


def fourthSpecies(finalMTX):
    # quadruple the size of the notes in the matrix (2nd dimension) using np.concatenate()

    # convert old note data to new locations (newindex = 4*oldindex)

    # copy all columns except the first (pitch) for all mod4 indices into the next 3

    # 'quarterize' ('4' for .ly) all duration values (2nd column of the 3rd dimension)

    # then find new pitches to go into the new columns
    for i in range(15):
        # check for repeated pitches first
        if finalMTX[2][i][0] == finalMTX[2][i+4][0]:
            num1 = random.random()
            if num1 < 0.5:  # use c d c b c
                pass
            else:  # use c b c d c
                pass

        # check for +2/-5 (wrapping), just use c d c b a or c b c d e
        elif finalMTX[2][i+4][3] == 2 or finalMTX[2][i+4][3] == -5:  # TO DO: when we fix intervals, this is only good for ==2, not ==-5
            # use c b c d e
            pass
        # check for -2/+5 (wrapping), just use c d c b a or c b c d e
        elif finalMTX[2][i+4][3] == -2 or finalMTX[2][i+4][3] == 5:  # TO DO: when we fix intervals, this is only good for ==-2, not ==5
            # use c d c b a
            pass
        # check for +4/-4 (remember wrapping with mod7), just use c d e f g or c b a g f

        # otherwise just find the direction and magic() in that direction
        else:
            direction = finalMTX[2][i+4][3]
            if direction > 0:
                pass
            else:
                pass

    return finalMTX


def fifthSpecies(finalMTX):
    # MAKE A NEW MATRIX
    newMTX = np.array([('0', '0', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)],
                        dtype=[('pitch', 'S5'), ('duration', 'S5'), ('direction', 'i4'),
                               ('interval', 'i4'), ('chordRoot', 'i4'), ('seventhChord', 'i4'),
                               ('tonality', 'i4'), ('inversion', 'i4'), ('prevRoot', 'i4'),
                               ('distance', 'i4'), ('beat', 'i4'), ('measure', 'i4')])
    newMTX = np.expand_dims(newMTX, 0)  # add the 3rd dimension as new 1st dimension
    copyMTX = newMTX  # copy for tacking on one at a time
    for i in range(finalMTX.shape[0]-1):  # tack on one more voice - will create 3x16x12 or 4x16x12
        newMTX = np.concatenate((newMTX, copyMTX), 0)
    newNote = newMTX  # now we can use np.concatenate([newMTX, newNote],1) to add a new note

    prevj = 0
    for i in range(finalMTX[0][0][-1]):
        measureRhythmsArr = gr.getRhythm()
        for j in range(prevj, prevj+len(measureRhythmsArr)):
            if j > 0:  # don't add the new note if j==0 because we already created the first struct (it's just empty)
                np.concatenate([newMTX, newNote],1)  # add a new note
            # fill all appropriate columns of the soprano
            # for reference:
            # 12 note data types: pitch, duration, direction, interval, chord root,
            #   7th chord, tonality, inversion, prev chord root, distance, beat, measure
            for m in range(4,12):
                newMTX[finalMTX.shape[0]-1][i][m] = finalMTX[finalMTX.shape[0]-1][i][m]  # instead of hardwiring voice 2

            # find appropriate pitches. can still use +2/-2 logic for linear ascents/descents by the way, since
            #   durations are irrelevant; only the number of notes matters!

            # set pitches, duration, direction, interval for soprano

            # set measure value for all voices
            for n in range(finalMTX.shape[0]-1):
                newMTX[n][j][11] = finalMTX[0][i][11]

        # when done with all notes in the soprano in the current measure, fill in other voices exactly as they are in finalMTX
        for p in range(finalMTX.shape[0]):
            for q in range(12):
                newMTX[p][i][q] = finalMTX[p][i][q]

        # update prevj to know what index to start at in the next measure
        prevj = j + 1

    return newMTX
