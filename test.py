import getNextChord as gnc
#import chorale_writer

# main() function
def main():

    # get the rate of chord movement
    numMeasures = int(input("Enter number of measures: "))
    beatsPerMeasure = int(input("Enter number of beats per measure: "))
    chordsPerMeasure = int(input("Enter the number of chords per measure: "))

    # get first chord or first few chords
    chordArray = [int(x) for x in input("Enter the array of chords: ").split()]
    # if no previous chords are provided, the first chord is defaulted to 1
    if chordArray == []:
        chordArray.append(1)
    #print(chordArray)

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
        nextChord = gnc.getNextChord((chordsNeeded - i), destination, chordArray[-1])
        chordArray.append(nextChord)

    # add the destination chord to the end of the chordArray after filling it
    chordArray.append(destination)

    # display chordArray
    print(chordArray)

    lenCA = len(chordArray)

    # create a 2D note matrix
    # dimensions:
    #   1. notes in current chord
    #   2. 12 note data types: pitch, duration, direction, interval, chord root,
    #       7th chord, tonality, inversion, prev chord root, pickup, beat, measure
    noteMTX = [[0 for y in range(12)] for x in range(lenCA)]

    #print(noteMTX)

    # create a list of the note matrices
    #   broken down by chord
    noteMTXList = []

    # fill in the chords:
    for j in range(lenCA):
        noteMTX[j][4] = chordArray[j]                       # chord root
        if j > 0:
            noteMTX[j][8] = noteMTX[j-1][4]                 # prev chord root
        noteMTX[j][10] = int((j % chordsPerMeasure) * (beatsPerMeasure / chordsPerMeasure)) + 1      # beats
        noteMTX[j][11] = int(j / chordsPerMeasure) + 1      # measure number
        #noteMTXList.append(noteMTX[j][:])

    #print(noteMTXList)
    print(noteMTX)


# call main()
if __name__ == "__main__":
    print('Test - by Jesse Lew')
    main()
