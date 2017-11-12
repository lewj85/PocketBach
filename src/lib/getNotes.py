import random
import defineChord as dc
import pitchToNum as ptn
import getRhythms as gr


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
        rhythms = gr.getRhythms(beats, timesig)

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
            nextNote = int(start)
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
            rhythms = gr.getRhythms(beats, timesig)

        # otherwise try to match intervals/rhythms from previousCell
        else:
            rhythms = previousCell[1]
            pass

    print(notes)
    print(rhythms)
    print(destination)
    return notes, rhythms, destination


# debugging
notes, rhythms, destination = getNotes(1, 4, 4)
notes, rhythms, destination = getNotes(4, 5, 2, destination)
notes, rhythms, destination = getNotes(5, 1, 2, destination)
print(destination)
