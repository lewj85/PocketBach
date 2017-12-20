# translate pitch numbers into pitch letters based on key
def tonalToPitch(noteNum = 0, key = 'c'):
    if key == 'c':
        pitchArray = ['r', 'c', 'd', 'e', 'f', 'g', 'a', 'b']
        return pitchArray[noteNum]
