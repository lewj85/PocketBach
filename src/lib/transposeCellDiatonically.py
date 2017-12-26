"""transposeCellDiatonically() transposes a Cell object passed to it diatonically (not chromatically)"""

from lib import pitchToTonal as ptt
from lib import tonalToPitch as ttp
from lib import musicObjects as mo
from lib import transposeDistance as td

# params are mo.Cell, mo.Chord, mo.Chord
# returns array of Note classes, destination pitch
# up = bool, transpose up or down

def transposeCellDiatonically(oldCell, newChord, newNextChord, direction = 1, newDestinationDistance = None):

    notes = []

    # set up
    if newDestinationDistance is not None and newDestinationDistance != 88:
        if oldCell.destination < newDestinationDistance:
            direction = 1
        else:
            direction = -1
    # don't make this an else to the above if because we need to set a correct direction for transposeDistance
    if newDestinationDistance is None:
        # set a new destination distance based on the old cell's destination
        newDestinationDistance = td.transposeDistance(oldCell.destination, oldCell.chord, newChord, direction)
        #print("newDestinationDistance", newDestinationDistance)
        #newDestinationTonal = dtt.distanceToTonal(newDestinationDistance)

    # first get distance between old chord and new chord
    distanceBetweenTonal = newChord.root - oldCell.chord.root
    if direction == 1 and distanceBetweenTonal < 0:
        distanceBetweenTonal += 7
    elif direction == -1 and distanceBetweenTonal > 0:
        distanceBetweenTonal -= 7
    #print('distanceBetweenTonal', distanceBetweenTonal)

    for oldNote in oldCell.notes:

        # adjust pitch
        newVal = (ptt.pitchToTonal(oldNote.pitch) + distanceBetweenTonal - 1) % 7 + 1  # TODO: doublecheck the -1 and +1
        newPitch = ttp.tonalToPitch(newVal)
        # adjust distance
        # TODO: think diatonically, consider minor keys, etc - use pitchToDistance()
        newDistance = td.transposeDistance(oldNote.distance, oldCell.chord, newChord, direction)

        #print('transposing:', oldNote.pitch, ptt.pitchToTonal(oldNote.pitch), oldNote.distance, '--->', newPitch, newVal, newDistance)

        # add everything else
        notes.append(mo.Note(newPitch, newDistance, oldNote.rhythm, oldNote.tied, newChord.root,
                             oldNote.tonality, oldNote.seventh, oldNote.inversion,
                             oldNote.secondary, oldNote.secondaryRoot,
                             oldNote.key, oldNote.major, oldNote.timesig))

    newCell = mo.Cell(newChord, newNextChord, oldCell.beats, notes, newDestinationDistance, oldCell.voice)

    return newCell
