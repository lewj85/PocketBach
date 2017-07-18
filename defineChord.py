# major: 0 = major, 1 = minor
# root: 1-7
# seventh: 0 = no, 1 = yes
# tonality: 0 = tonal root, 1 = raised (bVII vs vii in a minor key)

def defineChord(key='C', major=0, root=1, seventh=0, tonality=0, inversion=0):
    chord = []
    if key == 'C':
        if major == 0:
            if root == 1:
                if seventh == 0:
                    if inversion == 0:
                        chord = ['C', 'E', 'G']
                    elif inversion == 1:
                        chord = ['E', 'G', 'C']
                    elif inversion == 2:
                        chord = ['G', 'C', 'E']
                elif seventh == 1:
                    if inversion == 0:
                        chord = ['C', 'E', 'G', 'B']
                    elif inversion == 1:
                        chord = ['E', 'G', 'B', 'C']
                    elif inversion == 2:
                        chord = ['G', 'B', 'C', 'E']
                    elif inversion == 3:
                        chord = ['B', 'C', 'E', 'G']
            elif root == 2:
                if seventh == 0:
                    if inversion == 0:
                        chord = ['D', 'F', 'A']
                    elif inversion == 1:
                        chord = ['F', 'A', 'D']
                    elif inversion == 2:
                        chord = ['A', 'D', 'F']
                elif seventh == 1:
                    if inversion == 0:
                        chord = ['D', 'F', 'A', 'C']
                    elif inversion == 1:
                        chord = ['F', 'A', 'C', 'D']
                    elif inversion == 2:
                        chord = ['A', 'C', 'D', 'F']
                    elif inversion == 3:
                        chord = ['C', 'D', 'F', 'A']
            elif root == 3:
                if seventh == 0:
                    if inversion == 0:
                        chord = ['E', 'G', 'B']
                    elif inversion == 1:
                        chord = ['G', 'B', 'E']
                    elif inversion == 2:
                        chord = ['B', 'E', 'G']
                elif seventh == 1:
                    if inversion == 0:
                        chord = ['E', 'G', 'B', 'D']
                    elif inversion == 1:
                        chord = ['G', 'B', 'D', 'E']
                    elif inversion == 2:
                        chord = ['B', 'D', 'E', 'G']
                    elif inversion == 3:
                        chord = ['D', 'E', 'G', 'B']
            elif root == 4:
                if seventh == 0:
                    if inversion == 0:
                        chord = ['F', 'A', 'C']
                    elif inversion == 1:
                        chord = ['A', 'C', 'F']
                    elif inversion == 2:
                        chord = ['C', 'F', 'A']
                elif seventh == 1:
                    if inversion == 0:
                        chord = ['F', 'A', 'C', 'E']
                    elif inversion == 1:
                        chord = ['A', 'C', 'E', 'F']
                    elif inversion == 2:
                        chord = ['C', 'E', 'F', 'A']
                    elif inversion == 3:
                        chord = ['E', 'F', 'A', 'C']
            elif root == 5:
                if seventh == 0:
                    if inversion == 0:
                        chord = ['G', 'B', 'D']
                    elif inversion == 1:
                        chord = ['B', 'D', 'G']
                    elif inversion == 2:
                        chord = ['D', 'G', 'B']
                elif seventh == 1:
                    if inversion == 0:
                        chord = ['G', 'B', 'D', 'F']
                    elif inversion == 1:
                        chord = ['B', 'D', 'F', 'G']
                    elif inversion == 2:
                        chord = ['D', 'F', 'G', 'B']
                    elif inversion == 3:
                        chord = ['F', 'G', 'B', 'D']
            elif root == 6:
                if seventh == 0:
                    if inversion == 0:
                        chord = ['A', 'C', 'E']
                    elif inversion == 1:
                        chord = ['C', 'E', 'A']
                    elif inversion == 2:
                        chord = ['E', 'A', 'C']
                elif seventh == 1:
                    if inversion == 0:
                        chord = ['A', 'C', 'E', 'G']
                    elif inversion == 1:
                        chord = ['C', 'E', 'G', 'A']
                    elif inversion == 2:
                        chord = ['E', 'G', 'A', 'C']
                    elif inversion == 3:
                        chord = ['G', 'A', 'C', 'E']
            elif root == 7:
                if seventh == 0:
                    if inversion == 0:
                        chord = ['B', 'D', 'F']
                    elif inversion == 1:
                        chord = ['D', 'F', 'B']
                    elif inversion == 2:
                        chord = ['F', 'B', 'D']
                elif seventh == 1:
                    if inversion == 0:
                        chord = ['B', 'D', 'F', 'A']
                    elif inversion == 1:
                        chord = ['D', 'F', 'A', 'B']
                    elif inversion == 2:
                        chord = ['F', 'A', 'B', 'D']
                    elif inversion == 3:
                        chord = ['A', 'B', 'D', 'F']
    return chord
