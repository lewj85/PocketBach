import defineChord as dc
#import pitchToTonal as ptt
#import random


# calls itself recursively for composing Cells if it can't move linearly
# if it can't move linearly to smaller Cell destinations, it
def getNotesChorale(noteArray, rhythms, destination, chord, numOfNotes, measure):

    # get chord tones for strong beats, label as localDestinations
    #localDestinations,a,b,c = dc.defineChord(chord)
    #print('localDestinations are ' + str(localDestinations))

    # store notes needed to destination
    distToDestUp = 0
    note = noteArray[-1][0]
    while note != destination:
        distToDestUp += 1
        note += 1
        # wrap around
        if note == 8:
            note = 1
    distToDestDown = 7 - distToDestUp
    #print('note is : '+str(noteArray[-1][0])+', dest : '+str(destination)+', distUp is : '+str(distToDestUp)+', distDown is : '+str(distToDestDown))

    # count the number of non-tied rhythms
    counter = 0
    for i in range(len(rhythms)):
        if '~' not in rhythms[i][0]:
            counter += 1

    #print('counter : '+str(counter)+', numOfNotes : '+str(numOfNotes))

    # if the numOfNotes is the same as the distToDest, just move straight for it
    if numOfNotes + 1 == distToDestUp:
        print('numOfNotes == distToDestUp. moving linearly.')
        nextNote = noteArray[-1][0] + 1
        for i in range(len(rhythms)):
            if nextNote == 8:
                nextNote = 1
            if '~' not in noteArray[-1][1]:
                noteArray.append([nextNote, rhythms[i][0], measure])
                nextNote += 1
            else:
                noteArray.append([noteArray[-1][0], rhythms[i][0], measure])
    elif numOfNotes + 1 == distToDestDown:
        print('numOfNotes == distToDestDown. moving linearly.')
        # same as above in other direction
        nextNote = noteArray[-1][0] - 1
        for i in range(len(rhythms)):
            if nextNote == 0:
                nextNote = 7
            if '~' not in noteArray[-1][1]:
                noteArray.append([nextNote, rhythms[i][0], measure])
                nextNote -= 1
            else:
                noteArray.append([noteArray[-1][0], rhythms[i][0], measure])
    else:
        print('numOfNotes != distToDestUp/Down, so try something else')

        # TODO: can add suspensions and ornaments like appoggiaturas and trills later
        """
        COMMON PATTERNS FOR numOfNotes == counter: repeat (+0), passing tones, neighbor tones, cambiatas
        COMMON PATTERNS FOR numOfNotes != counter: anticipation, escape tone, leap and resolve by step, accented passing tones
        numOfNotes == 1: repeat (+0), anticipation (+1/-1), escape tone (+1/-1), leap and resolve by step (destination - noteArray[-1][0])
        """
        # check for common patterns
        # 1. REPEATED DESTINATIONS
        if distToDestUp == 0 or distToDestDown == 0:
            print('repeated destination. options: randomize, repeat, up down, down up, up up down down, down down up up, up down up down, down up down up')
            pass

        # 2. DESTINATION IS 1 STEP AWAY
        elif distToDestUp == 1:
            print('distToDestUp = 1. options: randomize, up, up up down, up down up, down up up, others?')
        elif distToDestDown == 1:
            print('distToDestDown = 1. options: randomize, cambiata, down, up down down, down up down, others?')
            pass

        # 3. DESTINATION IS 2 STEPS AWAY




        else: # otherwise if no patterns found, use localDestinations instead and call getNotes() recursively on a smaller number of notes with shorter destinations
            # TODO: the recursion in the comment above
            j = 0
            while j < len(rhythms):  # don't use a for-loop because we may increment i more than once per loop
                noteArray.append([noteArray[-1][0], rhythms[j][0], measure])
                # tie to the next note
                if '~' in noteArray[-1][1]:
                    j += 1
                    noteArray.append([noteArray[-1][0], rhythms[j][0], measure])
                j += 1

