import defineChord as dc
import random

def getNotes(noteArray, rhythms, destination, chord, numOfNotes):

    # get chord tones for strong beats, label as localDestinations
    localDestinations = dc.defineChord('C', 1, chord)

    # count the number of non-tied rhythms
    counter = 0
    for i in range(len(rhythms)):
        if '~' not in rhythms[i]:
            counter += 1

    # can stick to common patterns if the number of notes and rhythms match
    if counter == numOfNotes:
        print('same number of rhythms as notes')
    else:
        # otherwise gotta get creative
        pass

    # TODO: move this for loop into the if/else above
    # noteArray already contains the first note and correct rhythm, so start at 1 not 0
    for i in range(1, len(rhythms)):

        # TODO: replace the first parameter below with actual pitch choices
        noteArray.append([noteArray[-1][0], rhythms[i]])

        # don't append the destination pitch, that's done in writeSubject

