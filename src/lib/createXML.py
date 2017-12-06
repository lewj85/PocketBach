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
            "\n        <instrument-sound>keyboard.piano</instrument-sound>"
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

        # NOTE: if measure == 0: add things like <key>, <time>, etc
        pass


