def tonalToDistance(tonal, voice = 0, key = 'C'):

    # middle C is 39

    # C3 bass
    if voice == 0:
        distance = 27
        pitch = {
            'a': -3,
            'as': -2,
            'b': -1,
            'c': 0,
            'cs': 1,
            'd': 2,
            'ds': 3,
            'e': 4,
            'f': 5,
            'fs': -6,
            'g': -5,
            'gs': -4
        }.get(tonal, -1)

    # C5 soprano
    elif voice == 1:
        distance = 51
        pitch = {
            'a': -3,
            'as': -2,
            'b': -1,
            'c': 0,
            'cs': 1,
            'd': 2,
            'ds': 3,
            'e': 4,
            'f': 5,
            'fs': -6,
            'g': -5,
            'gs': -4
        }.get(tonal, -1)

    # F4 alto
    elif voice == 2:
        distance = 44
        pitch = {
            'a': 4,
            'as': 5,
            'b': -6,
            'c': -5,
            'cs': -4,
            'd': -3,
            'ds': -2,
            'e': -1,
            'f': 0,
            'fs': 1,
            'g': 2,
            'gs': 3
        }.get(tonal, -1)

    # if pitch > 6:
    #     distance -= 12

    if key == 'C':
        return distance + tonal