import defineChord as dc
import random

def getNotes(noteArray, rhythms, destination, chord, numOfNotes):

    # get chord tones for strong beats, label as localDestinations
    [localDestinations,a,b,c] = dc.defineChord('C', 1, chord)
    #print(localDestinations)

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
    #print('note is : '+str(noteArray[-1][0])+', dest : '+str(destination)+', distUp is : '+str(distToDestUp)+', distDown is : '+str(distToDestDown))

    # count the number of non-tied rhythms
    counter = 0
    for i in range(len(rhythms)):
        if '~' not in rhythms[i][0]:
            counter += 1

    #print('counter : '+str(counter)+', numOfNotes : '+str(numOfNotes))
    # can stick to common patterns if the number of notes and rhythms match
    if counter == numOfNotes:
        print('rhythm counter DOES match random numOfNotes generated: ' + str(counter) + ',' + str(numOfNotes))

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
                    noteArray.append([nextNote, rhythms[i][0]])
                    nextNote += 1
                else:
                    noteArray.append([noteArray[-1][0], rhythms[i][0]])
        elif numOfNotes + 1 == distToDestDown:
            # same as above in other direction
            nextNote = noteArray[-1][0] - 1
            for i in range(len(rhythms)):
                if nextNote == 0:
                    nextNote = 7
                if '~' not in noteArray[-1][1]:
                    noteArray.append([nextNote, rhythms[i][0]])
                    nextNote -= 1
                else:
                    noteArray.append([noteArray[-1][0], rhythms[i][0]])
        else:
            print('numOfNotes != distToDestUp/Down, so try something else')
            useLocalDests(noteArray, rhythms, localDestinations, destination, numOfNotes)
    else:
        # otherwise gotta get creative
        print('rhythm counter does NOT match random numOfNotes generated: ' + str(counter) + ',' + str(numOfNotes))
        useLocalDests(noteArray, rhythms, localDestinations, destination, numOfNotes)


def useLocalDests(noteArray, rhythms, localDestinations, destination, numOfNotes):
    i = 0
    while i < len(rhythms):  # don't use a for-loop because we may increment i more than once per loop
        print('writing for ' + str(rhythms[i][0]))  # if this throws an error it's probably because we use
                                                    # a counter in getNotes() above rather than numOfNotes
                                                    # to deal with tied notes...

        currentNote = noteArray[-1][0]

        # if: look ahead to find accented downbeats - use passing tones, neighbor tones, repeats, to get to localDestinations

        # elif none, then look for numNote:distance patterns - ie. cambiatas, anticipation, repeats

        # elif none, then pick a random motion - ie. escape tone, leap and resolve by step


        # TODO: REMOVE THIS PLACEHOLDER
        noteArray.append([noteArray[-1][0], rhythms[i][0]])
        # tie to the next note
        if '~' in noteArray[-1][1]:
            i += 1
            noteArray.append([noteArray[-1][0], rhythms[i][0]])


        # increment index
        i += 1
