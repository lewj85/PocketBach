# getNextNote() chooses the next note based on the previous note and current chord

import random
import numToPitch as ntp
import defineChord as dc

def getNextNote(prevNote=1, currentChord=1, nextChord=1, key='C', major=0, root=1,
                seventh=0, tonality=0, inversion=0, voice=0):
    # NOTE: need to add nextChord considerations!!
    #   especially for 7th chords because of 3rd inversion linear descents,
    #   but also for picking 2nd inversions, which should be rare if it isn't linear motion

    num1 = random.random()
    chordVec = dc.defineChord(key, major, root, seventh, tonality, inversion)

    # if bass line, high chance to pick root, even if there's a jump
    # NOTE: need to consider repeated pitches
    # NOTE: need to make it unlikely to pick 5th for 2nd inversion...
    if voice == 0:
        if num1 < 0.7:  # 70% chance to simply pick root
            nextNote = currentChord
        elif num1 < 0.85:   # 15% chance to move up linearly (technically less than 15%,
                            # because we check to see if prevNote + 1 is a chord tone)
            if prevNote == 7:  # if prevNote is 7, can't use prevNote + 1
                if ntp.numToPitch(1) in ntp.numToPitch(currentChord):
                    nextNote = 1
                else:  # otherwise just go with root
                    nextNote = currentChord
            else:  # if prevNote isn't 7, can use prevNote + 1
                if ntp.numToPitch(prevNote + 1) in ntp.numToPitch(currentChord):
                    nextNote = prevNote + 1
                else:  # otherwise just go with root
                    nextNote = currentChord
        else:   # 15% chance to move down linearly (technically less than 15%,
                # because we check to see if prevNote - 1 is a chord tone)
            if prevNote == 1:  # if prevNote is 1, can't use prevNote - 1
                if ntp.numToPitch(7) in ntp.numToPitch(currentChord):
                    nextNote = 7
                else:  # otherwise just go with root
                    nextNote = currentChord
            else:  # if prevNote isn't 1, can use prevNote - 1
                if ntp.numToPitch(prevNote - 1) in ntp.numToPitch(currentChord):
                    nextNote = prevNote - 1
                else:  # otherwise just go with root
                    nextNote = currentChord

    # if alto/tenor, high probability of repeating pitch,
    # equal probability to pick root, 3rd, or 5th
    # NOTE: need to check for note chosen in voice 0...
    #   consider passing the whole finalMTX with a cursor param
    elif voice == 1:
        if num1 < 0.75:  # 75% chance to repeat note if possible
            if ntp.numToPitch(prevNote) in ntp.numToPitch(currentChord):
                nextNote = prevNote
            else:
                if num1 < 0.25:
                    nextNote = chordVec[0]
                elif num1 < 0.5:
                    nextNote = chordVec[1]
                else:
                    nextNote = chordVec[2]
        # elif linear prevNote+1/-1 considerations? this section needs improvement
        else:
            if num1 < 0.85:  # 10% chance to pick root
                nextNote = chordVec[0]
            elif num1 < 0.95:  # 10% chance to pick 3rd
                nextNote = chordVec[1]
            else:  # 5% chance to pick 5th
                nextNote = chordVec[2]

    # if soprano, linear motion has highest probability
    # repeated notes should be unlikely (melody should have motion)
    # NOTE: need to check for note chosen in voices 0 and 1...
    #   consider passing the whole finalMTX with a cursor param
    else:
        if num1 < 0.2:  # 20% chance to repeat note (technically less)
            if ntp.numToPitch(prevNote) in ntp.numToPitch(currentChord):
                nextNote = prevNote
            else:
                if num1 < 0.5:  # 5% chance to pick root
                    nextNote = chordVec[0]
                elif num1 < 0.15:  # 10% chance to pick 3rd
                    nextNote = chordVec[1]
                else:  # 5% chance to pick 5th
                    nextNote = chordVec[2]
        elif num1 < 0.6:    # 40% chance to move up linearly (technically less than 40%,
                            # because we check to see if prevNote + 1 is a chord tone)
            if prevNote == 7:  # if prevNote is 7, can't use prevNote + 1
                if ntp.numToPitch(1) in ntp.numToPitch(currentChord):
                    nextNote = 1
                else:
                    if num1 < 0.3:  # 10% chance to pick root
                        nextNote = chordVec[0]
                    elif num1 < 0.5:  # 20% chance to pick 3rd
                        nextNote = chordVec[1]
                    else:  # 10% chance to pick 5th
                        nextNote = chordVec[2]
            else:  # if prevNote isn't 7, can use prevNote + 1
                if ntp.numToPitch(prevNote + 1) in ntp.numToPitch(currentChord):
                    nextNote = prevNote + 1
                else:
                    if num1 < 0.3:  # 10% chance to pick root
                        nextNote = chordVec[0]
                    elif num1 < 0.5:  # 20% chance to pick 3rd
                        nextNote = chordVec[1]
                    else:  # 10% chance to pick 5th
                        nextNote = chordVec[2]
        else:   # 40% chance to move down linearly (technically less than 40%,
                # because we check to see if prevNote - 1 is a chord tone)
            if prevNote == 1:  # if prevNote is 1, can't use prevNote - 1
                if ntp.numToPitch(7) in ntp.numToPitch(currentChord):
                    nextNote = 7
                else:
                    if num1 < 0.7:  # 10% chance to pick root
                        nextNote = chordVec[0]
                    elif num1 < 0.9:  # 20% chance to pick 3rd
                        nextNote = chordVec[1]
                    else:  # 10% chance to pick 5th
                        nextNote = chordVec[2]
            else:  # if prevNote isn't 1, can use prevNote - 1
                if ntp.numToPitch(prevNote - 1) in ntp.numToPitch(currentChord):
                    nextNote = prevNote - 1
                else:
                    if num1 < 0.7:  # 10% chance to pick root
                        nextNote = chordVec[0]
                    elif num1 < 0.9:  # 20% chance to pick 3rd
                        nextNote = chordVec[1]
                    else:  # 10% chance to pick 5th
                        nextNote = chordVec[2]

    return nextNote
