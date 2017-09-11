import matrixToLily as mtl

def createLily(key, major, finalMTX, measures, maxVoices):

    filename = 'newScore.ly'
    f = open(filename, 'w')
    if maxVoices == 3:
        f.write("\\version \"2.16.0\"\n\n" +
                "% PocketBach Score by Jesse Lew\n" +
                "\\language \"english\"\n\n" +
                "\\parallelMusic #\'(voiceA voiceB voiceC)\n" +
                "{\n" +
                mtl.matrixToLily(key, major, finalMTX, measures, maxVoices) +
                "}\n"
                "\\new StaffGroup <<\n"
                "  \\new Staff << \\relative c\'\' \\voiceA \\\\ \\relative c\' \\voiceB >>\n"
                "  \\new Staff \\relative c { \\clef bass \\voiceC }\n"
                ">>")
    elif maxVoices == 4:
        pass
    f.close()
