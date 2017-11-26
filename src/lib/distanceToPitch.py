"""Converts distance value (0-87, 88=rest) to pitch ('a','cs','ef', etc)"""

def distanceToPitch(distance):

    # if a rest
    if distance == 88:
        return 'r'

    # if not a rest
    else:
        distance %= 12
        pitchArray = ['a','bf','b','c','cs','d','ef','e','f','fs','g','af']
        return pitchArray[distance]
