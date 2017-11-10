import random
import defineChord as dc
import pitchToNum as ptn


#######################################################################
# getNotes()
#######################################################################
# calls defineChord(), getRhythms()
# returns notes, rhythms, destination

# NOTES:
# can pass it any number of beats, but they must be over ONE chord
# useful for 2-beat cells as well as 4-beat phrases
# uses previousCell for episodes to match intervals/rhythms - if previousCell is None, it will create the first cell of the episode

def getNotes(currentChord, nextChord, beats, start = None, destination = None, episode = False, rhythms = None, key = 'C', major = True, timesig = None):

    if not timesig:

        timesig = [4,4]


    # any measure where a voice first enters or re-enters after a rest and no start is specified
    if not start:

        # pick a random index from options
        options = dc.defineChord(None, currentChord)
        start = ptn.pitchToNum(random.choice(options[0]))


    if not destination:

        # pick a random destination
        options = dc.defineChord(None, nextChord)
        destination = ptn.pitchToNum(random.choice(options[0]))

        # TODO: direction and distance are important to prevent voice crossing. pass voice as param and pick destination's '88-value'.
        #    this will set a direction for use below, so remove distToUp and distToDown below.


    notes = []


    # store distance to destination both up and down
    distToDestUp = 0
    note = int(start)
    while note != destination:
        distToDestUp += 1
        note += 1
        # wrap around
        if note == 8:
            note = 1
    distToDestDown = 7 - distToDestUp


    print('start: ' + str(start) + '\tdestination: ' + str(destination) + '\tdistToDestUp: ' + str(distToDestUp) + '\tdistToDestDown: ' + str(distToDestDown))


    #######################################################################
    # FOR NON-EPISODES
    #######################################################################

    if not episode:

        # call getRhythms to generate rhythms - this is now our number of notes needed
        rhythms = getRhythms(beats, timesig)

        # TODO: only give linear motion an 80% chance. 20% chance to move differently
        # if dist up or dist down is same as number of rhythms, and that distance is < 5
        if len(rhythms) == distToDestUp and distToDestUp < 5:
            print('numOfNotes == distToDestUp. moving linearly.')
            nextNote = int(start)
            for note in rhythms:
                if nextNote == 8:
                    nextNote = 1
                notes.append(nextNote)
                nextNote += 1
        elif len(rhythms) == distToDestDown and distToDestDown < 5:
            print('numOfNotes == distToDestDown. moving linearly.')
            # same as above in other direction
            nextNote = start - 1
            for note in rhythms:
                if nextNote == 0:
                    nextNote = 7
                notes.append(nextNote)
                nextNote -= 1
        # if dist up or dist down is NOT the same, do something else
        else:
            # TODO: change this. don't just repeat.
            for note in rhythms:
                notes.append(start)


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

    print(notes)
    print(rhythms)
    print(destination)
    return notes, rhythms, destination



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

    # NOTE: removed whole notes and dotted half notes
    optionsArr = [['2', 2], ['4.', 1.5], ['4', 1], ['8.', 0.75], ['8', 0.5], ['16', 0.25]]
    optionsDict = {
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
            # remove certain rhythmic options based on previous rhythm selected
            if rhythms[-1][0] == '4.':  # must be an 8th
                rhythms.append(['8', int(total) + 1, downbeat, accented])
            elif rhythms[-1][0] == '8' and not downbeat:  # only allow 8th and 16ths
                rhythms.append(random.choice([['8', int(total) + 1, downbeat, accented], ['16', int(total) + 1, downbeat, accented]]))
            elif rhythms[-1][0] == '8.' or (rhythms[-1][0] == '16' and not downbeat):  # must be a 16th
                rhythms.append(['16', int(total)+1, downbeat, accented])
            elif not accented:  # remove half note and dotted rhythms
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

        # force 'rhythmic diversity' and rewrite measures with too many rhythms
        onlyRhythms = [a for a,b,c,d in rhythms]
        if len(rhythms) > 7 or onlyRhythms.count('2') > 1 or onlyRhythms.count('4') > 3 or onlyRhythms.count('8') > 4 or onlyRhythms.count('16') > 6:
            rhythms = []
            total = 0


    #print(total)
    #print(rhythms)
    return rhythms


# debugging
notes, rhythms, destination = getNotes(1, 4, 4)
notes, rhythms, destination = getNotes(4, 5, 2, destination)
notes, rhythms, destination = getNotes(5, 1, 2, destination)
print(destination)
