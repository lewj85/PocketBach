def createXML(key, major, finalMTX, measures, maxVoices):

    filename = "Fugue.mxl"
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
            "\n<!--=========================================================-->"
            "\n<part id = \"P1\">")

    for measure in range(measures):

        for voice in range(maxVoices):

            f.write("\n    <measure number=\"")
            f.write(measure)
            f.write("\">")

            # first measure, add things like <key>, <time>, etc
            if measure == 0:
                f.write("\n      <attributes>"
                        "\n        <divisions>4</divisions>"  # 4 divisions per quarter note
                        "\n        <key>"
                        "\n          <fifths>0</fifths>"
                        "\n          <mode>major</mode>"
                        "\n        </key>"
                        "\n        <time>"
                        "\n          <beats>4</beats>"
                        "\n          <beat-type>4</beat-type>"
                        "\n        </time>"
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
                f.write("\n      <note>"
                        "\n        <pitch>"
                        "\n          <step>C</step>"
                        "\n          <octave>4</octave>"
                        "\n        </pitch>"
                        "\n        <duration>")
                f.write()  # converted note duration * 4 because divisions = 4
                f.write("</duration>"
                        "\n        <voice>")
                f.write()  # voice 4 bass, 3 alto, 2 soprano? doublecheck this
                f.write("</voice>"
                        "\n        <type>half</type>"
                        "\n        <staff>")
                f.write()  # staff 1 for soprano and alto, staff 2 for bass
                f.write("</staff>"
                        "\n      </note>")

                # backup to next voice in same measure:
                if not the last voice:
                    f.write("\n      <backup>"
                            "\n        <duration>16</duration>"  # 16 = 4 beats*4 divisions
                            "\n      </backup>")

                # end of measure
                f.write("\n</measure>"
                        "\n<!--=======================================================-->")





