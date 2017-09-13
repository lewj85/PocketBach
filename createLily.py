import matrixToLily as mtl
import speciesCP

def createLily(key, major, finalMTX, measures, maxVoices, species=1):

    filename = 'newScore.ly'
    f = open(filename, 'w')
    if maxVoices == 3:
        f.write("\\version \"2.16.0\"\n\n" +
                "% PocketBach Score by Jesse Lew\n" +
                "\\language \"english\"\n\n" +
                "\\parallelMusic #\'(voiceA voiceB voiceC)\n" +
                "{\n\\relative c'' " +
                mtl.matrixToLily(key, major, finalMTX, measures, maxVoices) +
                "}\n"
                "\\new StaffGroup <<\n"
                "  \\new Staff << \\relative c\'\' \\voiceA \\\\ \\relative c\' \\voiceB >>\n"
                "  \\new Staff \\relative c { \\clef bass \\voiceC }\n"
                ">>")
    elif maxVoices == 4:
        pass
    f.close()  # save work, even if you're about to change it below

    if species == 2:
        speciesCP.secondSpecies(filename, finalMTX)
    elif species == 3:
        speciesCP.thirdSpecies(filename, finalMTX)
    elif species == 4:
        speciesCP.fourthSpecies(filename, finalMTX)
    elif species == 5:
        speciesCP.fifthSpecies(filename, finalMTX)

