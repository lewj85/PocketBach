import numToPitch as ntp
from numpy import shape

def matrixToLily(key, major, finalMTX, measures, maxVoices):
    #   12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, distance, beat, measure
    finalString = ""
    j = 0
    #voice = 0
    #print(finalMTX.shape)
    totalNotes = finalMTX.shape[1]  # changed from [0] to [1] after voice changed dimensions
    #print('total notes = ', totalNotes)

    # for each measure
    # NOTE: this must be above voice because we write all voices one measure at a time
    for i in range(1, measures + 1):
        # for each voice
        for voice in range(maxVoices - 1, -1, -1):
            prevj = j  # store old j value to reset for each voice
            # while you haven't reached the end of the piece yet AND you're still on the current measure
            #   add each note to the current line (voice) in the string
            # NOTE: the statement below only works because of the short-circuit "and"!!!
            while j < totalNotes and finalMTX[voice][j][11] == i:
                # NOTE: for different species, some notes in the matrix will have the same measure but pitch = '0'
                #   so we have to check for these and increment j instead of adding anything to the string
                if int(finalMTX[voice][j][0]) != 0:
                    if key == 'C':
                        if major == 1:
                            # pitch
                            # NOTE: str.lower() no longer needed as they are now lowercase
                            # TO DO: add flats and sharps for secondary dominants
                            finalString += ntp.numToPitch(key, int(finalMTX[voice][j][0]))
                            #print(finalString)

                            # duration optional for repeated durations, but we will be using it
                            # TO DO: fix this to take timesig param and calculate/convert durations properly
                            finalString += str(int(finalMTX[voice][j][1])) # was printing '1' instead of 1, so converted to int and back to string!
                            #print(finalString)

                            # TO DO: direction only needs to check if > 4 for "'" or < -4 for ","

                            # chord root and 7th chord not needed for LilyPond

                            # TO DO: tonality not needed in major (until we add secondary dominants)

                            # inversion and prev chord root not needed for LilyPond

                            # TO DO: distance needed for LilyPond to prevent voice crossing

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
                finalString += "%alto\n\\relative g' "
            # add \relative f' to the beginning of each bass voice line
            # note that this happens after voice 1, but before voice is updated to 0
            elif voice == 1:
                finalString += "%bass\n\\relative c "

            # reset j to old value for the next voice, but not after the last voice
            if voice != 0:
                j = prevj

        i += 1  # go to next measure
        finalString += "\n"
        # add \relative c'' to the beginning of each soprano voice line
        # note that this happens right before we begin the next measure
        # we have to make sure not to add it after the last measure though
        if j < totalNotes:
            finalString += "%soprano\n\\relative c'' "

    return finalString
