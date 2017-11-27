# TODO: think about how to fix this. perhaps take an extra param 0/1/-1 for normal/raised/lowered pitches
#     consider scope before doing extra work. minor keys would definitely need this (V chords)

# TODO: rename numToPitch and pitchToNum to "tonal" instead of "num" for consistency

from lib import distanceToPitch as dtp

def tonalToDistance(tonal, direction = 0, prevDist = None, voice = 0, key = 'C'):

    if prevDist is None:
        # middle C is 39
        if voice == 0:  # bass
            prevDist = 24
        elif voice == 1:  # alto
            prevDist = 36
        elif voice == 2:  # soprano
            prevDist = 48
        else:
            # should never happen
            print('voice out of range in tonalToDistance()')
            return -1

    # if tonal is 0, it's a rest, so return distance 0+88 = 88
    # assumes direction is 1, so if new tonal is same as prevDist, uses +12 to go up an octave instead of +0
    # if key == 'C':
    # TODO: add chromatic pitches 'as' or 'bf', 'cs' or 'df', etc
    if dtp.distanceToPitch(prevDist) == 'a':
        pitchVals = [88, 3, 5, 7, 8, 10, 12, 2]
    elif dtp.distanceToPitch(prevDist) == 'b':
        pitchVals = [88, 1, 3, 5, 6, 8, 10, 12]
    elif dtp.distanceToPitch(prevDist) == 'c':
        pitchVals = [88, 12, 2, 4, 5, 7, 9, 11]
    elif dtp.distanceToPitch(prevDist) == 'd':
        pitchVals = [88, 10, 12, 2, 3, 5, 7, 9]
    elif dtp.distanceToPitch(prevDist) == 'e':
        pitchVals = [88, 8, 10, 12, 1, 3, 5, 7]
    elif dtp.distanceToPitch(prevDist) == 'f':
        pitchVals = [88, 7, 9, 11, 12, 2, 4, 6]
    elif dtp.distanceToPitch(prevDist) == 'g':
        pitchVals = [88, 5, 7, 9, 10, 12, 2, 4]
    else:
        # should never happen - not adding chromatic pitches yet, consider scope
        print('prevDist out of range in tonalToDistance()')

    # necessary because we assume direction is 1 when we add
    if direction == 0:
        return prevDist
    elif direction == -1:
        prevDist -= 12
        # if you're dropping an octave
        if ttp.tonalToPitch(tonal) == dtp.distanceToPitch(prevDist):
            prevDist -=12

    return prevDist + pitchVals[tonal]
