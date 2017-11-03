"""writeAnswer() creates a response to a subject passed to it"""

import getRhythm as gr
import defineChord as dc
import getNotes as gn
import pitchToNum as ptn
import random

def writeCountersubject(chordsList = None, noteArray = None, measures = 2, measure = 3, key = 'C', major = 1, timeSig = None):

    # avoid mutable defaults since we'll be calling writeSubject often
    if chordsList is None:
        chordsList = [5,1,2]  # default to V-I-ii
    if noteArray is None:
        noteArray = []
    if timeSig is None:
        timeSig = [4,4]

    # get old rhythms
    oldRhythms = []
    for i in noteArray:
        oldRhythms.append(i[1])
    oldRhythms.pop()  # noteArray had 1 extra rhythm in it - a whole note. remove it.

    # make sure not to re-use same rhythms
    newRhythms = gr.randRhythm()
    # NOTE: rather than just compare newRhythms == oldRhythms, avoid matching 1st index too to add diversity
    while newRhythms[0] == oldRhythms[0]:
        newRhythms = gr.randRhythm()

    chordsList
