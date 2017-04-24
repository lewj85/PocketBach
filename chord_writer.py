# Chord Writer
# Jesse Lew
# This program takes chords from input and appends appropriate chords to it.

import random

# getNextChord chooses which chord should be next based on the number of
# chords remaining, the destination chord, and various weights. it makes
# use of the random() function when there are multiple options.
# NOTE: rearrange if statements so destination is outer if-else
def getNextChord(chordsRemaining, destination, previousChord):
    if chordsRemaining == 1:      # if on last chord
        if destination == 1:      # if destination is tonic I
            return 5              # return dominant V
        elif destination == 5:    # if destination is dominant V
            num1 = random.random()
            if num1 < 0.5:        # return random predominant ii or IV
                return 4
            else:
                return 2
        elif destination == 4:    # if destination is IV
            return 1              # return V/IV, which is I
        else:
            num1 = random.random()
            if num1 < 0.4:  # 40% chance to move up a fourth
                newChord = previousChord + 3
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            elif num1 < 0.6:  # 20% chance to move up a sixth
                newChord = previousChord + 5
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            elif num1 < 0.75:  # 15% chance to move up a fifth
                newChord = previousChord + 4
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            elif num1 < 0.85:  # 10% chance to move up a second
                newChord = previousChord + 1
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            elif num1 < 0.9:  # 5% chance to move up a third
                newChord = previousChord + 2
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            elif num1 < 0.95:  # 5% chance to move up a seventh
                newChord = previousChord + 6
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            else:  # 5% chance to stay the same
                newChord = previousChord
                return newChord
    elif chordsRemaining == 2:    # if on second to last chord
        if destination == 1:      # if destination is tonic I
            num1 = random.random()
            if num1 < 0.5:        # return random predominant ii or IV
                return 4
            else:
                return 2
        elif destination == 5:
            num1 = random.random()
            # return random predominant ii/V or IV/V, which is vi or I
            # NOTE: need to consider previous chord to prevent repeating
            # chords. it's allowable, but weights will make it uncommon
            if previousChord == 1:
                if num1 < 0.1:    # only 10% chance to repeat
                    return 1
                else:
                    return 6
            elif previousChord == 6:
                if num1 < 0.1:    # only 10% chance to repeat
                    return 6
                else:
                    return 1
            else:
                if num1 < 0.5:    # otherwise normal 50% chance to return
                    return 6      # ii/V or IV/V (vi or I)
                else:
                    return 1
        elif previousChord == 4:
            num1 = random.random()
            if num1 < 0.8:        # 80% chance to be V
                return 5
            else:
                return 1
        else:
            num1 = random.random()
            if num1 < 0.4:  # 40% chance to move up a fourth
                newChord = previousChord + 3
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            elif num1 < 0.6:  # 20% chance to move up a sixth
                newChord = previousChord + 5
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            elif num1 < 0.75:  # 15% chance to move up a fifth
                newChord = previousChord + 4
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            elif num1 < 0.85:  # 10% chance to move up a second
                newChord = previousChord + 1
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            elif num1 < 0.9:  # 5% chance to move up a third
                newChord = previousChord + 2
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            elif num1 < 0.95:  # 5% chance to move up a seventh
                newChord = previousChord + 6
                while newChord > 7:  # bring newChord range down to 1-7
                    newChord -= 7
                return newChord
            else:  # 5% chance to stay the same
                newChord = previousChord
                return newChord
    else:
        num1 = random.random()    # return a random chord with specific weights
        # NOTE: these weights should be adjusted based on composer profile data
        # NOTE: this section should be rewritten with weights based on previous
        # chord. ie. if previousChord == 1, 44% chance to go up a fourth, but
        # if previousChord == 5, 62% chance to go up a fourth
        if num1 < 0.4:            # 40% chance to move up a fourth
            newChord = previousChord + 3
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        elif num1 < 0.6:          # 20% chance to move up a sixth
            newChord = previousChord + 5
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        elif num1 < 0.75:         # 15% chance to move up a fifth
            newChord = previousChord + 4
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        elif num1 < 0.85:         # 10% chance to move up a second
            newChord = previousChord + 1
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        elif num1 < 0.9:          # 5% chance to move up a third
            newChord = previousChord + 2
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        elif num1 < 0.95:         # 5% chance to move up a seventh
            newChord = previousChord + 6
            while newChord > 7:   # bring newChord range down to 1-7
                newChord -= 7
            return newChord
        else:                     # 5% chance to stay the same
            newChord = previousChord
            return newChord

