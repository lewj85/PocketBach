# translate pitch numbers into pitch letters based on key
def numToPitch(key='C', noteNum=0):
    if key == 'C':
        pitchArray = ['r', 'c', 'd', 'e', 'f', 'g', 'a', 'b']
        return pitchArray[noteNum]
