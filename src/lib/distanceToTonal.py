# TODO: think about how to fix this. perhaps return an array where index 0 are the tonal ints below and
#   index 1 is 0/1/-1 for normal/raised/lowered. would need to pass chord as param to do properly. consider
#   scope of this project before doing extra work!
def distanceToTonal(distance, key = 'C'):

    # if rest, return 0 for tonal
    if distance == 88:
        return 0

    # otherwise bring down to 0-11 and return index
    newDist = distance % 12  # note: don't change distance with %=, make a new variable
    if key == 'C':
        tonalOptions = [6,7,7,0,0,1,1,2,3,3,4,5]
        return tonalOptions[newDist]
