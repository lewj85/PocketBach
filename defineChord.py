# major: 0 = major, 1 = minor
# root: 1-7
# seventh: 0 = no, 1 = yes
# tonality: 0 = tonal root, 1 = raised (bVII vs viio in a minor key)

def defineChord(key='C', major=1, root=1, seventh=0, tonality=0):

    # TO DO: turn params into a string and using that string as
    #   a dictionary lookup for O(1) lookup rather than go through a million nested if-elses

    dictKey = key+str(major)+str(root)+str(seventh)+str(tonality)

    # NOTE: removed all inversions because getNextNote removes specific indexes
    #   for each inversion already

    return {
        'C1100': ['c', 'e', 'g'],
        'C1110': ['c', 'e', 'g', 'b'],
        'C1200': ['d', 'f', 'a'],
        'C1210': ['d', 'f', 'a', 'c'],
        'C1300': ['e', 'g', 'b'],
        'C1310': ['e', 'g', 'b', 'd'],
        'C1400': ['f', 'a', 'c'],
        'C1410': ['f', 'a', 'c', 'e'],
        'C1500': ['g', 'b', 'd'],
        'C1510': ['g', 'b', 'd', 'f'],
        'C1600': ['a', 'c', 'e'],
        'C1610': ['a', 'c', 'e', 'g'],
        'C1700': ['b', 'd', 'f'],
        'C1710': ['b', 'd', 'f', 'a'],
    }[dictKey]
