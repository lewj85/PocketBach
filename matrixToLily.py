import numToPitch as ntp
from numpy import shape

def matrixToLily(key, major, finalMTX, measures, maxVoices):
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
    finalString = ""
    j = 0
    voice = 0
    totalNotes = finalMTX.shape[0]
    #print('total notes = ', totalNotes)

    for i in range(1, measures + 1):  # while there's another measure in the matrix
        # TO DO: all voices need to be added...
        #for voice in range(maxVoices):

        # while you haven't reached the end of the piece yet AND you're still on the current measure
        # NOTE: the statement below only works because of the short-circuit "and"!!!
        while j < totalNotes and finalMTX[j][11][voice] == i:
            print('loop #', i)
            if key == 'C':
                if major == 1:
                    # pitch
                    finalString += str.lower(ntp.numToPitch(finalMTX[j][0][voice], key))
                    #print(finalString)

                    # duration optional for repeated durations, but we will be using it
                    # NOTE: duration in matrix does not equal LilyPond duration notation!!!
                    #   so must use dictionary to return correct symbol
                    # TO DO: fix this to take timesig param and calculate/convert durations properly
                    matrixDuration = str(finalMTX[j][1][voice])
                    lilyDuration = {
                        '1': '4',
                        '2': '2',
                        '3': '2.',  # for 3/4 time
                        '4': '1'
                    }.get(matrixDuration, '1')  # find 'pitch' in dictionary above, otherwise default to 1
                    finalString += lilyDuration
                    #print(finalString)

                    # TO DO: direction only needs to check if > 4 for "'" or < -4 for ","

                    # chord root and 7th chord not needed for LilyPond

                    # TO DO: tonality not needed in major (until we add secondary dominants)

                    # inversion and prev chord root not needed for LilyPond

                    # TO DO: pickup needed for LilyPond but not for chorale

                    # beat not needed for LilyPond

                    # TO DO: articulation will go here eventually

                    # put a space after each note
                    finalString += " "
                    #print(finalString)

                    # TO DO: ties go here with a space after them too

            j += 1  # go to next note

        i += 1  # go to next measure

        # measure symbol is optional, but we will be using it
        finalString += "|\n"
        print(finalString)

    return finalString
