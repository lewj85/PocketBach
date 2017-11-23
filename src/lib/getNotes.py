from lib import defineChord as dc
from lib import pitchToNum as ptn
from lib import getRhythms as gr
from lib import musicObjects as mo
from lib import numToPitch as ntp
from lib import distanceToTonal as dtt
from lib import tonalToDistance as ttd
import random

#######################################################################
# getNotes()
#######################################################################
# returns notes, destination (of types: [Note class array], int)
# NOTE: destination is the 'distance' from 0-87, not pitch 0-7

# NOTES:
# can pass it any number of beats, but they must be over ONE chord
# useful for 2-beat cells as well as 4-beat phrases
# uses previousCell for episodes to match intervals/rhythms - if previousCell is None, it will create the first cell of the episode

def getNotes(currentChord, nextChord, beatsArr, start = None, destination = None, voice = 0, episode = False, previousCell = None, key = 'C', major = True, timesig = None):

    if not timesig:
        timesig = [4,4]


    # any measure where a voice first enters or re-enters after a rest and no start is specified
    if not start:
        # pick a random index from options
        options = dc.defineChord(None, currentChord)
        start = ptn.pitchToNum(random.choice(options[0]))
        # pick a distance based on voice
        startDistance = ttd.tonalToDistance(start, voice)
    else:
        # store distance
        startDistance = int(start)
        # convert start to 0-7
        pitch = dtt.distanceToTonal(startDistance)
        print('pitch is', pitch)
        start = ptn.pitchToNum(pitch)
        print('start is', start)


    if not destination:
        # pick a random destination
        options = dc.defineChord(None, nextChord)
        destination2 = random.choice(options[0])
        # pick a distance based on voice
        destDistance = ttd.tonalToDistance(destination2, voice)
        print('destDistance is', destDistance)
        destination = ptn.pitchToNum(destination2)
        print('destination, destination2:', destination, destination2)

    else:
        destDistance = int(destination)


    notes = []


    # calculate distance and direction
    distance = abs(start - destination)
    if startDistance < destDistance:
        direction = 1
    elif startDistance == destDistance:
        direction = 0
    else:
        direction = -1

    print('start: ' + str(start) + '\tdestination: ' + str(destination) + '\tdistance: ' + str(distance) + '\tdirection: ' + str(direction))


    #######################################################################
    # FOR NON-EPISODES
    #######################################################################

    if not episode:

        # call getRhythms to generate rhythms - this is now our number of notes needed
        rhythms = gr.getRhythms(beatsArr, timesig)

        # TODO: only give linear motion an 80% chance. 20% chance to move differently
        # if dist up or dist down is same as number of rhythms, and that distance is < 5
        if len(rhythms) == distance and direction > 1:
            print('numOfNotes == distance up. moving linearly.')
            nextNote = int(start)
            for note in rhythms:
                if nextNote == 8:
                    nextNote = 1
                notes.append(nextNote)
                nextNote += 1
        elif len(rhythms) == distance and direction < 1:
            print('numOfNotes == distance down. moving linearly.')
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
            rhythms = gr.getRhythms(beatsArr, timesig)

        # otherwise try to match intervals/rhythms from previousCell
        else:
            rhythms = previousCell[1]

    print('notes: ', notes)
    print('rhythms: ', rhythms)
    print('destination:', destination)

    # convert notes and rhythms to Note classes
    newNotes = []
    for i in range(len(notes)):
        tied = (rhythms[i][0][-1] == '.')
        if tied:
            rhythms[i][0] = rhythms[i][0][:-1]
        newNotes.append(mo.Note(ntp.numToPitch(notes[i]), ttd.tonalToDistance(ntp.numToPitch(notes[i])), int(rhythms[i][0]), tied, currentChord, 0, 0, 0, False, None, key, major, timesig))

    return newNotes, destination


# debugging
# notes, destination = getNotes(1, 4, range(4))
# allNotes = []
# allNotes.append(notes)
# notes, destination = getNotes(4, 5, range(2), destination)
# allNotes.append(notes)
# notes, destination = getNotes(5, 1, [2,3], destination)
# allNotes.append(notes)
# print(allNotes)
