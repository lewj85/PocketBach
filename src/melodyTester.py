from lib import createLily as cl
from lib import createXML as cx
from lib import getNotesFugue as gnf
from lib import musicObjects as mo
from lib import pitchToDistance as ptd
from lib import distanceToPitch as dtp
from lib import transposeCellDiatonically as tcd
from lib import getMicroDestination as gmd
from lib import distanceToTonal as dtt
import numpy as np
import random


# writes melodies for testing
def melodyTester(subjectMTX = None, music = None):

    if music is None:
        music = mo.Music()

    # initialize variables
    measures = 3 # TODO: update to number of measures that have been finished - 32 total
    beats1234 = [1, 2, 3, 4]
    beats12 = [1, 2]
    beats34 = [3, 4]
    maxVoices = 3
    bass = 0
    tenor = 1
    soprano = 2

    # create finalMTX - a 2D array of 1D arrays (lists) of Cells - because each measure can hold 1-4 Cells
    finalMTX = np.empty((measures, maxVoices), dtype=object)

    # Hard-coding to I-IV-V for testing
    destinationChords = [1,4,5]

    # fill bass and soprano with rests
    finalMTX[0][bass] = [mo.Cell(destinationChords[0], destinationChords[1], beats1234, [mo.Note('r', 88, 1, False, 1)], None, bass)]
    finalMTX[1][bass] = [mo.Cell(destinationChords[1], destinationChords[2], beats1234, [mo.Note('r', 88, 1, False, 1)], None, bass)]
    finalMTX[1][bass] = [mo.Cell(destinationChords[2], destinationChords[0], beats1234, [mo.Note('r', 88, 1, False, 1)], None, bass)]
    finalMTX[0][soprano] = [mo.Cell(destinationChords[0], destinationChords[1], beats1234, [mo.Note('r', 88, 1, False, 1)], None, soprano)]
    finalMTX[1][soprano] = [mo.Cell(destinationChords[1], destinationChords[2], beats1234, [mo.Note('r', 88, 1, False, 1)], None, soprano)]
    finalMTX[1][soprano] = [mo.Cell(destinationChords[2], destinationChords[0], beats1234, [mo.Note('r', 88, 1, False, 1)], None, soprano)]
    
    # notes, destinationTenor = gnf.getNotesFugue(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, ptd.pitchToDistance(music.key), None, tenor)  # NOTE: starting with root of key
    # print('destinationTenor', destinationTenor, dtp.distanceToPitch(destinationTenor))
    # finalMTX[0][tenor] = [mo.Cell(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, notes, destinationTenor, tenor)]
    # notes, destinationTenor = gnf.getNotesFugue(mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), beats1234, destinationTenor, None, tenor)  # NOTE: starting with root of key
    # print('destinationTenor', destinationTenor, dtp.distanceToPitch(destinationTenor))
    # finalMTX[1][tenor] = [mo.Cell(mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), beats1234, notes, destinationTenor, tenor)]
    # finalMTX[2][tenor] = [mo.Cell(mo.Chord(destinationChords[2]), mo.Chord(1), beats1234, [mo.Note(dtp.distanceToPitch(destinationTenor), destinationTenor, 1, False, 5)], destinationTenor, tenor)]


    # notes
    # using a bunch of melodies: train a neural network? create a decision tree? many options, but leaning toward decision tree with weighted probability
    # decision tree would know which elements are more important at each step (highest information gain using entropy)
    # ie. is linear motion more important than microdestinations landing on a chord tone on an accented beat?
    # ie. is following intervallic/rhythmic repetition more important than landing on a chord tone in the next measure?
    # ie. if landing on a chord tone is more important, then should we change the rhythm or the interval?
    # goal is to avoid landing on non-chord tone on accented beats often, but not always
    # one way to achieve this goal: use microdestinations a large percentage of the time
    # note that microdestinations don't always need to occur directly on the accented beat (ie. suspension), but would still be used
    # question: when should non-chord tones be used? is it truly random or are there times when a suspension is more likely? measure 1-2 vs 2-3, beat 2-3 vs 4-1, V-vi vs V-I, etc

    print('MEASURE 1')
    startDistance = ptd.pitchToDistance(music.key)
    direction = random.choice([1,-1])
    # first use getMicroDestination() to pick destination for next measure
    nextMeasureDestTonal, nextMeasureDestDistance, nextMeasureDestPitch = gmd.getMicroDestination(mo.Chord(destinationChords[1]), startDistance, direction)
    # make sure distance is within range of the voice - testing tenor, so keep from 32-48 in key of C
    while nextMeasureDestDistance > 48:
        nextMeasureDestDistance -= 12
        # direction may have changed
        if startDistance == nextMeasureDestDistance:
            direction = 0
        elif startDistance > nextMeasureDestDistance:
            direction = -1
        else:
            direction = 1
    while nextMeasureDestDistance < 32:
        nextMeasureDestDistance += 12
        # direction may have changed
        if startDistance == nextMeasureDestDistance:
            direction = 0
        elif startDistance > nextMeasureDestDistance:
            direction = -1
        else:
            direction = 1
    print('startDistance', startDistance, dtt.distanceToTonal(startDistance), '\tdirection', direction, '\tnextMeasureDestDistance', nextMeasureDestDistance, nextMeasureDestTonal)

    # use getMicroDestination() again, this time within the measure
    microDestTonal, microDestDistance, microDestPitch = gmd.getMicroDestination(mo.Chord(destinationChords[0]), startDistance, direction)

    # we now have the startDistance, microDestDistance, and nextMeasureDestDistance
    # TODO: test melody-creation here and add final result to getNotesFugue()

    # part1notes, microDestDistance = gnf.getNotesFugue(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[0]), beats12, startDistance, microDestDistance, tenor)
    # part2notes, nextMeasureDestDistance = gnf.getNotesFugue(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats34, microDestDistance, nextMeasureDestDistance, tenor)
    # notes = []
    # for note in part1notes:
    #     notes.append(note)
    # for note in part2notes:
    #     notes.append(note)
    # finalMTX[0][tenor] = [mo.Cell(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, notes, nextMeasureDestDistance, tenor)]

    # first pick a rhythm for beats [1 2]
    rhythmOptions = [
        # 1 note
        ['2'],
        # 2 notes
        ['4.', '8'], ['4', '4'], ['8', '4.'],
        # 3 notes
        ['4.', '16', '16'], ['4', '8.', '16'], ['4', '8', '8'], ['8.', '16', '4'], ['8', '8~', '8', '8'], ['8', '8', '4'],
        # ['4~', '16', '8', '16'], ['4~', '16', '16', '8'], ['16', '8.', '4'],
        # 4 notes
        ['4~', '16', '16', '16', '16'], ['4', '8', '16', '16'], ['4', '16', '8', '16'], ['4', '16', '16', '8'],
        ['8.', '16', '8.', '16'], ['8.', '16', '8', '8'], ['8', '8', '8.', '16'],
        ['8', '8~', '8', '16', '16'], ['8', '8', '8', '8'], ['8', '16', '16', '4'],
        ['16', '8', '16', '4'], ['16', '16', '8', '4'],
        # ['16', '8.', '8.', '16'], ['16', '8.', '8', '8'], ['16', '8.', '16', '8.'], ['8.', '16', '16', '8.'], ['8', '8', '16', '8.'],
        # 5 notes
        ['4', '16', '16', '16', '16'], ['8.', '16', '8', '16', '16'], ['8.', '16', '16', '8', '16'], ['8.', '16', '16', '16', '8'],
        ['8', '8~', '16', '16', '16', '16'], ['8', '8', '8', '16', '16'], ['8', '8', '16', '8', '16'], ['8', '8', '16', '16', '8'],
        ['8', '16', '16~', '16', '16', '8'], ['8', '16', '16', '8.', '16'], ['8', '16', '16', '8', '8'],
        ['16', '16', '8~', '8', '16', '16'], ['16', '16', '8~', '16', '8', '16'], ['16', '16', '8~', '16', '16', '8'],
        ['16', '16', '8', '8.', '16'], ['16', '16', '8', '8', '8'],
        # 6 notes
        ['8.', '16', '16', '16', '16', '16'], ['8', '8', '16', '16', '16', '16'], ['8', '16', '16~', '16', '16', '16', '16'],
        ['8', '16', '16', '8', '16', '16'], ['8', '16', '16', '16', '8', '16'], ['8', '16', '16', '16', '16', '8'],
        ['16', '8', '16~', '16', '16', '16', '16'], ['16', '8', '16', '8', '16', '16'],
        ['16', '8', '16', '16', '8', '16'], ['16', '8', '16', '16', '16', '8'], ['16', '16', '8~', '16', '16', '16', '16'],
        ['16', '16', '8', '8', '16', '16'], ['16', '16', '8', '16', '8', '16'], ['16', '16', '8', '16', '16', '8'],
        ['16', '16', '16', '16~', '16', '8', '16'], ['16', '16', '16', '16~', '16', '16', '8'],
        ['16', '16', '16', '16', '8.', '16'], ['16', '16', '16', '16', '8', '8'],
        # ['16', '8.', '16', '16', '16', '16'], ['16', '16', '16', '16', '16', '8.'],
        # 7 notes
        ['8', '16', '16', '16', '16', '16', '16'], ['16', '8', '16', '16', '16', '16', '16'],
        ['16', '16', '8', '16', '16', '16', '16'], ['16', '16', '16', '16~', '16', '16', '16', '16'],
        ['16', '16', '16', '16', '8', '16', '16'], ['16', '16', '16', '16', '16', '8', '16'],
        ['16', '16', '16', '16', '16', '16', '8'],
        # 8 notes
        # ['16', '16', '16', '16', '16', '16', '16', '16']
    ]

    # get random rhythms. check for # of them to prevent too many/few notes
    # make sure there's at least 1 'long' note (half, dotted quarter, tied quarter, or quarter)
    counter = 0
    longNotes = 0
    while (counter > 10 or counter < 3) or (longNotes == 0):
        rhythm12 = random.choice(rhythmOptions)
        rhythm34 = random.choice(rhythmOptions)
        counter = 0
        longNotes = 0
        for i in rhythm12:
            counter += 1
            if i == '2' or i == '4.' or i == '4~' or i == '4':
                longNotes += 1
        for i in rhythm34:
            counter += 1
            if i == '2' or i == '4.' or i == '4~' or i == '4':
                longNotes += 1
        #print(longNotes)

    #print(rhythm12, rhythm34)

    # count notes to microdestinations and combine rhythms
    rhythms = []
    counter12 = 0
    counter34 = 0
    for i in rhythm12:
        rhythms.append(i)
        counter12 += 1
    for i in rhythm34:
        rhythms.append(i)
        counter34 += 1
    print(rhythms)

    # calculate distance and direction
    startTonal = dtt.distanceToTonal(startDistance)
    if startDistance == microDestDistance:
        direction = 0
        distanceBetweenTonal = 0
    elif startDistance < microDestDistance:
        direction = 1
        if startTonal < microDestTonal: # 1 to 7 = 7 - 1 = 6, 3 to 5 = 5 - 3 = 2
            distanceBetweenTonal = max(microDestTonal, startTonal) - min(microDestTonal, startTonal)
        else: # 7 to 1 = 1 - 7 + 7 = 1, 5 to 3 = 3 - 5 + 7 = 5
            distanceBetweenTonal = min(microDestTonal, startTonal) - max(microDestTonal, startTonal) + 7
    else:
        direction = -1
        if startTonal < microDestTonal: # 1 to 7 = 1 - 7 + 7 = 1, 3 to 5 = 3 - 5 + 7 = 5
            distanceBetweenTonal = min(microDestTonal, startTonal) - max(microDestTonal, startTonal) + 7
        else: # 7 to 1 = 7 - 1 = 6, 5 to 3 = 5 - 3 = 2
            distanceBetweenTonal = max(microDestTonal, startTonal) - min(microDestTonal, startTonal)

    # 50% chance to pick a common pattern
    num1 = random.random()
    if num1 < .5:
        if counter12 == distanceBetweenTonal:
            # move linearly
            pass
        elif counter12 == distanceBetweenTonal + 1:
            pass
        elif counter12 == distanceBetweenTonal + 2:
            pass
        elif counter12 == distanceBetweenTonal + 3:
            pass
        else:
            # just do random
        pass
    # otherwise just move randomly
    else:
        if rhythm12[-1] == '16':
            # make sure it moves linearly
            if rhythm12[-2] == '16':
                # make sure both move linearly
                pass
            pass
        num2 = random.random()
        # the shorter the rhythm, the higher the chance to move linearly


    # TODO: continue from here





    # TODO: add measures 2 and 3
    # small percent chance to reuse a rhythm from measure 1
    num1 = random.random()
    if num1 < .1:
        # reuse rhythm12
        pass
    elif num1 < .2:
        # reuse rhythm34
        pass
    elif num1 < .25:
        # reuse both rhythm12 and rhythm34
        pass
    else:
        # pick random rhythms
        pass

    #####################################################################
    # CREATE FILES: .ly, .xml
    #####################################################################
    #cl.createLily(music.key, music.major, finalMTX, measures, maxVoices)  # commented out while fugueWriter is being written
    # cl.createLily(key, major, finalMTX, measures, maxVoices, 2)  # second species
    # TO DO: add other species
    # not using regex so don't need this anymore, keeping for legacy
    # copyfile('newScore.ly','newScore2.ly')


    # create the pdf score
    print("Creating .pdf file(s) with LilyPond...")
    filename = "Melody.ly"
    #os.system(filename)  # commented out while fugueWriter is being written
    # time.sleep(3)

    # create the xml file
    print("Creating .xml file(s)...")
    filename = "Melody.xml"
    cx.createXML(filename, music.key, music.major, music.timesig, finalMTX, measures, maxVoices, "piano")  # note "piano" to avoid .xml organ problems with tenor = 0


# debugging
print('Melody Tester - by Jesse Lew')
melodyTester()
