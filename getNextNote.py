# getNextNote() chooses the next note based on the previous note and current chord

import random
import numToPitch as ntp
import pitchToNum as ptn
import defineChord as dc

def getNextNote(key, major, noteMTX, finalMTX, index, measures, voice):
    # extract relevant data from matrices
    prevNote = finalMTX[index - 1][0][0]        # previous note
    currentRoot = noteMTX[index][4]             # current chord root
    nextChord = 1                               # next chord root
    if index < measures - 1:
        nextChord = noteMTX[index + 1][4]
    seventh = noteMTX[index][5]                 # seventh chord?
    tonality = noteMTX[index][6]                # tonal root?
    inversion = noteMTX[index][7]               # inversion

    # NOTE: need to add nextChord considerations!!
    #   especially for 7th chords because of 3rd inversion linear descents,
    #   but also for picking 2nd inversions, which should be rare if it isn't linear motion

    #print('prevNote = ', prevNote)  # debugging

    # generate random number - the 'soul of the composer'...
    num1 = random.random()
    # track chord tones
    chordVec = dc.defineChord(key, major, currentRoot, seventh, tonality, inversion)
    #print(chordVec)

    ################################################################
    # bass
    ################################################################
    # if bass line, high chance to pick root, even if there's a jump
    # NOTE: use actual data to derive percentages based on each composer's preferences
    # TO DO: need to consider repeated pitches
    # TO DO: need to make it unlikely to pick 5th for 2nd inversion...
    if voice == 0:
        if num1 < 0.5:  # 50% chance to simply pick root
            #print('root')
            nextNote = currentRoot
        elif num1 < 0.75:   # 25% chance to move up linearly (technically less than 25%,
                            # because we check to see if prevNote + 1 is a chord tone)
            if prevNote == 7:  # if prevNote is 7, can't use prevNote + 1
                if ntp.numToPitch(1) in chordVec:
                    #print('linear up')
                    nextNote = 1
                else:  # otherwise just go with root
                    #print('root')
                    nextNote = currentRoot
            else:  # if prevNote isn't 7, can use prevNote + 1
                if ntp.numToPitch(prevNote + 1) in chordVec:
                    #print('linear up')
                    nextNote = prevNote + 1
                else:  # otherwise just go with root
                    #print('root')
                    nextNote = currentRoot
        else:   # 25% chance to move down linearly (technically less than 25%,
                # because we check to see if prevNote - 1 is a chord tone)
            if prevNote == 1:  # if prevNote is 1, can't use prevNote - 1
                if ntp.numToPitch(7) in chordVec:
                    #print('linear down')
                    nextNote = 7
                else:  # otherwise just go with root
                    #print('root')
                    nextNote = currentRoot
            else:  # if prevNote isn't 1, can use prevNote - 1
                if ntp.numToPitch(prevNote - 1) in chordVec:
                    #print('linear down')
                    nextNote = prevNote - 1
                else:  # otherwise just go with root
                    #print('root')
                    nextNote = currentRoot

    ################################################################
    # soprano
    ################################################################
    # RULES:
    # can't be 3rd+3rd
    # can't be 5th+5th
    # NOTE: use actual data to derive percentages based on each composer's preferences
    # TO DO: need to check for note chosen in voices 0...
    elif voice == 2:
        # TO DO: enforce rules above by changing chordVec
        #if finalMTX[index][0][0] == blah


        if num1 < 0.2:  # 20% chance to repeat note (technically less)
            if ntp.numToPitch(prevNote) in chordVec:
                nextNote = prevNote
            else:
                if num1 < 0.5:  # 5% chance to pick root
                    nextNote = ptn.pitchToNum(chordVec[0])
                elif num1 < 0.15:  # 10% chance to pick 3rd
                    nextNote = ptn.pitchToNum(chordVec[1])
                else:  # 5% chance to pick 5th
                    nextNote = ptn.pitchToNum(chordVec[2])
        elif num1 < 0.6:    # 40% chance to move up linearly (technically less than 40%,
                            # because we check to see if prevNote + 1 is a chord tone)
            if prevNote == 7:  # if prevNote is 7, can't use prevNote + 1
                if ntp.numToPitch(1) in chordVec:
                    nextNote = 1
                else:
                    if num1 < 0.3:  # 10% chance to pick root
                        nextNote = ptn.pitchToNum(chordVec[0])
                    elif num1 < 0.5:  # 20% chance to pick 3rd
                        nextNote = ptn.pitchToNum(chordVec[1])
                    else:  # 10% chance to pick 5th
                        nextNote = ptn.pitchToNum(chordVec[2])
            else:  # if prevNote isn't 7, can use prevNote + 1
                if ntp.numToPitch(prevNote + 1) in chordVec:
                    nextNote = prevNote + 1
                else:
                    if num1 < 0.3:  # 10% chance to pick root
                        nextNote = ptn.pitchToNum(chordVec[0])
                    elif num1 < 0.5:  # 20% chance to pick 3rd
                        nextNote = ptn.pitchToNum(chordVec[1])
                    else:  # 10% chance to pick 5th
                        nextNote = ptn.pitchToNum(chordVec[2])
        else:   # 40% chance to move down linearly (technically less than 40%,
                # because we check to see if prevNote - 1 is a chord tone)
            if prevNote == 1:  # if prevNote is 1, can't use prevNote - 1
                if ntp.numToPitch(7) in chordVec:
                    nextNote = 7
                else:
                    if num1 < 0.7:  # 10% chance to pick root
                        nextNote = ptn.pitchToNum(chordVec[0])
                    elif num1 < 0.9:  # 20% chance to pick 3rd
                        nextNote = ptn.pitchToNum(chordVec[1])
                    else:  # 10% chance to pick 5th
                        nextNote = ptn.pitchToNum(chordVec[2])
            else:  # if prevNote isn't 1, can use prevNote - 1
                if ntp.numToPitch(prevNote - 1) in chordVec:
                    nextNote = prevNote - 1
                else:
                    if num1 < 0.7:  # 10% chance to pick root
                        nextNote = ptn.pitchToNum(chordVec[0])
                    elif num1 < 0.9:  # 20% chance to pick 3rd
                        nextNote = ptn.pitchToNum(chordVec[1])
                    else:  # 10% chance to pick 5th
                        nextNote = ptn.pitchToNum(chordVec[2])

    ################################################################
    # alto/tenor
    ################################################################
    # RULES:
    # if root+root, must be 3rd
    # if root+3rd, can be root or 5th
    # if root+5th, must be 3rd
    # if 3rd+root, can be root or 5th
    # can't be 3rd+3rd
    # if 3rd+5th, must be root
    # if 5th+root, must be 3rd
    # if 5th+3rd, must be root
    # can't be 5th+5th
    # NOTE: use actual data to derive percentages based on each composer's preferences
    # TO DO: need to check for note chosen in voice 0 and 1...
    else:
        # TO DO: enforce rules above by changing chordVec
        #if finalMTX[index][0][0] == blah and finalMTX[index][0][2] == blah


        if num1 < 0.75:  # 75% chance to repeat note if possible
            if ntp.numToPitch(prevNote) in chordVec:
                nextNote = prevNote
            else:
                if num1 < 0.25:
                    nextNote = ptn.pitchToNum(chordVec[0])
                elif num1 < 0.5:
                    nextNote = ptn.pitchToNum(chordVec[1])
                else:
                    nextNote = ptn.pitchToNum(chordVec[2])
        # TO DO: elif linear prevNote+1/-1 considerations?
        else:
            if num1 < 0.85:  # 10% chance to pick root
                nextNote = ptn.pitchToNum(chordVec[0])
            elif num1 < 0.95:  # 10% chance to pick 3rd
                nextNote = ptn.pitchToNum(chordVec[1])
            else:  # 5% chance to pick 5th
                nextNote = ptn.pitchToNum(chordVec[2])


    return nextNote
