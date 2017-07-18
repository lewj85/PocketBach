# translate pitch letters into pitch numbers based on key
def pitchToNum(pitch, key='C'):
    if key == 'C':
        return {
            'A': 6,
            'B': 7,
            'C': 1,
            'D': 2,
            'E': 3,
            'F': 4,
            'G': 5
        }.get(pitch, 1)  # find 'pitch' in dictionary above, otherwise default to 1
    # could also use }[pitch] if no default needed
