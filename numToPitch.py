# translate pitch numbers into pitch letters based on key
def numToPitch(noteNum=0, key='C'):
    if key == 'C':
        pitchArray = ['R', 'C', 'D', 'E', 'F', 'G', 'A', 'B']
        return pitchArray[noteNum]