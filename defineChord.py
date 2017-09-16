"""defineChord() returns lists of strings containing pitches for the requested chord"""

"""
major: 1 = major, 0 = minor
root: 1-7
seventh: 0 = no, 1 = yes
tonality = 0 is tonal root and chord
tonality = -1 is lowered root, such as bIII, bVI, and bVII in a minor key
tonality = 1 is a secondary dominant V, such as V/vi
tonality = 2 is a secondary dominant viio, such as viio/V
"""

"""
NOTE: currently only supports V/x chords and viio/x, no other secondary dominants
TO DO: decide if you want to break tonality into multiple columns (rootAdjust,
    secondaryDom, triadAdjust, seventhAdjust, etc)
    PROS: more advanced chord possibilities like neopolitan 6ths, aug 6ths, etc. 
    CONS: a lot of chord possibilities out there weren't common for Bach... consider this program's scope.
          notation may be difficult (see b7 vs L7 vs Y7).

on the subject of scope, consider if you really want to write music more than C major/minor
"""


def defineChord(key = 'C', major = 1, root = 1, seventh = 0, inversion = 0, tonality = 0):

    # create the dictionary key by concatenating the params using Hooktheory's chord terminology
    #   so we can complete searches in O(1) time
    dictKey = ''
    if tonality == 0:
        dictKey += str(root)
    elif tonality == -1:
        dictKey += 'b'+str(root)
    elif tonality == 1:
        dictKey += '5'
        secroot = root+3
        if secroot > 7:  # check root is in range
            secroot -= 7
    elif tonality == 2:
        dictKey += '7'
        secroot = root+1
        if secroot == 8:  # check root is in range
            secroot = 1

    if seventh == 0:
        # if inversion == 0: don't do anything
        if inversion == 1:
            dictKey += '6'
        elif inversion == 2:  # can't use 'else' because we skipped inversion == 0
            dictKey += '64'
    else:  # seventh == 1
        if inversion == 0:
            dictKey += '7'
        elif inversion == 1:
            dictKey += '65'
        elif inversion == 2:
            dictKey += '43'
        else:  # inversion == 3
            dictKey += '2'

    if tonality > 0:
        dictKey += '/'+str(secroot)

    print(dictKey)  # debugging

    # TO DO: fix the chordArr adjustments in getNextNote.py to account for inversions being added

    if key == 'C':
        if major == 1:
            return {
                # tonal chords
                '1': ['c', 'e', 'g'],
                '16': ['e', 'g', 'c'],
                '164': ['g', 'c', 'e'],
                '17': ['c', 'e', 'g', 'b'],
                '165': ['e', 'g', 'b', 'c'],
                '143': ['g', 'b', 'c', 'e'],
                '12': ['b', 'c', 'e', 'g'],
                '2': ['d', 'f', 'a'],
                '26': ['f', 'a', 'd'],
                '264': ['a', 'd', 'f'],
                '27': ['d', 'f', 'a', 'c'],
                '265': ['f', 'a', 'c', 'd'],
                '243': ['a', 'c', 'd', 'f'],
                '22': ['c', 'd', 'f', 'a'],
                '3': ['e', 'g', 'b'],
                '36': ['g', 'b', 'e'],
                '364': ['b', 'e', 'g'],
                '37': ['e', 'g', 'b', 'd'],
                '365': ['g', 'b', 'd', 'e'],
                '343': ['b', 'd', 'e', 'g'],
                '32': ['d', 'e', 'g', 'b'],
                '4': ['f', 'a', 'c'],
                '46': ['a', 'c', 'f'],
                '464': ['c', 'f', 'a'],
                '47': ['f', 'a', 'c', 'e'],
                '465': ['a', 'c', 'e', 'f'],
                '443': ['c', 'e', 'f', 'a'],
                '42': ['e', 'f', 'a', 'c'],
                '5': ['g', 'b', 'd'],
                '56': ['b', 'd', 'g'],
                '564': ['d', 'g', 'b'],
                '57': ['g', 'b', 'd', 'f'],
                '565': ['b', 'd', 'f', 'g'],
                '543': ['d', 'f', 'g', 'b'],
                '52': ['f', 'g', 'b', 'd'],
                '6': ['a', 'c', 'e'],
                '66': ['c', 'e', 'a'],
                '664': ['e', 'a', 'c'],
                '67': ['a', 'c', 'e', 'g'],
                '665': ['c', 'e', 'g', 'a'],
                '643': ['e', 'g', 'a', 'c'],
                '62': ['g', 'a', 'c', 'e'],
                '7': ['b', 'd', 'f'],
                '76': ['d', 'f', 'b'],
                '764': ['f', 'b', 'd'],
                '77': ['b', 'd', 'f', 'a'],
                '765': ['d', 'f', 'a', 'b'],
                '743': ['f', 'a', 'b', 'd'],
                '72': ['a', 'b', 'd', 'f'],
                # secondary dominants, V/x and V7/x
                '5/2': ['a', 'cs', 'e'],
                '56/2': ['cs', 'e', 'a'],
                '564/2': ['e', 'a', 'cs'],
                '57/2': ['a', 'cs', 'e', 'g'],
                '565/2': ['cs', 'e', 'g', 'a'],
                '543/2': ['e', 'g', 'a', 'cs'],
                '52/2': ['g', 'a', 'cs', 'e'],
                '5/3': ['b', 'ds', 'fs'],
                '56/3': ['ds', 'fs', 'b'],
                '564/3': ['fs', 'b', 'ds'],
                '57/3': ['b', 'ds', 'fs', 'a'],
                '565/3': ['ds', 'fs', 'a', 'b'],
                '543/3': ['fs', 'a', 'b', 'ds'],
                '52/3': ['a', 'b', 'ds', 'fs'],
                '5/4': ['c', 'e', 'g'], # 5/4 is just a 1 chord, but for completion...
                '56/4': ['e', 'g', 'c'], # 56/4 is just a 16 chord, but for completion...
                '564/4': ['g', 'c', 'e'], # 564/4 is just a 164 chord, but for completion...
                '57/4': ['c', 'e', 'g', 'bf'],
                '565/4': ['e', 'g', 'bf', 'c'],
                '543/4': ['g', 'bf', 'c', 'e'],
                '52/4': ['bf', 'c', 'e', 'g'],
                '5/5': ['d', 'fs', 'a'],
                '56/5': ['fs', 'a', 'd'],
                '564/5': ['a', 'd', 'fs'],
                '57/5': ['d', 'fs', 'a', 'c'],
                '565/5': ['fs', 'a', 'c', 'd'],
                '543/5': ['a', 'c', 'd', 'fs'],
                '52/5': ['c', 'd', 'fs', 'a'],
                '5/6': ['e', 'gs', 'b'],
                '56/6': ['gs', 'b', 'e'],
                '564/6': ['b', 'e', 'gs'],
                '57/6': ['e', 'gs', 'b', 'd'],
                '565/6': ['gs', 'b', 'd', 'e'],
                '543/6': ['b', 'd', 'e', 'gs'],
                '52/6': ['d', 'e', 'gs', 'b'],
                '5/7': ['fs', 'as', 'cs'],
                '56/7': ['as', 'cs', 'fs'],
                '564/7': ['cs', 'fs', 'as'],
                '57/7': ['fs', 'as', 'cs', 'e'],
                '565/7': ['as', 'cs', 'e', 'fs'],
                '543/7': ['cs', 'e', 'fs', 'as'],
                '52/7': ['e', 'fs', 'as', 'cs'],
                # secondary dominants, viio/x and viio7/x (half-diminished in a major key)
                '7/2': ['cs', 'e', 'g'],
                '76/2': ['e', 'g', 'cs'],
                '764/2': ['g', 'cs', 'e'],
                '77/2': ['cs', 'e', 'g', 'b'],
                '765/2': ['e', 'g', 'b', 'cs'],
                '743/2': ['g', 'b', 'cs', 'e'],
                '72/2': ['b', 'cs', 'e', 'g'],
                '7/3': ['ds', 'fs', 'a'],
                '76/3': ['fs', 'a', 'ds'],
                '764/3': ['a', 'ds', 'fs'],
                '77/3': ['ds', 'fs', 'a', 'cs'],
                '765/3': ['fs', 'a', 'cs', 'ds'],
                '743/3': ['a', 'cs', 'ds', 'fs'],
                '72/3': ['cs', 'ds', 'fs', 'a'],
                '7/4': ['e', 'g', 'bf'],
                '76/4': ['g', 'bf', 'e'],
                '764/4': ['bf', 'e', 'g'],
                '77/4': ['e', 'g', 'bf', 'd'],
                '765/4': ['g', 'bf', 'd', 'e'],
                '743/4': ['bf', 'd', 'e', 'g'],
                '72/4': ['d', 'e', 'g', 'bf'],
                '7/5': ['fs', 'a', 'c'],
                '76/5': ['a', 'c', 'fs'],
                '764/5': ['c', 'fs', 'a'],
                '77/5': ['fs', 'a', 'c', 'e'],
                '765/5': ['a', 'c', 'e', 'fs'],
                '743/5': ['c', 'e', 'fs', 'a'],
                '72/5': ['e', 'fs', 'a', 'c'],
                '7/6': ['gs', 'b', 'd'],
                '76/6': ['b', 'd', 'gs'],
                '764/6': ['d', 'gs', 'b'],
                '77/6': ['gs', 'b', 'd', 'fs'],
                '765/6': ['b', 'd', 'fs', 'gs'],
                '743/6': ['d', 'fs', 'gs', 'b'],
                '72/6': ['fs', 'gs', 'b', 'd'],
                '7/7': ['as', 'cs', 'e'],
                '76/7': ['cs', 'e', 'as'],
                '764/7': ['e', 'as', 'cs'],
                '77/7': ['as', 'cs', 'e', 'gs'],
                '765/7': ['cs', 'e', 'gs', 'as'],
                '743/7': ['e', 'gs', 'as', 'cs'],
                '72/7': ['gs', 'as', 'cs', 'e'],
            }.get(dictKey, ['c', 'e', 'g'])
        elif major == 0:
            pass


    return 'r'