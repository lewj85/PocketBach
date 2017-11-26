# TODO: think about how to fix this. perhaps return an array where index 0 are the tonal ints below and
#   index 1 is 0/1/-1 for normal/raised/lowered. would need to pass chord as param to do properly. consider
#   scope of this project before doing extra work!
def distanceToTonal(distance, key = 'C'):
    distance %= 12
    if key == 'C':
        return {
            0 : 6,
            1 : 7,
            2 : 7,
            3 : 0,
            4 : 0,
            5 : 1,
            6 : 1,
            7 : 2,
            8 : 3,
            9 : 3,
            10 : 4,
            11 : 5
        }.get(distance, -1)

