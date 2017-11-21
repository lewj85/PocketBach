"""writeAnswer() creates a response to a subject passed to it"""

from lib import getRhythms as gr
from lib import defineChord as dc
from lib import getNotes as gn
from lib import pitchToNum as ptn
from lib import numToPitch as ntp
from lib import musicObjects as mo
from lib import tonalToDistance as ttd
import random


# returns array of Note classes, destination pitch

def transposeDiatonically(oldCell, newChord, newNextChord):

    notes = []
    down = False

    # first get distance between old chord and new chord
    # NOTE: may be negative
    distanceBetween = oldCell.chord.root - newChord

    # next check destination because it's possible/probable only transposition is needed
    if oldCell.destination + ((distanceBetween - 1) % 7 + 1)  in newNextChord.getPitches()[0]:

        for note in oldCell.notes:

            # adjust pitch
            newVal = (ptn.pitchToNum(note.pitch) + distanceBetween - 1) % 7 + 1
            newPitch = ntp.numToPitch(newVal)

            # adjust root
            newRoot = (note.root + distanceBetween - 1) % 7 + 1

            # adjust distance
            # TODO: think diatonically, consider minor keys, etc - use tonalToDistance()
            newDistance = note.distance + ttd.tonalToDistance()

            # add everything else
            notes.append(mo.Note(newPitch, newDistance, note.rhythm, note.tied, newRoot,
                                 note.tonality, note.seventh, note.inversion,
                                 note.secondary, note.secondaryRoot,
                                 note.key, note.major, note.timesig))

    # if a destination doesn't match, find how far off we are
    else:
        pass

    return notes, destination
