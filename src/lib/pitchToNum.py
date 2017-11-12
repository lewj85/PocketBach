# translate pitch letters into pitch numbers based on key
def pitchToNum(pitch='r', key='C'):
    if key == 'C':
        return {
            'r': 0,
            'a': 6,
            'b': 7,
            'c': 1,
            'd': 2,
            'e': 3,
            'f': 4,
            'g': 5
        }.get(pitch, -1)  # find 'pitch' in dictionary above, otherwise default to -1 so we know there's an error
                            # could also use }[pitch] if no default needed
