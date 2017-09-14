# major: 0 = major, 1 = minor
# root: 1-7
# seventh: 0 = no, 1 = yes
# tonality: 0 = tonal root, 1 = raised (bVII vs viio in a minor key)

def defineChord(key='C', major=1, root=1, seventh=0, tonality=0):

    # TO DO: turn params into a string and using that string as
    #   a dictionary lookup for O(1) lookup rather than go through a million nested if-elses

    # NOTE: removed all inversions because getNextNote removes specific indexes
    #   for each inversion already

    chord = []
    if key == 'C':
        if major == 1:
            if root == 1:
                if seventh == 0:
                    chord = ['C', 'E', 'G']
                else:
                    chord = ['C', 'E', 'G', 'B']
            elif root == 2:
                if seventh == 0:
                    chord = ['D', 'F', 'A']
                else:
                    chord = ['D', 'F', 'A', 'C']
            elif root == 3:
                if seventh == 0:
                    chord = ['E', 'G', 'B']
                else:
                    chord = ['E', 'G', 'B', 'D']
            elif root == 4:
                if seventh == 0:
                    chord = ['F', 'A', 'C']
                else:
                    chord = ['F', 'A', 'C', 'E']
            elif root == 5:
                if seventh == 0:
                    chord = ['G', 'B', 'D']
                else:
                    chord = ['G', 'B', 'D', 'F']
            elif root == 6:
                if seventh == 0:
                    chord = ['A', 'C', 'E']
                else:
                    chord = ['A', 'C', 'E', 'G']
            elif root == 7:
                if seventh == 0:
                    chord = ['B', 'D', 'F']
                else:
                    chord = ['B', 'D', 'F', 'A']

    return chord
