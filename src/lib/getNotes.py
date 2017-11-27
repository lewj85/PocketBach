from lib import defineChord as dc
from lib import pitchToNum as ptn
from lib import getRhythms as gr
from lib import musicObjects as mo
from lib import numToPitch as ntp
from lib import distanceToPitch as dtp
from lib import distanceToTonal as dtt
from lib import pitchToDistance as ptd
import random

#######################################################################
# getNotes()
#######################################################################
# returns notes, destinationDistance (of types: [Note class array], int)
# NOTE: destinationDistance is the distance from 0-87, not destinationTonal from 0-7

# NOTES:
# can pass it any number of beats, but they must be over ONE chord
# useful for 2-beat cells as well as 4-beat cells
# uses previousCell for episodes to match intervals/rhythms - if previousCell is None, it will create the first cell of the episode

def getNotes(currentChord, nextChord, beatsArr, startDistance = None, destinationDistance = None, voice = 0, episode = False, previousCell = None, key = 'C', major = True, timesig = None):

    if timesig is None:
        timesig = [4,4]

    # any measure where a voice first enters or re-enters after a rest and no start is specified
    if not startDistance:

        # pick a random index from options
        options = dc.defineChord(None, currentChord)
        startPitch = random.choice(options[0])
        startTonal = ptn.pitchToNum(startPitch)
        # pick a distance based on voice
        startDistance = ptd.pitchToDistance(startPitch, voice)
        print('startDistance is', startDistance)
        print('start:', startTonal, startPitch)

    # if we are given a start
    else:

        # convert start to 0-7
        startPitch = dtp.distanceToPitch(startDistance)
        startTonal = ptn.pitchToNum(startPitch)
        print('startDistance is', startDistance)
        print('start:', startTonal, startPitch)


    # if no destination given, make one
    if not destinationDistance:

        # pick a random destination
        options = dc.defineChord(None, nextChord)
        destinationPitch = random.choice(options[0])
        destinationTonal = ptn.pitchToNum(destinationPitch)
        # pick a distance based on voice
        destinationDistance = ptd.pitchToDistance(destinationPitch, voice)
        print('destinationDistance is', destinationDistance)
        print('destination:', destinationTonal, destinationPitch)

    # if we are given a destination
    else:

        # convert destination to 0-7
        destinationPitch = dtp.distanceToPitch(destinationDistance)
        destinationTonal = ptn.pitchToNum(destinationPitch)
        print('destinationDistance is', destinationDistance)
        print('destination:', destinationTonal, destinationPitch)


    notes = []

    # calculate distance and direction
    distance = abs(startTonal - destinationTonal)
    if distance == 0:
        direction = 0
    elif startDistance < destinationDistance:
        direction = 1
    else:
        direction = -1

    print('start: ' + str(startTonal) + '\tdestination: ' + str(destinationTonal) + '\tdistance: ' + str(distance) + '\tdirection: ' + str(direction))


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
            nextNote = int(startTonal)
            for note in rhythms:
                if nextNote == 8:
                    nextNote = 1
                notes.append(nextNote)
                nextNote += 1
        elif len(rhythms) == distance and direction < 1:
            print('numOfNotes == distance down. moving linearly.')
            # same as above in other direction
            nextNote = int(startTonal)
            for note in rhythms:
                if nextNote == 0:
                    nextNote = 7
                notes.append(nextNote)
                nextNote -= 1
        # if dist up or dist down is NOT the same, do something else
        else:
            # TODO: change this. don't just repeat.
            for note in rhythms:
                notes.append(startTonal)


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


    #######################################################################
    # CONVERT TO MUSIC OBJECTS BEFORE RETURNING
    #######################################################################
    print('notes: ', notes)
    print('rhythms: ', rhythms)
    print('destinationDistance:', destinationDistance)

    # convert notes and rhythms to Note classes
    newNotes = []
    for i in range(len(notes)):
        tied = (rhythms[i][0][-1] == '.')
        if tied:
            rhythms[i][0] = rhythms[i][0][:-1]
        ##########################################################################
        # TODO: FIX DISTANCE BELOW! this is where you decide where to move
        ##########################################################################
        fixedDistance = ptd.pitchToDistance(ntp.numToPitch(notes[i]), voice)
        if direction == -1:
            # if voice == blah, check bounds so distance doesn't go too far
            fixedDistance -= 12
        newNotes.append(mo.Note(ntp.numToPitch(notes[i]), fixedDistance, int(rhythms[i][0]), tied, currentChord, 0, 0, 0, False, None, key, major, timesig))

    return newNotes, destinationDistance


# debugging
# notes, destination = getNotes(1, 4, range(4))
# allNotes = []
# allNotes.append(notes)
# notes, destination = getNotes(4, 5, range(2), destination)
# allNotes.append(notes)
# notes, destination = getNotes(5, 1, [2,3], destination)
# allNotes.append(notes)
# print(allNotes)
