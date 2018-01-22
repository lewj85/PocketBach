from lib import createLily as cl
from lib import createXML as cx
from lib import getNotesFugue as gnf
from lib import musicObjects as mo
from lib import pitchToDistance as ptd
from lib import distanceToPitch as dtp
from lib import transposeCellDiatonically as tcd
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
    maxVoices = 1
    tenor = 0

    # create finalMTX - a 2D array of 1D arrays (lists) of Cells - because each measure can hold 1-4 Cells
    finalMTX = np.empty((measures, maxVoices), dtype=object)

    # Hard-coding to I-IV-V for testing
    destinationChords = [1,4,5]
    notes, destinationTenor = gnf.getNotesFugue(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, ptd.pitchToDistance(music.key), None, tenor)  # NOTE: starting with root of key
    print('destinationTenor', destinationTenor, dtp.distanceToPitch(destinationTenor))
    finalMTX[0][tenor] = [mo.Cell(mo.Chord(destinationChords[0]), mo.Chord(destinationChords[1]), beats1234, notes, destinationTenor, tenor)]
    notes, destinationTenor = gnf.getNotesFugue(mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), beats1234, destinationTenor, None, tenor)  # NOTE: starting with root of key
    print('destinationTenor', destinationTenor, dtp.distanceToPitch(destinationTenor))
    finalMTX[1][tenor] = [mo.Cell(mo.Chord(destinationChords[1]), mo.Chord(destinationChords[2]), beats1234, notes, destinationTenor, tenor)]
    finalMTX[2][tenor] = [mo.Cell(mo.Chord(destinationChords[2]), mo.Chord(1), beats1234, [mo.Note(dtp.distanceToPitch(destinationTenor), destinationTenor, 1, False, 5)], destinationTenor, tenor)]



    #####################################################################
    # CREATE FILES: .ly, .mxl
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
    cx.createXML(filename, music.key, music.major, music.timesig, finalMTX, measures, maxVoices, "piano")


# debugging
print('Melody Tester - by Jesse Lew')
melodyTester()
