'''makeMatrix(N) creates a matrix for N number of voices. It returns one column of the matrix: a list with default values.'''

import numpy as np

def makeMatrix(voices):
    newMTX = np.array([('0', '0', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)],
                          dtype=[('pitch', 'S5'), ('duration', 'S5'), ('direction', 'i4'),
                                 ('interval', 'i4'), ('chordRoot', 'i4'), ('seventhChord', 'i4'),
                                 ('tonality', 'i4'), ('inversion', 'i4'), ('prevRoot', 'i4'),
                                 ('distance', 'i4'), ('beat', 'i4'), ('measure', 'i4')])
    newMTX = np.expand_dims(newMTX, 0)  # add the 3rd dimension as new 1st dimension
    copyMTX = newMTX  # copy for tacking on one at a time
    for i in range(voices - 1):  # tack on more voices - will create 3x16x12 or 4x16x12
        newMTX = np.concatenate((newMTX, copyMTX), 0)

    # to add new notes to the matrix in files that call this function, do 2 things:
    # 1) newNote = yourMTXname  # once, BEFORE you replace the default values
    # 2) yourMTXname = np.concatenate((yourMTXname, newNote), 1)  # as many times as you want
    return newMTX
