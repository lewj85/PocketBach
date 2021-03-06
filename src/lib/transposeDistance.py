from lib import distanceToTonal as dtt
from lib import tonalToDistance as ttd

# oldChord and newChord are Chord objects, not root ints
# direction = 1 for up, = -1 for down. should never be transposing if = 0
def transposeDistance(oldDistance, oldChord, newChord, direction = 1):

    tonalDistanceBetween = newChord.root - oldChord.root  # can be negative
    #print("tonalDistanceBetween", tonalDistanceBetween)
    if direction == 0:  # this should never happen but...
        print('error in transposeDistance: direction == 0')
        return oldDistance
    elif direction == 1 and tonalDistanceBetween < 0:
        tonalDistanceBetween += 7
    elif direction == -1 and tonalDistanceBetween > 0: # > -1 because we may want to transpose down an octave?
        tonalDistanceBetween -= 7

    #print('oldDistance', oldDistance)
    oldTonal = dtt.distanceToTonal(oldDistance)
    #print('oldTonal', oldTonal)
    newTonal = oldTonal + tonalDistanceBetween
    if newTonal < 1:
        newTonal += 7
    elif newTonal > 7:
        newTonal -= 7
    #print('newTonal', newTonal)
    # need tonalToDistance because distances between distance values isn't consistent like distances between tonal values
    newDistance = ttd.tonalToDistance(newTonal, direction, oldDistance)
    #print('newDistance', newDistance)

    return newDistance
