# translate pitch letters into pitch numbers based on key
def pitchToNum(pitch, key='C'):
    if key == 'C':
        return {
            'a': 6,
            'b': 7,
            'c': 1,
            'd': 2,
            'e': 3,
            'f': 4,
            'g': 5
        }.get(pitch, 1)  # find 'pitch' in dictionary above, otherwise default to 1
    # could also use }[pitch] if no default needed
