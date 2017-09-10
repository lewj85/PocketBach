import numToPitch as ntp

def matrixToLily(key, major, finalMTX, measures, maxVoices):
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
    finalString = ""
    for i in range(measures):  # while there's another measure in the matrix
        j = 0
        # TO DO:
        for voice in range(maxVoices):
            while finalMTX[j][11][voice] == i + 1:  # while still on the current measure
                print('loop #', i)
                if key == 'C':
                    if major == 1:
                        # pitch
                        finalString += str.lower(ntp.numToPitch(finalMTX[j][0][voice]))

                        # duration optional for repeated durations, but we will be using it
                        finalString += finalString + str(finalMTX[j][1][voice])

                        # TO DO: direction only needs to check if > 4 for "'" or < -4 for ","

                        # chord root and 7th chord not needed for LilyPond

                        # TO DO: tonality not needed in major (until we add secondary dominants)

                        # inversion and prev chord root not needed for LilyPond

                        # TO DO: pickup needed for LilyPond but not for chorale

                        # beat not needed for LilyPond

                        # TO DO: articulation will go here eventually

                        # put a space after each note
                        finalString += " "

                        # TO DO: ties go here with a space after them too

            # measure symbol is optional, but we will be using it
            finalString += "|\n"

        i += 1  # go to next measure

    return finalString
