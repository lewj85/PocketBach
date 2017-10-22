import getRhythm as gr
import defineChord as dc
import getNotes as gn
import pitchToNum as ptn
import random

# TODO: use real data to find number of notes per measure ('melodic density') and weights for rhythms.
#       ignoring weights for now

def writeSubject(key = 'C', major = 1, timeSig = list([4,4]), noteArray=list([]), measure=1, measures = 2, chords = list([1,4,5])):

    if measure == 1:
        # starting pitches are 1, 3, or 5 with different weights
        options = [1,1,1,3,5,5]
        # pick a random index from start[] list
        start = options[random.randint(0,5)]
    else:
        start = noteArray[-1][0]

    # pick random destinations for the following measures
    destArr = [start]
    for i in range(1, len(chords)):  # NOTE: starts at 1, not 0, because we manually added the current known pitch
        options = dc.defineChord('C', 1, chords[i])
        #print(options)
        num1 = random.randint(0,len(options[0])-1)
        destArr.append(int(ptn.pitchToNum('C',options[0][num1])))
    print('destArr : '+str(destArr))

    # for each measure
    for i in range(measures):
        # fill with random number of notes
        # TODO: use real 'melodic density' data to apply weighted randomization
        numOfNotes = random.randint(2,7)
        print('numOfNotes : '+str(numOfNotes))

        # first get rhythms based on interval to destination and numOfNotes
        # NOTE: kinda weird to consider rhythms before pitch!
        interval = max([destArr[i], destArr[i+1]]) - min([destArr[i], destArr[i+1]])
        rhythms = gr.randRhythm(timeSig, interval, 0, numOfNotes)
        print('rhythms : '+str(rhythms))

        # if first measure, add the first note and first rhythm
        if measure == 1:
            noteArray.append([destArr[0], rhythms[0]])
        # otherwise set the last value in noteArray with a real rhythm because it has a default whole note!
        else:
            noteArray[-1][1] = rhythms[0]

        # get notes for the rhythms
        gn.getNotes(noteArray, rhythms, destArr[i+1], chords[i], numOfNotes)

        # finally, tack on the next destination to start the next measure with a default rhythm of
        # NOTE: this will add the final destination to noteArray, meaning this will start an extra measure!
    noteArray.append([destArr[i+1], 1])

    print(noteArray)

# debugging
writeSubject()