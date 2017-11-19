"""writeAnswer() creates a response to a subject passed to it"""

from lib import getRhythms as gr
from lib import defineChord as dc
from lib import getNotes as gn
from lib import pitchToNum as ptn
import random


# returns array of Note classes, destination pitch

def writeAnswer(oldCell, newChord):

    # first check destinations because it's possible/probable only transposition is needed
    destNotes = dc.defineChord(newChord)
    if oldCell.destination in destNotes[0]:
        pass
    # if a destination doesn't match, find how far off we are
    else:
        pass

    return notes, destination