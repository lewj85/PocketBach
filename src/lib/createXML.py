def createXML(filename, key, major, timesig, finalMTX, measures, maxVoices):

    if timesig is None:
        timesig = [4,4]

    f = open(filename, 'w')


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
            "\n        <volume>80</volume>"
            "\n        <pan>0</pan>"
            "\n      </midi-instrument>"
            "\n    </score-part>"
            "\n  </part-list>"
            "\n  <!--=========================================================-->"
            "\n  <part id = \"P1\">")

    for measure in range(measures):

        for voice in range(maxVoices):

            f.write("\n    <measure number=\""+str(measure)+"\">")

            # first measure, add things like <key>, <time>, etc
            if measure == 0:
                f.write("\n      <attributes>"
                        "\n        <divisions>4</divisions>"  # 4 divisions per quarter note
                        "\n        <key>")

                # TODO: add other keys
                sharpsflats = {
                    'C1':0,
                    'C0':-3
                }
                f.write("\n          <fifths>"+str(sharpsflats.get(str(str(key)+str(major))))+"</fifths>")

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
                        f.write("\n      <note>"
                                "\n        <pitch>"
                                "\n          <step>C</step>"
                                "\n          <octave>4</octave>"
                                "\n        </pitch>")

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
                        f.write("\n        <duration>"+str(duration.get(note.rhythm))+"</duration>")

                        # voice 4 bass, 3 alto, 2 soprano? doublecheck this
                        # staff 1 for soprano and alto, staff 2 for bass
                        if maxVoices == 3:
                            voices = {
                                0: 4,
                                1: 3,
                                2: 2
                            }
                            staves = {
                                4: 1,
                                3: 2,
                                2: 2
                            }
                        elif maxVoices == 4:
                            voices = {
                                0: 4,
                                1: 1,  # ?? check this...
                                2: 3,
                                3: 2
                            }
                            staves = {
                                4: 1,
                                1: 1,  # ?? check this...
                                3: 2,
                                2: 2
                            }
                        else:
                            print("error in createXML: maxVoices isn\'t 3 or 4...")
                        f.write("\n        <voice>"+str(voices.get(voice))+"</voice>")

                        noteName = {
                            '1':'whole',
                            '2.':'dotted-half',
                            '2':'half',
                            '4.':'dotted-quarter',
                            '4':'quarter',
                            '8.':'dotted-eighth',
                            '8':'eighth',
                            '16':'sixteenth'
                        }
                        f.write("\n        <type>"+noteName.get(note.rhythm)+"</type>")
                        f.write("\n        <staff>"+str(staves.get(voice))+"</staff>")
                        f.write("\n      </note>")

                # backup to next voice in same measure:
                if voice != maxVoices - 1:
                    f.write("\n      <backup>"
                            "\n        <duration>16</duration>"  # 16 = 4 beats*4 divisions
                            "\n      </backup>")

                # end of measure
                f.write("\n    </measure>")
                if not (measure == measures - 1 and voice == maxVoices - 1):  # all measures and voices except the last
                    f.write("\n    <!--=======================================================-->")

        # last measure
        if measure == measures - 1:
            f.write("\n  </part>")
            f.write("\n  <!--=========================================================-->")
            f.write("\n</score-partwise>\n")


    f.close()
