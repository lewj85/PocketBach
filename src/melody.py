import random
import defineChord as dc


#######################################################################
# getNotes()
#######################################################################
# calls defineChord(), getRhythms()
# returns notes, rhythms

# NOTES:
# can pass it any number of beats, but they must be over ONE chord
# useful for 2-beat cells as well as 4-beat phrases
# uses previousCell for episodes to match intervals/rhythms - if previousCell is None, it will create the first cell of the episode

def getNotes(currentChord, nextChord, beats, start = None, destination = None, episode = False, previousCell = None, key = 'C', major = True, timesig = None):

    if not timesig:
        timesig = [4,4]

    # any measure where a voice first enters or re-enters after a rest
    if not start:
        options = dc.defineChord(key, major, currentChord)
        # pick a random index from options
        start = random.choice(options[0])

    if not destination:
        # pick a random destination
        options = dc.defineChord(key, major, nextChord)

    notes = []

    #######################################################################
    # FOR NON-EPISODES
    #######################################################################

    if not episode:

        # call getRhythms to generate rhythms - this is now our number of notes needed
        rhythms = getRhythms(beats, timesig)
        print(rhythms)


    #######################################################################
    # FOR EPISODES
    #######################################################################

    else:

        # if previousCell is None, it's the first cell of the episode
        if not previousCell:
            rhythms = getRhythms(beats, timesig)

        # otherwise try to match intervals/rhythms from previousCell
        else:
            rhythms = previousCell[1]
            pass

    return notes, rhythms



#######################################################################
# getRhythms()
#######################################################################
# calls nothing
# returns rhythms

# NOTES:
# generates beats randomly using random.choice() until the beat total matches totalBeats parameter

def getRhythms(totalBeats, timesig = None):

    if not timesig:
        timesig = [4,4]

    # NOTE: removed whole notes
    optionsArr = [['2.', 3], ['2', 2], ['4.', 1.5], ['4', 1], ['8.', 0.75], ['8', 0.5], ['16', 0.25]]
    optionsDict = {
        '2.': 3,
        '2': 2,
        '4.': 1.5,
        '4': 1,
        '8.': 0.75,
        '8': 0.5,
        '16': 0.25
        }

    rhythms = []
    total = 0

    while total < totalBeats:
        downbeat = 0
        accented = 0
        if total == int(total):
            downbeat = 1
        if total == 0 or total == 2:
            accented = 1
        if rhythms:
            if rhythms[-1][0] == '4.' or (rhythms[-1][0] == '8' and not downbeat):
                rhythms.append(random.choice([['8', int(total) + 1, downbeat, accented], ['16', int(total) + 1, downbeat, accented]]))
            elif rhythms[-1][0] == '8.' or (rhythms[-1][0] == '16' and not downbeat):
                rhythms.append(['16', int(total)+1, downbeat, accented])
            elif not accented:
                rhythms.append(random.choice([['4', int(total) + 1, downbeat, accented], ['8', int(total) + 1, downbeat, accented], ['16', int(total) + 1, downbeat, accented]]))
            else:
                rhythms.append([random.choice(optionsArr)[0], int(total) + 1, downbeat, accented])
        else:
            rhythms.append([random.choice(optionsArr)[0], int(total) + 1, downbeat, accented])

        total += optionsDict[rhythms[-1][0]]

        # if you went beyond totalBeats, replace last value
        if total > totalBeats:
            total -= optionsDict[rhythms[-1][0]]
            rhythms.pop()

    #print(total)
    #print(rhythms)
    return rhythms


# debugging
getNotes(1, 4, 4)
