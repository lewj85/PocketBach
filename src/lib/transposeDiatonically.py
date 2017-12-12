"""writeAnswer() creates a response to a subject passed to it"""

from lib import getRhythms as gr
from lib import defineChord as dc
from lib import getNotes as gn
from lib import pitchToTonal as ptt
from lib import tonalToPitch as ttp
from lib import musicObjects as mo
from lib import distanceToTonal as dtt
from lib import pitchToDistance as ptd
import random


# params are mo.Cell, mo.Chord, mo.Chord
# returns array of Note classes, destination pitch
# up = bool, transpose up or down

def transposeDiatonically(oldCell, newChord, newNextChord, newDestinationDistance, up = True):

    notes = []

    # set up
    up = oldCell.destination < newDestinationDistance

    # first get distance between old chord and new chord
    # NOTE: may be negative
    distanceBetweenTonal = oldCell.chord.root - ptt.pitchToTonal(newChord.root)

    # # next check destination because it's possible/probable only transposition is needed
    destination = (ptt.pitchToTonal(dtt.distanceToTonal(oldCell.destination)) + (distanceBetweenTonal - 1)) % 7 + 1
    # if ttp.tonalToPitch(destination) in newNextChord.getPitches()[0]:

    for oldNote in oldCell.notes:

        # adjust pitch
        newVal = (ptt.pitchToTonal(oldNote.pitch) + distanceBetweenTonal - 1) % 7 + 1
        newPitch = ttp.tonalToPitch(newVal)
        print('transposing:', oldNote.pitch, '--->', newPitch, newVal)

        # adjust root
        newRoot = (oldNote.root + distanceBetweenTonal - 1) % 7 + 1

        # adjust distance
        # TODO: think diatonically, consider minor keys, etc - use pitchToDistance()
        newDistance = oldNote.distance + distanceBetween
        if up is False:
            newDistance -= 12 # drop an octave

        # add everything else
        notes.append(mo.Note(newPitch, newDistance, oldNote.rhythm, oldNote.tied, newRoot,
                             oldNote.tonality, oldNote.seventh, oldNote.inversion,
                             oldNote.secondary, oldNote.secondaryRoot,
                             oldNote.key, oldNote.major, oldNote.timesig))

    return notes, destination
