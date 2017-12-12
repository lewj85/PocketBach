"""transposeCellDiatonically() transposes a Cell object passed to it diatonically (not chromatically)"""

#from lib import getRhythms as gr
#from lib import defineChord as dc
#from lib import getNotes as gn
from lib import pitchToTonal as ptt
from lib import tonalToPitch as ttp
from lib import musicObjects as mo
#from lib import distanceToTonal as dtt
#from lib import pitchToDistance as ptd
from lib import transposeDistance as td
import random


# params are mo.Cell, mo.Chord, mo.Chord
# returns array of Note classes, destination pitch
# up = bool, transpose up or down

def transposeCellDiatonically(oldCell, newChord, newNextChord, direction = 1, newDestinationDistance = None):

    notes = []

    # set up
    if newDestinationDistance is not None:
        if oldCell.destination < newDestinationDistance:
            direction = 1
        else:
            direction = -1
    else:
        # set a new destination distance based on the old cell's destination
        newDestinationDistance = td.transposeDistance(oldCell.destination, oldCell.chord, newChord, direction)
        #newDestinationTonal = dtt.distanceToTonal(newDestinationDistance)

    # first get distance between old chord and new chord
    distanceBetweenTonal = newChord.root - oldCell.chord.root
    if direction == 1 and distanceBetweenTonal < 0:
        distanceBetweenTonal += 7
    elif direction == -1 and distanceBetweenTonal > 0:
        distanceBetweenTonal -= 7

    for oldNote in oldCell.notes:

        # adjust pitch
        newVal = (ptt.pitchToTonal(oldNote.pitch) + distanceBetweenTonal - 1) % 7 + 1  # TODO: doublecheck the -1 and +1
        newPitch = ttp.tonalToPitch(newVal)
        print('transposing:', oldNote.pitch, '--->', newPitch, newVal)

        # adjust distance
        # TODO: think diatonically, consider minor keys, etc - use pitchToDistance()
        newDistance = td.transposeDistance(oldNote.distance, oldCell.chord, newChord, direction)

        # add everything else
        notes.append(mo.Note(newPitch, newDistance, oldNote.rhythm, oldNote.tied, newChord.root,
                             oldNote.tonality, oldNote.seventh, oldNote.inversion,
                             oldNote.secondary, oldNote.secondaryRoot,
                             oldNote.key, oldNote.major, oldNote.timesig))

    newCell = mo.Cell(newChord, newNextChord, oldCell.beats, notes, newDestinationDistance, oldCell.voice)

    return newCell
