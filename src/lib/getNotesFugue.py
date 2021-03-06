from lib import defineChord as dc
from lib import getRhythmsFugue as grf
from lib import musicObjects as mo
from lib import tonalToDistance as ttd
from lib import tonalToPitch as ttp
from lib import distanceToPitch as dtp
from lib import distanceToTonal as dtt
from lib import pitchToDistance as ptd
from lib import pitchToTonal as ptt
from lib import getMicroDestination as gmd
import random

#######################################################################
# getNotesFugue()
#######################################################################
# returns notes, destinationDistance (of types: [Note class array], int)
# NOTE: destinationDistance is the distance from 0-87, not destinationTonal from 0-7

# NOTES:
# can pass it any number of beats, but they must be over ONE chord
# useful for 2-beat cells as well as 4-beat cells
# uses previousCell for episodes to match intervals/rhythms - if previousCell is None, it will create the first cell of the episode

# currentChord and nextChord params are now mo.Chord objects
def getNotesFugue(currentChord, nextChord, beatsArr, startDistance = None, destinationDistance = None, voice = 0, episode = False, previousCell = None, key = 'c', major = True, timesig = None):

    if timesig is None:
        timesig = [4,4]

    # any measure where a voice first enters or re-enters after a rest and no start is specified
    if not startDistance:

        # pick a random index from options
        options = dc.defineChord(currentChord)
        startPitch = random.choice(options[0])
        startTonal = ptt.pitchToTonal(startPitch)
        # pick a distance based on voice
        startDistance = ptd.pitchToDistance(startPitch, voice)
        #print('start:', startTonal, startPitch, startDistance)

    # if we are given a start
    else:

        # convert start to 0-7
        startPitch = dtp.distanceToPitch(startDistance)
        startTonal = ptt.pitchToTonal(startPitch)
        #print('start:', startTonal, startPitch, startDistance)


    # if no destination given, make one
    if not destinationDistance:

        # pick a random destination
        options = dc.defineChord(nextChord)
        destinationPitch = random.choice(options[0])
        destinationTonal = ptt.pitchToTonal(destinationPitch)
        # pick a distance based on voice
        destinationDistance = ptd.pitchToDistance(destinationPitch, voice)
        #print('destination:', destinationTonal, destinationPitch, destinationDistance)

    # if we are given a destination
    else:

        # convert destination to 0-7
        destinationPitch = dtp.distanceToPitch(destinationDistance)
        destinationTonal = ptt.pitchToTonal(destinationPitch)
        #print('destination:', destinationTonal, destinationPitch, destinationDistance)


    notes = []

    # calculate distance and direction
    if startDistance == destinationDistance:
        direction = 0
        distanceBetweenTonal = 0
    elif startDistance < destinationDistance:
        direction = 1
        if startTonal < destinationTonal: # 1 to 7 = 7 - 1 = 6, 3 to 5 = 5 - 3 = 2
            distanceBetweenTonal = max(destinationTonal, startTonal) - min(destinationTonal, startTonal)
        else: # 7 to 1 = 1 - 7 + 7 = 1, 5 to 3 = 3 - 5 + 7 = 5
            distanceBetweenTonal = min(destinationTonal, startTonal) - max(destinationTonal, startTonal) + 7
    else:
        direction = -1
        if startTonal < destinationTonal: # 1 to 7 = 1 - 7 + 7 = 1, 3 to 5 = 3 - 5 + 7 = 5
            distanceBetweenTonal = min(destinationTonal, startTonal) - max(destinationTonal, startTonal) + 7
        else: # 7 to 1 = 7 - 1 = 6, 5 to 3 = 5 - 3 = 2
            distanceBetweenTonal = max(destinationTonal, startTonal) - min(destinationTonal, startTonal)


    print('start: ' + str(startTonal) + '\tdestination: ' + str(destinationTonal) + '\tdistanceBetweenTonal: ' + str(distanceBetweenTonal) + '\tdirection: ' + str(direction))


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
        if num1 < 0.8 and ( (len(beatsArr) == 4 and distanceBetweenTonal > 2 and distanceBetweenTonal < 9) or (len(beatsArr) == 2 and distanceBetweenTonal > 0 and distanceBetweenTonal < 8) ):

            # create rhythms with a length equal to distance
            # TODO: update and reuse randRhythm() from old getRhythmsChorale.py rather than rely on while loop... wasted cycles
            lenR = -1
            while lenR != distanceBetweenTonal:
                rhythms = grf.getRhythmsFugue(beatsArr, timesig)
                lenR = len(rhythms)

            #print('distance:', distance, '\tlenR:', lenR)

            # TODO: only give linear motion an X% chance. (100-X)% chance to move differently
            # if dist up or dist down is same as number of rhythms, and that distance is < 5
            if lenR == distanceBetweenTonal and direction == 1:
                nextNote = int(startTonal)
                for note in rhythms:
                    if nextNote == 8:
                        nextNote = 1
                    notes.append(nextNote)
                    nextNote += 1
            elif lenR == distanceBetweenTonal and direction == -1:
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

            # call getRhythmsFugue to generate rhythms - this is now our number of notes needed
            rhythms = grf.getRhythmsFugue(beatsArr, timesig)
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
            #             microDestinationTonal, x, y = gmd.getMicroDestination(currentChord, startDistance, direction)
            #         else:
            #             pass

    #######################################################################
    # FOR EPISODES
    #######################################################################

    else:
        #print('episode')

        # if previousCell is None, it's the first cell of the episode
        if not previousCell:
            rhythms = grf.getRhythmsFugue(beatsArr, timesig)

            # TODO: change this. don't just repeat.
            for note in rhythms:
                notes.append(startTonal)

        # otherwise try to match intervals/rhythms from previousCell
        else:
            rhythms = grf.addRhythmData(previousCell.notes)

            # TODO: change this. don't just repeat.
            for note in rhythms:
                notes.append(startTonal)



    #######################################################################
    # CONVERT TO MUSIC OBJECTS BEFORE RETURNING
    #######################################################################
    #print('notes: ', notes)
    #print('rhythms: ', rhythms)
    #print('destinationDistance:', destinationDistance)

    # convert notes and rhythms to Note classes
    newNotes = []
    for i in range(len(notes)):
        tied = (rhythms[i][0][-1] == '.')
        if tied:
            rhythms[i][0] = rhythms[i][0][:-1]
        ##########################################################################
        # TODO: FIX DISTANCE BELOW! this is where you decide where to move
        ##########################################################################
        if i == 0:
            fixedDistance = int(startDistance)
        else:
            # no octave jumps yet, so this fixes the repeated note problem
            if notes[i] == notes[i-1]:
                fixedDistance = ttd.tonalToDistance(notes[i], 0, fixedDistance)
            else:
                fixedDistance = ttd.tonalToDistance(notes[i], direction, fixedDistance)
                # check range
                if newNotes[-1].distance > fixedDistance and (newNotes[-1].distance - fixedDistance) > 9:
                    fixedDistance += 12
                elif newNotes[-1].distance < fixedDistance and (fixedDistance - newNotes[-1].distance) > 9:
                    fixedDistance += 12
        # if voice == blah, check bounds so distance doesn't go too far
        newNotes.append(mo.Note(ttp.tonalToPitch(notes[i]), fixedDistance, int(rhythms[i][0]), tied, currentChord.root,
                                currentChord.tonality, currentChord.seventh, currentChord.inversion, currentChord.secondary,
                                currentChord.secondaryRoot, key, major, timesig))

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
