# TODO: think about how to fix this for chromaticism. perhaps take an extra param 0/1/-1 for normal/raised/lowered pitches
#     consider scope before doing extra work. minor keys would definitely need this (V chords)

from lib import distanceToPitch as dtp
from lib import tonalToPitch as ttp

def tonalToDistance(tonal, direction = 0, prevDist = None, voice = 0, key = 'C', major = True):

    # shouldn't happen
    if direction == 0:
        print('error: direction is 0 in tonalToDistance')
        return prevDist

    # in case we're at the start of the piece or coming from a rest
    if prevDist is None or prevDist == 88:
        # middle C is 39
        if voice == 0:  # bass
            prevDist = 24
        elif voice == 1:  # alto
            prevDist = 36
        elif voice == 2:  # soprano
            prevDist = 48
        else:
            # TODO: accommodate 4 voices, not just 3. need to pass maxVoices as param. default to 3
            print('voice out of range in tonalToDistance(). haven\'t accounted for more than 3 voices')
            return -1

    # if tonal is 0, it's a rest, so return 88 - NOTE: set index 0 to 88 below so distance 0+88=88
    # if tonal == 0:
    #     return 88
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
    if direction == -1:
        prevDist -= 12
        # if you're dropping an octave
        #print('tonal', tonal)
        #print('ttp.tonalToPitch(tonal)', ttp.tonalToPitch(tonal))
        #print('prevDist', prevDist)
        #print('dtp.distanceToPitch(prevDist)', dtp.distanceToPitch(prevDist))
        if ttp.tonalToPitch(tonal) == dtp.distanceToPitch(prevDist):
            print('dropping an octave')
            prevDist -=12

    return prevDist + pitchVals[tonal]
