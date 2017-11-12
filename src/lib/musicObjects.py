"""Class definitions for musical objects"""

import defineChord as dc

"""
Matrix = [voice][measure][Cell]
getNotes() composes for Cells, not measure by measure, and not beat by beat
for now, the matrix isn't broken into beats, cells are the smallest part, each cell has 1 chord

Class Hierarchy
Music = key, major, timesig
    Chord = root, tonality, seventh, inversion, secondary, secondaryRoot
        Note = pitch, distance, rhythm
Cell = chord, beats, notes, rhythms
"""


class Music:

    def __init__(self, key = 'C', major = 1, timesig = None):
        self.key = key                          # int: represents number of sharps (positive) or flats (negative)
        self.major = major                      # int: major = 1, minor = 0
        if timesig is None:
            self.timesig = [4,4]                # default is [4,4]
        else:
            self.timesig = timesig              # [int, int] array: index 0 = beats, index 1 = rhythmic base value



class Chord(Music):

    def __init__(self, key, major, timesig, root, tonality = 0, seventh = 0, inversion = 0, secondary = 0, secondaryRoot = 0):
        Music.__init__(self, key, major, timesig)
        self.root = root                        # int: chord root, represents Roman numeral number (key is irrelevant)
        self.tonality = tonality                # int: represents moving from tonal triad up/down (ie. minor v to V = 1)
        self.seventh = seventh                  # int: 0 = triad, 1 = 7th
        self.inversion = inversion              # int: 0 = None, 1 = 1st, 2 = 2nd, 3 = 3rd
        self.secondary = secondary              # int: 0 = None, 1 = secondary
        self.secondaryRoot = secondaryRoot      # int: 1-7, represents root of secondary (dominant) chord

    def getPitches(self):
        return dc.defineChord(None, root, seventh, tonality, inversion, key, major)



class Note(Chord):

    def __init__(self, key, major, timesig, root, tonality, seventh, inversion, secondary, secondaryRoot, pitch, distance, rhythm, tied = 0):
        Chord.__init__(self, key, major, timesig, root, tonality, seventh, inversion, secondary, secondaryRoot)
        self.pitch = pitch                      # string: lowercase char plus "s" for sharp, "f" for flat, "ss", or "ff"
        self.distance = distance                # int: 0-87, distance from lowest pitch "A0" = 0, "C8" = 87
        self.rhythm = rhythm                    # int: 1 = whole note, 2 = half, 4 = quarter, 8 = 8th, etc
        self.tied = tied                        # int: 0 = not tied to next note, 1 = tied to next note

    def inChord(self):
        return [chordPitch for chordPitch in self.getPitches()]       # inherited

    def getIntervalFrom(self, note2):
        return self.distance - note2.distance

    def getIntervalTo(self, note2):
        return note2.distance - self.distance



class Cell:

    def __init__(self, chord, beats, notes):
        self.chord = chord                      # Chord class: see definition above
        self.beats = beats                      # [int] array: contains the beats that this cell covers, ie. [1, 2], max size is 1 measure
        self.notes = notes                      # [Note] array: see Note definition above, contains data including pitch and rhythm
