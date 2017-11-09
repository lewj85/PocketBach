import random

# Can be any number of beats, but must be over ONE chord - anything from a 2-beat cell to an 8-beat phrase
def getNotes(currentChord, nextChord, beats, start = None, destination = None, previousCells = None, key = None, timesig = None):

    if not key:
        key = 'C'
    if not timesig:
        timesig = [4,4]

    # any measure where a voice first enters or re-enters after a rest
    if not start:
        options = dc.defineChord(key, 1, currentChord)
        # pick a random index from options
        start = random.choice(options[0])

    if not destination:
        # pick a random destination
        options = dc.defineChord(key, 1, nextChord)



def createEpisodeCell(chordsOverBeats, start = None, destination = None, episodeCell = None):
    pass



def alterPhraseToFitNewChord(phrase, newChord):
    # can either change pitches or rhythms, such as turning 1 quarter note into 2 eights to arrive at a destination 1 away
    pass



def getRhythms(totalBeats, timesig = None):

    if not timesig:
        timesig = [4,4]

    # NOTE: removed whole notes
    optionsArr = [['2.', 3], ['2', 2], ['4.', 1.5], ['4', 1], ['8.', 0.75], ['8', 0.5], ['16', 0.25]]
    optionsDict = {
        '2.': 3,
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
            if rhythms[-1][0] == '4.' or (rhythms[-1][0] == '8' and not downbeat):
                rhythms.append(random.choice([['8', int(total) + 1, downbeat, accented], ['16', int(total) + 1, downbeat, accented]]))
            elif rhythms[-1][0] == '8.' or (rhythms[-1][0] == '16' and not downbeat):
                rhythms.append(['16', int(total)+1, downbeat, accented])
            elif not accented:
                rhythms.append(random.choice([['4', int(total) + 1, downbeat, accented], ['8', int(total) + 1, downbeat, accented], ['16', int(total) + 1, downbeat, accented]]))
            else:
                rhythms.append([random.choice(optionsArr)[0], int(total) + 1, downbeat, accented])
        else:
            rhythms.append([random.choice(optionsArr)[0], int(total) + 1, downbeat, accented])

        total += optionsDict[rhythms[-1][0]]

        # if you went beyond totalBeats, replace last value
        if total > totalBeats:
            total -= optionsDict[rhythms[-1][0]]
            rhythms.pop()

    print(total)

    return rhythms

#print(getRhythms(2))
#print(getRhythms(4))
