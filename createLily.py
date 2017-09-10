import matrixToLily as mtl

def createLily(key, major, finalMTX, measures, maxVoices):

    filename = 'newScore.ly'
    f = open(filename, 'w')
    f.write("\\version \"2.16.0\"\n\n" +
            "% PocketBach Score by Jesse Lew\n" +
            "\\language \"english\"\n\n" +
            "\\relative c\'\n" +
            "{\n" +
            mtl.matrixToLily(key, major, finalMTX, measures, maxVoices) +
            "}\n")
    f.close()
