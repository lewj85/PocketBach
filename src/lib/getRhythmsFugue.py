import random

#######################################################################
# getRhythmsFugue()
#######################################################################
# calls nothing
# returns rhythms

# NOTES:
# generates beats randomly using random.choice() until the beat total matches totalBeats parameter
# TODO: currently assumes the first beat in beatsArr is an accented beat - fine for current scope

def getRhythmsFugue(beatsArr, timesig = None):

    totalBeats = len(beatsArr)

    if not timesig:
        timesig = [4,4]

    # NOTE: removed whole notes and dotted half notes
    optionsArr = [['2', 2], ['4.', 1.5], ['4', 1], ['8.', 0.75], ['8', 0.5], ['16', 0.25]]
    optionsDict = {
        '2': 2,
        '4.': 1.5,
        '4': 1,
        '8.': 0.75,
        '8': 0.5,
        '16': 0.25
        }

    rhythms = []
    total = 0

    while total < totalBeats:
        downbeat = 0
        accented = 0
        if total == int(total):
            downbeat = 1
        if total == 0 or total == 2:
            accented = 1
        if rhythms:
            # remove certain rhythmic options based on previous rhythm selected
            if rhythms[-1][0] == '4.':  # must be an 8th
                rhythms.append(['8', int(total) + 1, downbeat, accented])
            elif rhythms[-1][0] == '8' and not downbeat:  # only allow 8th and 16ths
                rhythms.append(random.choice([['8', int(total) + 1, downbeat, accented], ['16', int(total) + 1, downbeat, accented]]))
            elif rhythms[-1][0] == '8.' or (rhythms[-1][0] == '16' and not downbeat):  # must be a 16th
                rhythms.append(['16', int(total)+1, downbeat, accented])
            elif not accented:  # remove half note and dotted rhythms
                rhythms.append(random.choice([['4', int(total) + 1, downbeat, accented], ['8', int(total) + 1, downbeat, accented], ['16', int(total) + 1, downbeat, accented]]))
            else:
                rhythms.append([random.choice(optionsArr)[0], int(total) + 1, downbeat, accented])
        else:
            rhythms.append([random.choice(optionsArr)[0], int(total) + 1, downbeat, accented])

        # update total count
        total += optionsDict[rhythms[-1][0]]

        # if you went beyond totalBeats, replace last value
        if total > totalBeats:
            total -= optionsDict[rhythms[-1][0]]
            rhythms.pop()

        # force 'rhythmic diversity' and rewrite measures with too many rhythms
        onlyRhythms = [a for a,b,c,d in rhythms]
        if len(rhythms) > 8 or onlyRhythms.count('2') > 1 or onlyRhythms.count('4') > 3 or onlyRhythms.count('8') > 5 or onlyRhythms.count('16') > 6:
            rhythms = []
            total = 0


    #print(total)
    #print(rhythms)
    return rhythms