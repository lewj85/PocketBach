import numToPitch as ntp
from numpy import shape

def matrixToLily(key, major, finalMTX, measures, maxVoices):
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
    finalString = ""
    j = 0
    #voice = 0
    totalNotes = finalMTX.shape[0]
    #print('total notes = ', totalNotes)

    for i in range(1, measures + 1):  # while there's another measure in the matrix

        # TO DO: all voices need to be added...
        for voice in range(maxVoices - 1, -1, -1):
            prevj = j  # store old j value to reset for each voice

            # while you haven't reached the end of the piece yet AND you're still on the current measure
            # NOTE: the statement below only works because of the short-circuit "and"!!!
            while j < totalNotes and finalMTX[j][11][voice] == i:
                #print('loop #', i)
                if key == 'C':
                    if major == 1:
                        # pitch
                        finalString += str.lower(ntp.numToPitch(finalMTX[j][0][voice], key))
                        #print(finalString)

                        # duration optional for repeated durations, but we will be using it
                        # TO DO: fix this to take timesig param and calculate/convert durations properly
                        finalString += str(finalMTX[j][1][voice])
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

            # measure symbol is optional, but we will be using it
            finalString += "| %" + str(i) + "\n"
            # print(finalString)

            # add \relative c to the beginning of each alto/tenor voice line
            # note that this happens after voice 2, but before voice is updated to 1
            if voice == 2:
                finalString += "\\relative f' "
            # add \relative f' to the beginning of each bass voice line
            # note that this happens after voice 1, but before voice is updated to 0
            elif voice == 1:
                finalString += "\\relative c "

            # reset j to old value for the next voice, but not after the last voice
            if voice != 0:
                j = prevj

        i += 1  # go to next measure
        finalString += "\n"
        # add \relative c'' to the beginning of each soprano voice line
        # note that this happens right before we begin the next measure
        # we have to make sure not to add it after the last measure though
        if j < totalNotes:
            finalString += "\\relative c'' "

    return finalString
