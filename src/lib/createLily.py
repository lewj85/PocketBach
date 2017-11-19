from lib import matrixToLily as mtl
from lib import speciesCP as scp

def createLily(key, major, finalMTX, measures, maxVoices, scoreType=1):

    # first convert the finalMTX if needed
    if scoreType == 1:
        filename = 'ChoraleFirstSpecies.ly'
    if scoreType == 2:
        filename = 'ChoraleSecondSpecies.ly'
        finalMTX = scp.secondSpecies(finalMTX)
    elif scoreType == 3:
        filename = 'ChoraleThirdSpecies.ly'
        finalMTX = scp.thirdSpecies(finalMTX)
    elif scoreType == 4:
        filename = 'ChoraleFourthSpecies.ly'
        finalMTX = scp.fourthSpecies(finalMTX)
    elif scoreType == 5:
        filename = 'ChoraleFifthSpecies.ly'
        finalMTX = scp.fifthSpecies(finalMTX)
    else:
        filename = 'Fugue.ly'

    # then write the file using finalMTX and matrixToLily()
    if scoreType == 1:
        f = open(filename, 'w')
        if maxVoices == 3:
            f.write("\\version \"2.16.0\"\n\n" +
                    "% PocketBach Score by Jesse Lew\n" +
                    "\\language \"english\"\n\n" +
                    "\\parallelMusic #\'(voiceA voiceB voiceC)\n" +
                    "{\n%soprano\n\\relative c'' " +
                    mtl.matrixToLily(key, major, finalMTX, measures, maxVoices) +
                    "}\n"
                    "\\new StaffGroup <<\n"
                    "  \\new Staff << \\relative c\'\' \\voiceA \\\\ \\relative c\' \\voiceB >>\n"
                    "  \\new Staff \\relative c { \\clef bass \\voiceC }\n"
                    ">>")
        elif maxVoices == 4:
            pass

        f.close()


    # NOTE: scoreType == 6 is for FUGUES
    # then write the file using finalMTX and matrixToLily()
    if scoreType == 6:
        f = open(filename, 'w')
        if maxVoices == 3:
            f.write("\\version \"2.16.0\"\n\n" +
                    "% PocketBach Score by Jesse Lew\n" +
                    "\\language \"english\"\n\n" +
                    "\\parallelMusic #\'(voiceA voiceB voiceC)\n" +
                    "{\n%soprano\n\\relative c'' " +
                    mtl.matrixToLily(key, major, finalMTX, measures, maxVoices) +
                    "}\n"
                    "\\new StaffGroup <<\n"
                    "  \\new Staff << \\relative c\'\' \\voiceA \\\\ \\relative c\' \\voiceB >>\n"
                    "  \\new Staff \\relative c { \\clef bass \\voiceC }\n"
                    ">>")
        elif maxVoices == 4:
            pass

        f.close()
