def createXML(filename, key, major, timesig, finalMTX, measures, maxVoices, instrument = "organ"):

    if timesig is None:
        timesig = [4,4]

    f = open(filename, 'w')

    if instrument == "piano":
        f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>"
                "\n<!DOCTYPE score-partwise PUBLIC \"-//Recordare//DTD MusicXML 3.0 Partwise//EN\" \"http://www.musicxml.org/dtds/partwise.dtd\">"
                "\n<score-partwise version=\"3.0\">"
                "\n  <movement-title>Fugue</movement-title>"
                "\n  <part-list>"
                "\n    <score-part id=\"P1\">"
                "\n      <part-name>Piano</part-name>"
                "\n      <part-abbreviation>Pno.</part-abbreviation>"
                "\n      <score-instrument id=\"P1-I1\">"
                "\n        <instrument-name>SmartMusic SoftSynth 1</instrument-name>"
                "\n      </score-instrument>"
                "\n      <midi-instrument id=\"P1-I1\">"
                "\n        <midi-channel>1</midi-channel>"
                "\n        <midi-bank>15489</midi-bank>"
                "\n        <midi-program>1</midi-program>"
                #"\n        <volume>80</volume>"
                #"\n        <pan>0</pan>"
                "\n      </midi-instrument>"
                "\n    </score-part>"
                "\n  </part-list>"
                "\n  <!--=========================================================-->"
                "\n  <part id = \"P1\">")

    elif instrument == "organ":
        f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>"
                "\n<!DOCTYPE score-partwise PUBLIC \"-//Recordare//DTD MusicXML 3.0 Partwise//EN\" \"http://www.musicxml.org/dtds/partwise.dtd\">"
                "\n<score-partwise version=\"3.0\">"
                "\n  <movement-title>Fugue</movement-title>"
                "\n  <part-list>"
                "\n    <score-part id=\"P1\">"
                "\n      <part-name>Organ</part-name>"
                "\n      <score-instrument id=\"P1-I1\">"
                "\n        <instrument-name>Organ</instrument-name>"
                "\n      </score-instrument>"
                "\n      <midi-instrument id=\"P1-I1\">"
                "\n        <midi-channel>1</midi-channel>"
                "\n        <midi-program>20</midi-program>"
                "\n        <volume>80</volume>"
                "\n        <pan>0</pan>"
                "\n      </midi-instrument>"
                "\n    </score-part>"
                "\n    <score-part id=\"P2\">"
                "\n      <part-name print-object=\"no\">MusicXML Part</part-name>"
                "\n      <score-instrument id=\"P2-I1\">"
                "\n        <instrument-name>Organ</instrument-name>"
                "\n      </score-instrument>"
                "\n      <midi-instrument id=\"P2-I1\">"
                "\n        <midi-channel>1</midi-channel>"
                "\n        <midi-program>20</midi-program>"
                "\n      </midi-instrument>"
                "\n    </score-part>"
                "\n  </part-list>"
                "\n  <!--=========================================================-->"
                "\n  <part id=\"P1\">")


    for measure in range(measures):

        # do bass afterward if organ
        if instrument == "organ":
            start = 1
        elif instrument == "piano":
            start = 0
        else:
            print('error in createXML: no \'start\' value set')

        f.write("\n    <measure number=\"" + str(measure + 1) + "\">")

        for voice in range(start, maxVoices):

            # first measure, add things like <key>, <time>, etc
            if measure == 0 and voice == start:
                f.write("\n      <attributes>"
                        "\n        <divisions>4</divisions>"  # 4 divisions per quarter note
                        "\n        <key>")

                sharpsflats = {
                    'c1': '0',
                    'a0': '0',
                    'g1': '1',
                    'e0': '1',
                    'd1': '2',
                    'b0': '2',
                    'a1': '3',
                    'fs0': '3',
                    'e1': '4',
                    'cs0': '4',
                    'b1': '5',
                    'fs1': '6',
                    'df1': '-5',
                    'bf0': '-5',
                    'af1': '-4',
                    'ff0': '-4',
                    'ef1': '-3',
                    'c0': '-3',
                    'bf1': '-2',
                    'g0': '-2',
                    'f1': '-1',
                    'd0': '-1'
                }
                f.write("\n          <fifths>" + sharpsflats.get(str(key)+str(int(major))) + "</fifths>")

                if major:
                    majorN = "major"
                else:
                    majorN = "minor"
                f.write("\n          <mode>"+majorN+"</mode>")
                f.write("\n        </key>"
                        "\n        <time>")

                f.write("\n          <beats>"+str(timesig[0])+"</beats>")
                f.write("\n          <beat-type>"+str(timesig[1])+"</beat-type>")

                f.write("\n        </time>"
                        "\n        <staves>2</staves>"
                        "\n        <clef number=\"1\">"
                        "\n          <sign>G</sign>"
                        "\n          <line>2</line>"
                        "\n        </clef>"
                        "\n        <clef number=\"2\">"
                        "\n          <sign>F</sign>"
                        "\n          <line>4</line>"
                        "\n        </clef>"
                        "\n      </attributes>"
                        "\n      <sound tempo=\"120\"/>")

            # every measure
            for cell in finalMTX[measure][voice]:
                for note in cell.notes:
                    f.write("\n      <note>")
                    if note.pitch == 'r':
                        f.write("\n        <rest/>")
                    else:
                        f.write("\n        <pitch>")

                        pitchName = note.pitch[0].upper()
                        f.write("\n          <step>" + pitchName + "</step>")
                        if len(note.pitch) > 1:
                            alterDict = {
                                'f':-1,
                                'ff':-2,
                                's':1,
                                'ss':2
                            }
                            f.write("\n          <alter>" + str(alterDict.get(note.pitch[1:])) + "</alter>")

                        octave = (note.distance + 10) // 12
                        f.write("\n          <octave>" + str(octave) + "</octave>")

                        f.write("\n        </pitch>")

                    # converted note duration * 4 because divisions = 4
                    duration = {
                        '1': 16,
                        '2.': 12,
                        '2': 8,
                        '4.': 6,
                        '4': 4,
                        '8.': 3,
                        '8': 2,
                        '16': 1
                    }
                    durKey = str(note.rhythm)
                    if note.tied:
                        durKey += '.'
                    f.write("\n        <duration>"+str(duration.get(durKey))+"</duration>")

                    # voice 4 bass, 3 alto, 2 soprano? doublecheck this
                    # staff 1 for soprano and alto, staff 2 for bass
                    if maxVoices == 3:
                        voices = {
                            0: 3,
                            1: 2,
                            2: 1
                        }
                        if instrument == "piano":
                            staves = {
                                0: 2,
                                1: 1,
                                2: 1
                            }
                        elif instrument == "organ":
                            staves = {
                                0: 1,  # gets its own staff
                                1: 2,
                                2: 1
                            }
                    elif maxVoices == 4:
                        voices = {
                            0: 4,
                            1: 3,
                            2: 2,
                            3: 1
                        }
                        staves = {
                            0: 1,
                            1: 2,
                            2: 1,
                            3: 1
                        }
                    else:
                        print("error in createXML: maxVoices isn\'t 3 or 4...")
                    f.write("\n        <voice>" + str(voices.get(voice)) + "</voice>")

                    rhythmName = {
                        1:'whole',
                        2:'half',
                        4:'quarter',
                        8:'eighth',
                        16:'16th'
                    }
                    if note.pitch != 'r':
                        f.write("\n        <type>" + rhythmName.get(note.rhythm) + "</type>")
                    if note.tied:
                        f.write("\n        <dot/>")

                    f.write("\n        <staff>" + str(staves.get(voice)) + "</staff>")

                    #f.write("\n        <beam number=\"1\">start</beam>" # start, continue, end based on beat

                    f.write("\n      </note>")

            # backup to next voice in same measure:
            if voice != maxVoices - 1:
                f.write("\n      <backup>"
                        "\n        <duration>16</duration>"  # 16 = 4 beats*4 divisions
                        "\n      </backup>")

            # last measure of each part vs end of any other measure
            if voice == maxVoices - 1:
                f.write("\n    </measure>")
                if measure == measures - 1:
                    f.write("\n  </part>"
                            "\n  <!--=========================================================-->")
                else:
                    f.write("\n    <!--=======================================================-->")


    # now do bass separately for organ
    if instrument == "organ":

        f.write("\n  <part id=\"P2\">")

        for measure in range(measures):
            voice = 0
            f.write("\n    <measure number=\"" + str(measure + 1) + "\">")

            # first measure, add things like <key>, <time>, etc
            if measure == 0:
                f.write("\n      <attributes>"
                        "\n        <divisions>4</divisions>"  # 4 divisions per quarter note
                        "\n        <key>")

                sharpsflats = {
                    'c1': '0',
                    'a0': '0',
                    'g1': '1',
                    'e0': '1',
                    'd1': '2',
                    'b0': '2',
                    'a1': '3',
                    'fs0': '3',
                    'e1': '4',
                    'cs0': '4',
                    'b1': '5',
                    'fs1': '6',
                    'df1': '-5',
                    'bf0': '-5',
                    'af1': '-4',
                    'ff0': '-4',
                    'ef1': '-3',
                    'c0': '-3',
                    'bf1': '-2',
                    'g0': '-2',
                    'f1': '-1',
                    'd0': '-1'
                }
                f.write("\n          <fifths>" + sharpsflats.get(str(key) + str(int(major))) + "</fifths>")

                if major:
                    majorN = "major"
                else:
                    majorN = "minor"
                f.write("\n          <mode>" + majorN + "</mode>")
                f.write("\n        </key>"
                        "\n        <time>")

                f.write("\n          <beats>" + str(timesig[0]) + "</beats>")
                f.write("\n          <beat-type>" + str(timesig[1]) + "</beat-type>")

                f.write("\n        </time>"
                        #"\n        <staves>2</staves>"
                        #"\n        <clef> number=\"1\">"
                        #"\n          <sign>G</sign>"
                        #"\n          <line>2</line>"
                        #"\n        </clef>"
                        "\n        <clef>" # number=\"2\">"
                        "\n          <sign>F</sign>"
                        "\n          <line>4</line>"
                        "\n        </clef>"
                        "\n      </attributes>"
                        "\n      <sound tempo=\"120\"/>")

            # every measure
            for cell in finalMTX[measure][voice]:
                for note in cell.notes:
                    f.write("\n      <note>")
                    if note.pitch == 'r':
                        f.write("\n        <rest/>")
                    else:

                        f.write("\n        <pitch>")

                        pitchName = note.pitch[0].upper()
                        f.write("\n          <step>" + pitchName + "</step>")
                        if len(note.pitch) > 1:
                            alterDict = {
                                'f':-1,
                                'ff':-2,
                                's':1,
                                'ss':2
                            }
                            f.write("\n          <alter>" + str(alterDict.get(note.pitch[1:])) + "</alter>")

                        octave = (note.distance + 10) // 12
                        f.write("\n          <octave>" + str(octave) + "</octave>")

                        f.write("\n        </pitch>")

                    # converted note duration * 4 because divisions = 4
                    duration = {
                        '1': 16,
                        '2.': 12,
                        '2': 8,
                        '4.': 6,
                        '4': 4,
                        '8.': 3,
                        '8': 2,
                        '16': 1
                    }
                    durKey = str(note.rhythm)
                    if note.tied:
                        durKey += '.'
                    f.write("\n        <duration>" + str(duration.get(durKey)) + "</duration>")

                    # voice 4 bass, 3 alto, 2 soprano? doublecheck this
                    # staff 1 for soprano and alto, staff 2 for bass
                    if maxVoices == 3:
                        voices = {
                            0: 3,
                            1: 2,
                            2: 1
                        }
                        #if instrument == "organ":
                        staves = {
                            0: 1,  # gets its own staff
                            1: 2,
                            2: 1
                        }
                    elif maxVoices == 4:
                        voices = {
                            0: 4,
                            1: 3,
                            2: 2,
                            3: 1
                        }
                        staves = {
                            0: 1,
                            1: 2,
                            2: 1,
                            3: 1
                        }
                    else:
                        print("error in createXML: maxVoices isn\'t 3 or 4...")
                    f.write("\n        <voice>" + str(voices.get(voice)) + "</voice>")

                    rhythmName = {
                        1: 'whole',
                        2: 'half',
                        4: 'quarter',
                        8: 'eighth',
                        16: '16th'
                    }

                    if note.pitch != 'r':
                        f.write("\n        <type>" + rhythmName.get(note.rhythm) + "</type>")
                    if note.tied:
                        f.write("\n        <dot/>")

                    f.write("\n        <staff>" + str(staves.get(voice)) + "</staff>")

                    #f.write("\n        <beam number=\"1\">start</beam>" # start, continue, end based on beat

                    f.write("\n      </note>")

            # end of measure
            f.write("\n    </measure>")
            if measure == measures - 1:
                f.write("\n  </part>"
                        "\n  <!--=========================================================-->")
            else:
                f.write("\n    <!--=======================================================-->")


    # close last measure
    f.write("\n</score-partwise>\n")

    f.close()



# debugging - move createXML to src directory for testing
# from lib import musicObjects as mo
# import numpy as np
# a = mo.Note('c', 39, 2, False, 1)
# b = mo.Note('e', 43, 2, False, 1)
# c = mo.Note('g', 46, 2, False, 5)
# d = mo.Note('d', 41, 2, False, 5)
# r1 = mo.Note('r', 88, 1, False, 1)
# r5 = mo.Note('r', 88, 1, False, 5)
# e0 = mo.Cell(mo.Chord(1), mo.Chord(5), [1, 2, 3, 4], [a, b], 46, 0)
# e1 = mo.Cell(mo.Chord(1), mo.Chord(5), [1, 2, 3, 4], [r1], 88, 1)
# e2 = mo.Cell(mo.Chord(1), mo.Chord(5), [1, 2, 3, 4], [r1], 88, 2)
# f0 = mo.Cell(mo.Chord(5), mo.Chord(1), [1, 2, 3, 4], [r5], 88, 0)
# f1 = mo.Cell(mo.Chord(5), mo.Chord(1), [1, 2, 3, 4], [r5], 88, 1)
# f2 = mo.Cell(mo.Chord(5), mo.Chord(1), [1, 2, 3, 4], [c, d], 39, 2)
# testMTX = np.empty((2, 3), dtype=object)
# testMTX[0][0] = [e0]
# testMTX[0][1] = [e1]
# testMTX[0][2] = [e2]
# testMTX[1][0] = [f0]
# testMTX[1][1] = [f1]
# testMTX[1][2] = [f2]
# createXML('Fugue.xml', 'c', True, [4,4], testMTX, 2, 3, "organ")
