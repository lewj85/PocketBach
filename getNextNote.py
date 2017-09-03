# getNextNote() chooses the next note based on the previous note and current chord

import random
import numToPitch as ntp

def getNextNote(prevNote=1, currentChord=1, nextChord=1, seventhChord=0, voice=0):
    # NOTE: need to add nextChord considerations!!
    #   especially for 7th chords because of 3rd inversion linear descents,
    #   but also for picking 2nd inversions, which should be rare if it isn't linear motion

    num1 = random.random()

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
    elif voice == 1:
        pass

    # if soprano, linear motion has highest probability
    # repeated notes should be unlikely (melody should have motion)
    else:
        pass


    return nextNote
