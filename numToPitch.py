# translate pitch numbers into pitch letters based on key
def numToPitch(noteNum=0, key='C'):
    if key == 'C':
        pitchArray = ['r', 'c', 'd', 'e', 'f', 'g', 'a', 'b']
        return pitchArray[noteNum]