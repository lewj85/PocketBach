from lib import defineChord as dc
from lib import pitchToNum as ptn
from lib import getRhythms as gr
from lib import musicObjects as mo
from lib import tonalToPitch as ttp
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
        print('start:', startTonal, startPitch, startDistance)

    # if we are given a start
    else:

        # convert start to 0-7
        startPitch = dtp.distanceToPitch(startDistance)
        startTonal = ptn.pitchToNum(startPitch)
        print('start:', startTonal, startPitch, startDistance)


    # if no destination given, make one
    if not destinationDistance:

        # pick a random destination
        options = dc.defineChord(None, nextChord)
        destinationPitch = random.choice(options[0])
        destinationTonal = ptn.pitchToNum(destinationPitch)
        # pick a distance based on voice
        destinationDistance = ptd.pitchToDistance(destinationPitch, voice)
        print('destination:', destinationTonal, destinationPitch, destinationDistance)

    # if we are given a destination
    else:

        # convert destination to 0-7
        destinationPitch = dtp.distanceToPitch(destinationDistance)
        destinationTonal = ptn.pitchToNum(destinationPitch)
        print('destination:', destinationTonal, destinationPitch, destinationDistance)


    notes = []

    # calculate distance and direction
    if startDistance == destinationDistance:
        direction = 0
        distance = 0
    elif startDistance < destinationDistance:
        direction = 1
        distance = (destinationTonal - startTonal) % 7
    else:
        direction = -1
        distance = (startTonal - destinationTonal) % 7


    print('start: ' + str(startTonal) + '\tdestination: ' + str(destinationTonal) + '\tdistance: ' + str(distance) + '\tdirection: ' + str(direction))


    #######################################################################
    # FOR NON-EPISODES
    #######################################################################

    if not episode:

        num1 = random.random()
        #print(num1)

        #####################################################
        # LINEAR MOTION
        #####################################################

        # TODO: find good percentage. starting high for debugging
        # 80% chance to move linearly - technically less if distance is out of range
        # NOTE: tested these values with testGetRhythms.py
        if num1 < 0.8 and ( (len(beatsArr) == 4 and distance > 2 and distance < 9) or (len(beatsArr) == 2 and distance > 0 and distance < 8) ):

            # create rhythms with a length equal to distance
            # TODO: update and reuse randRhythm() from old getRhythm.py rather than rely on while loop... wasted cycles
            lenR = -1
            while lenR != distance:
                rhythms = gr.getRhythms(beatsArr, timesig)
                lenR = len(rhythms)

            #print('distance:', distance, '\tlenR:', lenR)

            # TODO: only give linear motion an X% chance. (100-X)% chance to move differently
            # if dist up or dist down is same as number of rhythms, and that distance is < 5
            if lenR == distance and direction == 1:
                nextNote = int(startTonal)
                for note in rhythms:
                    if nextNote == 8:
                        nextNote = 1
                    notes.append(nextNote)
                    nextNote += 1
            elif lenR == distance and direction == -1:
                # same as above in other direction
                nextNote = int(startTonal)
                for note in rhythms:
                    if nextNote == 0:
                        nextNote = 7
                    notes.append(nextNote)
                    nextNote -= 1
            else:
                print('error under linear motion in getNotes.py')


        #####################################################
        # COMMON PATTERNS
        #####################################################

        # elif num1 < 0.8

            # # repeated pitch patterns
            # elif abs(distance) == 0:
            #     pass

            # # 2nd jump patterns
            # elif abs(distance) == 1:
            #     pass

            # # 3rd jump patterns
            # elif abs(distance) == 2:
            #     pass

            # # 4th jump patterns
            # elif abs(distance) == 3:
            #     pass

            # # 5th jump patterns
            # elif abs(distance) == 4:
            #     pass

            # # 6th jump patterns
            # elif abs(distance) == 5:
            #     pass

            # # 7th jump patterns
            # elif abs(distance) == 6:
            #     pass

            # # octave jump patterns
            # elif abs(distance) == 7:
            #     pass

        #####################################################
        # MICRO-DESTINATION
        #####################################################

        else:

            # call getRhythms to generate rhythms - this is now our number of notes needed
            rhythms = gr.getRhythms(beatsArr, timesig)
            lenR = len(rhythms)

            # TODO: change this. don't just repeat.
            for note in rhythms:
                notes.append(startTonal)

            # check for accented beats after the first rhythm, create new micro-destinations
            # if len(beatsArr) > 2:
            #     for r in rhythms[1:]:
            #         if r[-1]:  # if accented
            #             # find a new micro-dest with a distance between startDistance and destinationDistance
            #             # move linearly if possible
            #             # else move be step
            #             pass

    #######################################################################
    # FOR EPISODES
    #######################################################################

    else:
        print('episode')

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
        fixedDistance = ptd.pitchToDistance(ttp.tonalToPitch(notes[i]), voice)
        if direction == -1:
            # if voice == blah, check bounds so distance doesn't go too far
            fixedDistance -= 12
        newNotes.append(mo.Note(ttp.tonalToPitch(notes[i]), fixedDistance, int(rhythms[i][0]), tied, currentChord, 0, 0, 0, False, None, key, major, timesig))

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
