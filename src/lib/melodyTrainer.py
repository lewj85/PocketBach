"""melodyTrainer uses Machine Learning to train a Neural Network to predict the next note of a procedurally-generated melody"""

import tensorflow as tf

"""
TODO: build a database of melodies for each composer's profile - start with Bach

features (using one-hot encoding): 
previousChordRoot (13) - a, as/bf, b, c, cs/df, d, ds/ef, e, f, fs/gf, g, gs/af, none
currentChordRoot (12) - a, as/bf, b, c, cs/df, d, ds/ef, e, f, fs/gf, g, gs/af
nextChordRoot (13) - a, as/bf, b, c, cs/df, d, ds/ef, e, f, fs/gf, g, gs/af, none/unknown
currentBeat (16) - 4 16th notes x 4 beats
downbeat - 0, 1
accentedBeat - 0, 1
previousNote (13) - rest, a, as/bf, b, c, cs/df, d, ds/ef, e, f, fs/gf, g, gs/af, none
previousNoteLength (9) - 16th, 8th, dotted-8th, quarter, dotted-quarter, half, dotted-half, whole, none
previousNoteApproachedLinearly - 0, 1
previousNoteDirection (3) - down, repeat, up
= 13+12+13+16+1+1+13+9+1+3 = 82 total
(consider adding other features, such as additional previous notes/rhythms for context/patterns)

labels:
note (13) - rest, a, as/bf, b, c, cs/df, d, ds/ef, e, f, fs/gf, g, gs/af
noteLength (8) - 16th, 8th, dotted-8th, quarter, dotted-quarter, half, dotted-half, whole

outputs should not have high confidence due to multiple acceptable options. 
threshold very low confident options, but then use random weighted probability to select from remaining possibilities.  
"""

def melodyTrainer(melodyDatabase):
    pass

