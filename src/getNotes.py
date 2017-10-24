import defineChord as dc
import random

def getNotes(noteArray, rhythms, destination, chord, numOfNotes):

    # get chord tones for strong beats, label as localDestinations
    localDestinations = dc.defineChord('C', 1, chord)

    # store notes needed to destination
    distToDestUp = 0
    note = noteArray[-1][0]
    while note != destination:
        distToDestUp += 1
        note += 1
        # wrap around
        if note == 8:
            note = 1
    distToDestDown = (7 - distToDestUp) % 7  # NOTE: % 7 is in case distToDestUp is 0
    print('note is : '+str(noteArray[-1][0])+', dest : '+str(destination)+', distUp is : '+str(distToDestUp)+', distDown is : '+str(distToDestDown))

    # count the number of non-tied rhythms
    counter = 0
    for i in range(len(rhythms)):
        if '~' not in rhythms[i]:
            counter += 1

    print('counter : '+str(counter)+', numOfNotes : '+str(numOfNotes))
    # can stick to common patterns if the number of notes and rhythms match
    if counter == numOfNotes:
        print('same number of rhythms as notes')

        # TODO: can add suspensions and ornaments like appoggiaturas and trills later
        """
        COMMON PATTERNS FOR numOfNotes == counter: repeat (+0), passing tones, neighbor tones, cambiatas
        COMMON PATTERNS FOR numOfNotes != counter: anticipation, escape tone, leap and resolve by step, accented passing tones
        numOfNotes == 1: repeat (+0), anticipation (+1/-1), escape tone (+1/-1), leap and resolve by step (destination - noteArray[-1][0])
        """
        # if the numOfNotes is the same as the distToDest, just move straight for it
        if numOfNotes + 1 == distToDestUp:
            nextNote = noteArray[-1][0] + 1
            for i in range(len(rhythms)):
                if nextNote == 8:
                    nextNote = 1
                if '~' not in noteArray[-1][1]:
                    noteArray.append([nextNote, rhythms[i]])
                    nextNote += 1
                else:
                    noteArray.append([noteArray[-1][0], rhythms[i]])
        elif numOfNotes + 1 == distToDestDown:
            # same as above in other direction
            nextNote = noteArray[-1][0] - 1
            for i in range(len(rhythms)):
                if nextNote == 0:
                    nextNote = 7
                if '~' not in noteArray[-1][1]:
                    noteArray.append([nextNote, rhythms[i]])
                    nextNote -= 1
                else:
                    noteArray.append([noteArray[-1][0], rhythms[i]])
        else:
            print('numOfNotes != distToDestUp/Down, so try something else')
            for i in range(len(rhythms)):
                noteArray.append([noteArray[-1][0], rhythms[i]])
    else:
        # otherwise gotta get creative
        # TODO: replace the first parameter below with actual pitch choices
        for i in range(len(rhythms)):
            noteArray.append([noteArray[-1][0], rhythms[i]])

