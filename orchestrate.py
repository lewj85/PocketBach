# orchestrate() fleshes out all voices for a given chord matrix

import random

def orchestrate(noteMTX, chordsPerMeasure=1, beatsPerMeasure=4):
    # 3 dimensional matrix finalMTX contains the fully orchestrated chorale
    # x = time (chords)
    # y = note (note and chord data)
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
    # z = voice
    #   0 = bass, 1 = alto/tenor, 2 = soprano
    finalMTX = []

    # first chord, bass
    finalMTX[0][:][0] = noteMTX[0][:]








    return finalMTX

