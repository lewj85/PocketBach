import getRhythm as gr
import defineChord as dc
import getNotes as gn
#import pitchToNum as ptn
import random

# TODO: use real data to find number of notes per measure ('melodic density') and weights for rhythms.
#       ignoring weights for now

def writeSubject(key = 'C', major = 1,  subject=list([]), measure=1, measures = 2, chords = list([1,4,5])):

    noteArray = []

    if measure == 1:
        # starting pitches are 1, 3, or 5 with different weights
        start = [1,1,1,3,5,5]
        # pick a random index from start[] list
        noteArray.append(start[random.randint(0,5)])
        #print(pitches)

    # pick random destinations for the following measures
    destArr = []
    for i in range(1, len(chords)):  # NOTE: starts at 1, not 0, so we skip the current known pitch
        options = dc.defineChord(chords[i])
        num1 = random.randint(0,len(options)-1)
        destArr.append(options[num1])

    # for each measure
    for i in range(measures):
        # fill with random number of notes
        # TODO: use real 'melodic density' data to apply weighted randomization
        numOfNotes = random.randint(2,7)
        #print(numOfNotes)

        rhythms = gr.getRhythm(numOfNotes)  # add this parameter functionality to getRhythm or make a new function

        noteArray = gn.getNotes(noteArray, rhythms, destArr[i])  # add this function



# debugging
writeSubject()