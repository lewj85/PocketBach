def pitchToDistance(pitch, voice = 0, key = 'c'):

    if key == 'c':
        # middle C is 39
        # C3 bass
        if voice == 0:
            distance = 24
        elif voice == 1:
            distance = 36
        elif voice == 2:
            distance = 48

        pitchVal = {
            'a': 0,
            'bf': 1,
            'b': 2,
            'c': 3,
            'cs': 4,
            'd': 5,
            'ef': 6,
            'e': 7,
            'f': 8,
            'fs': 9,
            'g': 10,
            'gs': 11
        }.get(pitch, -1)

    # # C5 soprano
    # elif voice == 2:
    #     distance = 51
    #     pitchVal = {
    #         'a': -3,
    #         'as': -2,
    #         'b': -1,
    #         'c': 0,
    #         'cs': 1,
    #         'd': 2,
    #         'ds': 3,
    #         'e': 4,
    #         'f': 5,
    #         'fs': -6,
    #         'g': -5,
    #         'gs': -4
    #     }.get(pitch, -1)
    #
    # # F4 alto
    # elif voice == 1:
    #     distance = 44
    #     pitchVal = {
    #         'a': 4,
    #         'bf': 5,
    #         'b': -6,
    #         'c': -5,
    #         'cs': -4,
    #         'd': -3,
    #         'ds': -2,
    #         'e': -1,
    #         'f': 0,
    #         'fs': 1,
    #         'g': 2,
    #         'af': 3
    #     }.get(pitch, -1)

    # wrap around
    #if pitchVal > 6:
        #distance -= 12

    return distance + pitchVal