# translate pitch numbers into pitch letters based on key
def tonalToPitch(noteNum = 0, key = 'C'):
    if key == 'C':
        pitchArray = ['r', 'c', 'd', 'e', 'f', 'g', 'a', 'b']
        return pitchArray[noteNum]
