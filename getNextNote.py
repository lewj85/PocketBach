# getNextNote() chooses the next note based on the previous note and current chord

import random
import numToPitch as ntp
import pitchToNum as ptn
import defineChord as dc

def getNextNote(key, major, noteMTX, finalMTX, index, measures, voice, maxVoices):
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

    # for reference:
    # 12 note data types: pitch, duration, direction, interval, chord root,
    #   7th chord, tonality, inversion, prev chord root, pickup, beat, measure

    # generate random number - PocketBach's soul...
    num1 = random.random()

    # track chord tones
    chordVec = dc.defineChord(key, major, currentRoot, seventh, tonality, inversion)
    #print(chordVec)

    ################################################################
    # bass
    ################################################################
    # RULES:
    # 7th chords with only 3 voices cannot be in 2nd inversion (5th in bass)
    # bass line has high chance to pick root, even if there's a jump
    # NOTE: use actual data to derive percentages based on each composer's preferences
    # TO DO: need to consider repeated pitches
    if voice == 0:

        # 7th chords with only 3 voices cannot be in 2nd inversion (5th in bass)
        if noteMTX[index][5] == 1 and maxVoices == 3:
            # can also use "del chordVec[2]"
            chordVec = [chordVec[0], chordVec[1], chordVec[3]]

        if num1 < 0.4:  # 40% chance to simply pick root
            nextNote = currentRoot
        elif num1 < 0.6:    # 20% chance to repeat bass note (technically less than 20%,
                            # because we check to see if prevNote is a chord tone)
            if prevNote in chordVec:  # repeat prevNote if you can
                nextNote = prevNote
            else:  # otherwise just go with root
                nextNote = currentRoot
        elif num1 < 0.8:   # 20% chance to move up linearly (technically less than 20%,
                            # because we check to see if prevNote + 1 is a chord tone)
            if prevNote == 7:  # if prevNote is 7, can't use prevNote + 1
                if ntp.numToPitch(1) in chordVec:
                    nextNote = 1
                else:  # otherwise just go with root
                    nextNote = currentRoot
            else:  # if prevNote isn't 7, can use prevNote + 1
                if ntp.numToPitch(prevNote + 1) in chordVec:
                    nextNote = prevNote + 1
                else:  # otherwise just go with root
                    nextNote = currentRoot
        else:   # 20% chance to move down linearly (technically less than 20%,
                # because we check to see if prevNote - 1 is a chord tone)
            if prevNote == 1:  # if prevNote is 1, can't use prevNote - 1
                if ntp.numToPitch(7) in chordVec:
                    nextNote = 7
                else:  # otherwise just go with root
                    nextNote = currentRoot
            else:  # if prevNote isn't 1, can use prevNote - 1
                if ntp.numToPitch(prevNote - 1) in chordVec:
                    nextNote = prevNote - 1
                else:  # otherwise just go with root
                    nextNote = currentRoot

    ################################################################
    # soprano
    ################################################################
    # RULES:
    # can't be 3rd+3rd
    # can't be 5th+5th
    # 7th chords with 3 voices cannot have a 5th
    # 7th chords with 3 voices cannot be root+root
    # TO DO: no parallel 5ths or octaves
    # NOTE: use actual data to derive percentages based on each composer's preferences
    elif voice == 2:
        # enforce rules above by changing chordVec!!!
        # check for 7th chords first
        if finalMTX[index][5][0] == 0:  # if not a 7th chord
            if finalMTX[index][7][0] == 1:  # if inversion = 1
                # can also use "del chordVec[1]"
                chordVec = [chordVec[0], chordVec[2]]  # can't be 3rd+3rd
            elif finalMTX[index][7][0] == 2:  # if inversion = 2
                chordVec = [chordVec[0], chordVec[1]]  # can't be 5th+5th
        else:  # elif finalMTX[index][5][0] == 1:
            # 7th chords with 3 voices cannot have a 5th
            if maxVoices == 3:
                if finalMTX[index][7][0] == 0:  # if inversion = 0
                    chordVec = [chordVec[1], chordVec[3]]  # 7th chords with 3 voices cannot be root+root
                elif finalMTX[index][7][0] == 1:  # if inversion = 1
                    chordVec = [chordVec[0], chordVec[3]]
                # elif finalMTX[index][7][0] == 2:  # NOTE: this should never happen with only 3 voices...
                #    chordVec = [chordVec[0], chordVec[1], chordVec[3]]
                else:  # finalMTX[index][7][0] == 3:  # if inversion = 3
                    chordVec = [chordVec[0], chordVec[1]]
            else:
                if finalMTX[index][7][0] == 1:  # if inversion = 1
                    chordVec = [chordVec[0], chordVec[2], chordVec[3]]
                elif finalMTX[index][7][0] == 2:  # if inversion = 2
                    chordVec = [chordVec[0], chordVec[1], chordVec[3]]
                elif finalMTX[index][7][0] == 3:  # if inversion = 3
                    chordVec = [chordVec[0], chordVec[1], chordVec[2]]

        if num1 < 0.75:     # 75% chance to repeat note (technically less
                            # because we check to see if prevNote is a chord tone)
            if ntp.numToPitch(prevNote) in chordVec:
                return prevNote
        elif num1 < 0.3:    # 30% chance to move up linearly (technically less than 30%,
                            # because we check to see if prevNote + 1 is a chord tone)
            if prevNote == 7:  # if prevNote is 7, can't use prevNote + 1
                if ntp.numToPitch(1) in chordVec:
                    return 1
            else:  # if prevNote isn't 7, can use prevNote + 1
                if ntp.numToPitch(prevNote + 1) in chordVec:
                    return prevNote + 1
        elif num1 < 0.6:    # 60% chance to move down linearly (technically less than 30%,
                            # because we check to see if prevNote - 1 is a chord tone)
                            # NOTE: higher than previous elif to balance up and down movement
            if prevNote == 1:  # if prevNote is 1, can't use prevNote - 1
                if ntp.numToPitch(7) in chordVec:
                    return 7
            else:  # if prevNote isn't 1, can use prevNote - 1
                if ntp.numToPitch(prevNote - 1) in chordVec:
                    return prevNote - 1

        # 25% base chance to run this anyway, but there's a small chance the note will fall
        # through the if-elifs above, so don't put this line into "else:"
        return ptn.pitchToNum(chordVec[random.randint(0, len(chordVec) - 1)])

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
    # can't be 7th+7th
    # 7th chords with 3 voices cannot have a 5th
    # 7th chords with 3 voices cannot be root+root
    # 7th chords with 3 voices with root+3rd, must be 7th
    # 7th chords with 3 voices with root+7th, must be 3rd
    # 7th chords with 3 voices with 3rd+root, must be 7th
    # 7th chords with 3 voices with 3rd+7th, must be 7th
    # 7th chords with 3 voices with 7th+root, must be 3rd
    # 7th chords with 3 voices with 7th+3rd, must be root
    # TO DO: no parallel 5ths or octaves
    # NOTE: use actual data to derive percentages based on each composer's preferences
    # TO DO: need to check for note chosen in voice 0 and 1...
    else:
        # enforce rules above by changing chordVec!!!
        # check for 7th chords first
        if finalMTX[index][5][0] == 0:  # if not a 7th chord
            if finalMTX[index][7][0] == 0:  # if inversion = 0
                if finalMTX[index][0][2] == ptn.pitchToNum(chordVec[0]):  # if root+root, must be 3rd
                    return ptn.pitchToNum(chordVec[1])  # NOTE: return
                elif finalMTX[index][0][2] == ptn.pitchToNum(chordVec[1]):  # if root+3rd, can be root or 5th
                    chordVec = [chordVec[0], chordVec[2]]
                else:  # if root+5th, must be 3rd
                    return ptn.pitchToNum(chordVec[1])  # NOTE: return
            elif finalMTX[index][7][0] == 1:  # if inversion = 1
                if finalMTX[index][0][2] == ptn.pitchToNum(chordVec[0]):  # if 3rd+root, can be root or 5th
                    chordVec = [chordVec[0], chordVec[2]]
                # elif # can't be 3rd+3rd
                else:  # if 3rd+5th, must be root
                    return ptn.pitchToNum(chordVec[1])  # NOTE: return
            elif finalMTX[index][7][0] == 2:  # if inversion = 2
                if finalMTX[index][0][2] == ptn.pitchToNum(chordVec[0]):  # if 5th+root, must be 3rd
                    return ptn.pitchToNum(chordVec[1])  # NOTE: return
                # elif # can't be 5th+5th
                else:  # if 5th+3rd, must be root
                    return ptn.pitchToNum(chordVec[0])  # NOTE: return
        else:  # if a 7th chord
            # 7th chords with 3 voices cannot have a 5th
            if maxVoices == 3:
                if finalMTX[index][7][0] == 0:  # if inversion = 0
                    # 7th chords with 3 voices cannot be root+root
                    if finalMTX[index][0][2] == ptn.pitchToNum(chordVec[1]):  # 7th chords with 3 voices with root+3rd, must be 7th
                        return ptn.pitchToNum(chordVec[3])  # NOTE: return
                    # elif # 7th chords with 3 voices cannot have a 5th
                    else:  # 7th chords with 3 voices with root+7th, must be 3rd
                        return ptn.pitchToNum(chordVec[1])  # NOTE: return
                elif finalMTX[index][7][0] == 1:  # if inversion = 1
                    if finalMTX[index][0][2] == ptn.pitchToNum(chordVec[0]):  # 7th chords with 3 voices with 3rd+root, must be 7th
                        return ptn.pitchToNum(chordVec[3])  # NOTE: return
                    # elif # can't be 3rd+3rd
                    # elif # 7th chords with 3 voices cannot have a 5th
                    else:  # 7th chords with 3 voices with 3rd+7th, must be root
                        return ptn.pitchToNum(chordVec[0])  # NOTE: return
                # elif # 7th chords with 3 voices cannot have a 5th
                else:  # if inversion = 3
                    if finalMTX[index][0][2] == ptn.pitchToNum(chordVec[0]):  # 7th chords with 3 voices with 7th+root, must be 3rd
                        return ptn.pitchToNum(chordVec[1])  # NOTE: return
                    else:  # 7th chords with 3 voices with 7th+3rd, must be root
                        return ptn.pitchToNum(chordVec[0])  # NOTE: return
                    # elif # 7th chords with 3 voices cannot have a 5th
                    # can't be 7th+7th

            # TO DO: many possible combinations and rules for 4 voices below...
            # not relevant at the moment so skipping them...
            else:
                if finalMTX[index][7][0] == 1:  # if inversion = 1
                    chordVec = [chordVec[0], chordVec[2], chordVec[3]]
                elif finalMTX[index][7][0] == 2:  # if inversion = 2
                    chordVec = [chordVec[0], chordVec[1], chordVec[3]]
                elif finalMTX[index][7][0] == 3:  # if inversion = 3
                    chordVec = [chordVec[0], chordVec[1], chordVec[2]]

        if num1 < 0.4:  # 40% chance to repeat note (technically less)
                        # because we check to see if prevNote is a chord tone)
            if ntp.numToPitch(prevNote) in chordVec:
                nextNote = prevNote
            else:
                nextNote = ptn.pitchToNum(chordVec[random.randint(0, len(chordVec) - 1)])
        elif num1 < 0.7:    # 30% chance to move up linearly (technically less than 30%,
                            # because we check to see if prevNote + 1 is a chord tone)
            if prevNote == 7:  # if prevNote is 7, can't use prevNote + 1
                if ntp.numToPitch(1) in chordVec:
                    nextNote = 1
                else:
                    nextNote = ptn.pitchToNum(chordVec[random.randint(0, len(chordVec) - 1)])
            else:  # if prevNote isn't 7, can use prevNote + 1
                if ntp.numToPitch(prevNote + 1) in chordVec:
                    nextNote = prevNote + 1
                else:
                    nextNote = ptn.pitchToNum(chordVec[random.randint(0, len(chordVec) - 1)])
        else:   # 30% chance to move down linearly (technically less than 30%,
                # because we check to see if prevNote - 1 is a chord tone)
            if prevNote == 1:  # if prevNote is 1, can't use prevNote - 1
                if ntp.numToPitch(7) in chordVec:
                    nextNote = 7
                else:
                    nextNote = ptn.pitchToNum(chordVec[random.randint(0, len(chordVec) - 1)])
            else:  # if prevNote isn't 1, can use prevNote - 1
                if ntp.numToPitch(prevNote - 1) in chordVec:
                    nextNote = prevNote - 1
                else:
                    nextNote = ptn.pitchToNum(chordVec[random.randint(0, len(chordVec) - 1)])

    #print(chordVec)
    return nextNote
