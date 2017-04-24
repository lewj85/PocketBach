import chord_writer
#import chorale_writer

# main() function
def main():

    # initialize variables
    beatsPerMeasure = 4

    # get the rate of chord movement
    numMeasures = int(input("Enter number of measures: "))
    chordsPerMeasure = int(input("Enter the number of chords per measure: "))

    # get first chord or first few chords
    chordArray = [int(x) for x in input("Enter the array of chords: ").split()]
    # if no previous chords are provided, the first chord is defaulted to 1
    if chordArray == []:
        chordArray.append(1)
    #print(chordArray)  # comment out

    # get destination
    try:
        destination = int(input("Enter the destination chord: "))
    # if no destination is provided, the destination is defaulted to 1
    except:
        destination = 1

    #key = input("Enter the key: ")  # commented out until key library is used

    # calculate number of chords that need to be filled
    chordsNeeded = (numMeasures * chordsPerMeasure) - len(chordArray)

    # fill in the missing chords
    for i in range(0, chordsNeeded):
        # get the next chord. pass 3 params:
        # 1. the number of remaining chords, found by (chordsNeeded - i)
        # 2. the destination chord
        # 3. the previous chord, found by chordArray[-1]
        nextChord = chord_writer.getNextChord((chordsNeeded - i), destination, chordArray[-1])
        chordArray.append(nextChord)

    # add the destination chord to the end of the chordArray after filling it
    chordArray.append(destination)

    # display chordArray
    print(chordArray)

    lenCA = len(chordArray)

    # create a 2D note matrix
    # dimensions:
    #   1. notes in current chord
    #   2. note data: pitch, duration, direction, interval, chord root, 7th chord,
    #        tonality, inversion, prev chord root, pickup, beat, measure
    noteMTX = [[0 for x in range(16)] for y in range(12)]

    #print(noteMTX)

    # create a list of the note matrices
    #   broken down by chord
    noteMTXList = []

    # fill in the chords:
    for j in range(lenCA):
        noteMTX[j][4] = chordArray[j]
        noteMTX[j][10] = 1
        noteMTX[j][11] = j+1
        noteMTXList.append(noteMTX[j][:])

    print(noteMTXList)

    # fill in the bass line



    #print(noteMTX)


# call main()
main()
