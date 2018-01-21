"""defineChord() returns a list of data: [[pitches for the requested chord], inversion, 7th chord, secondary dominant]"""

"""
major: 1 = major, 0 = minor
root: 1-7
seventh: 0 = no, 1 = yes
tonality = 0 is tonal root and chord
tonality = -1 is lowered root, such as bIII, bVI, and bVII in a minor key
tonality = 1 is a secondary dominant V, such as V/vi
tonality = 2 is a secondary dominant viio, such as viio/V

NOTE: currently only supports V/x chords and viio/x, no other secondary dominants
        but these are temporarily removed because choraleWriter manually inserts certain chords,
        so there's no guarantee that the secondary dominants will be followed by their expected resolution
TO DO: decide if you want to break tonality into multiple columns (rootAdjust,
    secondaryDom, triadAdjust, seventhAdjust, etc)
    PROS: more advanced chord possibilities like neopolitan 6ths, aug 6ths, etc. 
    CONS: a lot of chord possibilities out there weren't common for Bach... consider this program's scope.
          notation may be difficult (see b7 vs L7 vs Y7).

on the subject of scope, consider if you really want to write music more than C major/minor
"""

# NOTE: weightedProbability must use a dictKey
def defineChord(ChordObject, dictKey = None):

    key = ChordObject.key
    major = ChordObject.major
    root = ChordObject.root
    seventh = ChordObject.seventh
    tonality = ChordObject.tonality
    inversion = ChordObject.inversion
    secroot = ChordObject.secondaryRoot

    if dictKey is None:
        # create the dictionary key by concatenating the params using Hooktheory's chord terminology
        #   so we can complete searches in O(1) time
        # TODO: fix tonality and secroot using ChordObject.secondaryRoot - consider scope of this project...
        dictKey = ''
        if tonality == 0:
            dictKey += str(root)
        else:
            print('tonality is not 0 in defineChord')

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

        if ChordObject.secondary:
            dictKey += '/'+str(secroot)

        #print("dictKey:", dictKey)

    # TODO: fix the chordArr adjustments in getNextNote.py to account for inversions being added

    if key == 'c':
        if major is True:
            # returns [notes in chord, inversion, 7th chord, secondary dominant]
            return {
                # tonal chords
                '1': [['c', 'e', 'g'],0,0,0],
                '16': [['e', 'g', 'c'],1,0,0],
                '164': [['g', 'c', 'e'],2,0,0],
                '17': [['c', 'e', 'g', 'b'],0,1,0],
                '165': [['e', 'g', 'b', 'c'],1,1,0],
                '143': [['g', 'b', 'c', 'e'],2,1,0],
                '12': [['b', 'c', 'e', 'g'],3,1,0],
                '2': [['d', 'f', 'a'],0,0,0],
                '26': [['f', 'a', 'd'],1,0,0],
                '264': [['a', 'd', 'f'],2,0,0],
                '27': [['d', 'f', 'a', 'c'],0,1,0],
                '265': [['f', 'a', 'c', 'd'],1,1,0],
                '243': [['a', 'c', 'd', 'f'],2,1,0],
                '22': [['c', 'd', 'f', 'a'],3,1,0],
                '3': [['e', 'g', 'b'],0,0,0],
                '36': [['g', 'b', 'e'],1,0,0],
                '364': [['b', 'e', 'g'],2,0,0],
                '37': [['e', 'g', 'b', 'd'],0,1,0],
                '365': [['g', 'b', 'd', 'e'],1,1,0],
                '343': [['b', 'd', 'e', 'g'],2,1,0],
                '32': [['d', 'e', 'g', 'b'],3,1,0],
                '4': [['f', 'a', 'c'],0,0,0],
                '46': [['a', 'c', 'f'],1,0,0],
                '464': [['c', 'f', 'a'],2,0,0],
                '47': [['f', 'a', 'c', 'e'],0,1,0],
                '465': [['a', 'c', 'e', 'f'],1,1,0],
                '443': [['c', 'e', 'f', 'a'],2,1,0],
                '42': [['e', 'f', 'a', 'c'],3,1,0],
                '5': [['g', 'b', 'd'],0,0,0],
                '56': [['b', 'd', 'g'],1,0,0],
                '564': [['d', 'g', 'b'],2,0,0],
                '57': [['g', 'b', 'd', 'f'],0,1,0],
                '565': [['b', 'd', 'f', 'g'],1,1,0],
                '543': [['d', 'f', 'g', 'b'],2,1,0],
                '52': [['f', 'g', 'b', 'd'],3,1,0],
                '6': [['a', 'c', 'e'],0,0,0],
                '66': [['c', 'e', 'a'],1,0,0],
                '664': [['e', 'a', 'c'],2,0,0],
                '67': [['a', 'c', 'e', 'g'],0,1,0],
                '665': [['c', 'e', 'g', 'a'],1,1,0],
                '643': [['e', 'g', 'a', 'c'],2,1,0],
                '62': [['g', 'a', 'c', 'e'],3,1,0],
                '7': [['b', 'd', 'f'],0,0,0],
                '76': [['d', 'f', 'b'],1,0,0],
                '764': [['f', 'b', 'd'],2,0,0],
                '77': [['b', 'd', 'f', 'a'],0,1,0],
                '765': [['d', 'f', 'a', 'b'],1,1,0],
                '743': [['f', 'a', 'b', 'd'],2,1,0],
                '72': [['a', 'b', 'd', 'f'],3,1,0],  # add the comma here when you re-add secondary dominants
                # secondary dominants, V/x and V7/x
                '5/2': [['a', 'cs', 'e'],0,0,1],
                '56/2': [['cs', 'e', 'a'],1,0,1],
                '564/2': [['e', 'a', 'cs'],2,0,1],
                '57/2': [['a', 'cs', 'e', 'g'],0,1,1],
                '565/2': [['cs', 'e', 'g', 'a'],1,1,1],
                '543/2': [['e', 'g', 'a', 'cs'],2,1,1],
                '52/2': [['g', 'a', 'cs', 'e'],3,1,1],
                '5/3': [['b', 'ds', 'fs'],0,0,1],
                '56/3': [['ds', 'fs', 'b'],1,0,1],
                '564/3': [['fs', 'b', 'ds'],2,0,1],
                '57/3': [['b', 'ds', 'fs', 'a'],0,1,1],
                '565/3': [['ds', 'fs', 'a', 'b'],1,1,1],
                '543/3': [['fs', 'a', 'b', 'ds'],2,1,1],
                '52/3': [['a', 'b', 'ds', 'fs'],3,1,1],
                '5/4': [['c', 'e', 'g'],0,0,1], # 5/4 is just a 1 chord, but for completion...
                '56/4': [['e', 'g', 'c'],1,0,1], # 56/4 is just a 16 chord, but for completion...
                '564/4': [['g', 'c', 'e'],2,0,1], # 564/4 is just a 164 chord, but for completion...
                '57/4': [['c', 'e', 'g', 'bf'],0,1,1],
                '565/4': [['e', 'g', 'bf', 'c'],1,1,1],
                '543/4': [['g', 'bf', 'c', 'e'],2,1,1],
                '52/4': [['bf', 'c', 'e', 'g'],3,1,1],
                '5/5': [['d', 'fs', 'a'],0,0,1],
                '56/5': [['fs', 'a', 'd'],1,0,1],
                '564/5': [['a', 'd', 'fs'],2,0,1],
                '57/5': [['d', 'fs', 'a', 'c'],0,1,1],
                '565/5': [['fs', 'a', 'c', 'd'],1,1,1],
                '543/5': [['a', 'c', 'd', 'fs'],2,1,1],
                '52/5': [['c', 'd', 'fs', 'a'],3,1,1],
                '5/6': [['e', 'gs', 'b'],0,0,1],
                '56/6': [['gs', 'b', 'e'],1,0,1],
                '564/6': [['b', 'e', 'gs'],2,0,1],
                '57/6': [['e', 'gs', 'b', 'd'],0,1,1],
                '565/6': [['gs', 'b', 'd', 'e'],1,1,1],
                '543/6': [['b', 'd', 'e', 'gs'],2,1,1],
                '52/6': [['d', 'e', 'gs', 'b'],3,1,1],
                '5/7': [['fs', 'as', 'cs'],0,0,1],
                '56/7': [['as', 'cs', 'fs'],1,0,1],
                '564/7': [['cs', 'fs', 'as'],2,0,1],
                '57/7': [['fs', 'as', 'cs', 'e'],0,1,1],
                '565/7': [['as', 'cs', 'e', 'fs'],1,1,1],
                '543/7': [['cs', 'e', 'fs', 'as'],2,1,1],
                '52/7': [['e', 'fs', 'as', 'cs'],3,1,1],
                # secondary dominants, viio/x and viio7/x (half-diminished in a major key)
                '7/2': [['cs', 'e', 'g'],0,0,1],
                '76/2': [['e', 'g', 'cs'],1,0,1],
                '764/2': [['g', 'cs', 'e'],2,0,1],
                '77/2': [['cs', 'e', 'g', 'b'],0,1,1],
                '765/2': [['e', 'g', 'b', 'cs'],1,1,1],
                '743/2': [['g', 'b', 'cs', 'e'],2,1,1],
                '72/2': [['b', 'cs', 'e', 'g'],3,1,1],
                '7/3': [['ds', 'fs', 'a'],0,0,1],
                '76/3': [['fs', 'a', 'ds'],1,0,1],
                '764/3': [['a', 'ds', 'fs'],2,0,1],
                '77/3': [['ds', 'fs', 'a', 'cs'],0,1,1],
                '765/3': [['fs', 'a', 'cs', 'ds'],1,1,1],
                '743/3': [['a', 'cs', 'ds', 'fs'],2,1,1],
                '72/3': [['cs', 'ds', 'fs', 'a'],3,1,1],
                '7/4': [['e', 'g', 'bf'],0,0,1],
                '76/4': [['g', 'bf', 'e'],1,0,1],
                '764/4': [['bf', 'e', 'g'],2,0,1],
                '77/4': [['e', 'g', 'bf', 'd'],0,1,1],
                '765/4': [['g', 'bf', 'd', 'e'],1,1,1],
                '743/4': [['bf', 'd', 'e', 'g'],2,1,1],
                '72/4': [['d', 'e', 'g', 'bf'],3,1,1],
                '7/5': [['fs', 'a', 'c'],0,0,1],
                '76/5': [['a', 'c', 'fs'],1,0,1],
                '764/5': [['c', 'fs', 'a'],2,0,1],
                '77/5': [['fs', 'a', 'c', 'e'],0,1,1],
                '765/5': [['a', 'c', 'e', 'fs'],1,1,1],
                '743/5': [['c', 'e', 'fs', 'a'],2,1,1],
                '72/5': [['e', 'fs', 'a', 'c'],3,1,1],
                '7/6': [['gs', 'b', 'd'],0,0,1],
                '76/6': [['b', 'd', 'gs'],1,0,1],
                '764/6': [['d', 'gs', 'b'],2,0,1],
                '77/6': [['gs', 'b', 'd', 'fs'],0,1,1],
                '765/6': [['b', 'd', 'fs', 'gs'],1,1,1],
                '743/6': [['d', 'fs', 'gs', 'b'],2,1,1],
                '72/6': [['fs', 'gs', 'b', 'd'],3,1,1],
                '7/7': [['as', 'cs', 'e'],0,0,1],
                '76/7': [['cs', 'e', 'as'],1,0,1],
                '764/7': [['e', 'as', 'cs'],2,0,1],
                '77/7': [['as', 'cs', 'e', 'gs'],0,1,1],
                '765/7': [['cs', 'e', 'gs', 'as'],1,1,1],
                '743/7': [['e', 'gs', 'as', 'cs'],2,1,1],
                '72/7': [['gs', 'as', 'cs', 'e'],3,1,1]
            }.get(dictKey, 0)
        elif major is False:
            pass

    print('error in defineChord.py - dictionary did not return values')
    return 0
