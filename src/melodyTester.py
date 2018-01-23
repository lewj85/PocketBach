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
    # decision tree would know which elements are more important at each step (highest entropy)
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

    part1notes, microDestDistance = gnf.getNotesFugue(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[0]), beats12, startDistance, microDestDistance, tenor)
    part2notes, nextMeasureDestDistance = gnf.getNotesFugue(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats34, microDestDistance, nextMeasureDestDistance, tenor)
    notes = []
    for note in part1notes:
        notes.append(note)
    for note in part2notes:
        notes.append(note)
    finalMTX[0][tenor] = [mo.Cell(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, notes, nextMeasureDestDistance, tenor)]

    # TODO: continue from here. add measures 2 and 3


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
