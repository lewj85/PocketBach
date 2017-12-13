"""Class definitions for musical objects"""

from lib import defineChord as dc

"""
Matrix = [voice][measure][Cell]
getNotes() composes for Cells, not measure by measure, and not beat by beat
for now, the matrix isn't broken into beats, cells are the smallest part, each cell has 1 chord

Class Hierarchy
Music = key, major, timesig
    Chord = root, tonality, seventh, inversion, secondary, secondaryRoot
        Note = pitch, distance, rhythm, tied
Cell = chord, beats, notes, rhythms
"""


class Music:

    def __init__(self, key = 'c', major = True, timesig = None):
        self.key = key                          # int: represents number of sharps (positive) or flats (negative)
        self.major = major                      # boolean: True or False
        self.timesig = timesig                  # [int, int] array: index 0 = beats, index 1 = rhythmic base value
        if timesig is None:
            self.timesig = [4,4]                # default is [4,4]



class Chord(Music):

    def __init__(self, root, tonality = 0, seventh = False, inversion = 0, secondary = False, secondaryRoot = 0, key = 'C', major = True, timesig = None):
        Music.__init__(self, key, major, timesig)
        self.root = root                        # int: chord root, represents Roman numeral number (key/accidentals are irrelevant)
        self.tonality = tonality                # int: represents moving from tonal triad up/down (ie. minor v to V = 1, IV to minor iv = -1)
        self.seventh = seventh                  # boolean: False = triad, True = 7th
        self.inversion = inversion              # int: 0 = None, 1 = 1st, 2 = 2nd, 3 = 3rd
        self.secondary = secondary              # boolean: False = no, True = secondary
        self.secondaryRoot = secondaryRoot      # int: 1-7, represents Roman numeral number root of secondary (dominant) chord

    def getPitches(self):
        return dc.defineChord(self)[0]



class Note(Chord):

    def __init__(self, pitch, distance, rhythm, tied, root, tonality = 0, seventh = False, inversion = 0, secondary = False, secondaryRoot = 0, key = 'C', major = True, timesig = None):
        Chord.__init__(self, root, tonality, seventh, inversion, secondary, secondaryRoot, key, major, timesig)
        self.pitch = pitch                      # string: lowercase char plus "s" for sharp, "f" for flat, "ss", or "ff" - 'r' for rest
        self.distance = distance                # int: 0-88, distance from lowest pitch "A0" = 0, "C8" = 87, rest = 88
        self.rhythm = rhythm                    # int: 1 = whole note, 2 = half, 4 = quarter, 8 = 8th, 16 = 16th
        self.tied = tied                        # boolean: False = not tied to next note, True = tied to next note

    def inChord(self):
        return [chordPitch for chordPitch in self.getPitches()]       # inherited from Chord class

    def getIntervalFrom(self, note2):
        return self.distance - note2.distance

    def getIntervalTo(self, note2):
        return note2.distance - self.distance



class Cell:

    def __init__(self, chord, nextChord, beats, notes, destination, voice):
        self.chord = chord                      # Chord class: see definition above
        self.nextChord = nextChord              # Chord class: the next chord so we know where to start the next Cell
        self.beats = beats                      # [int] array: contains the beats that this cell covers, ie. [1, 2], max size is 1 measure
        self.notes = notes                      # [Note] array: see Note definition above, contains data including pitch and rhythm
        self.destination = destination          # int: 'distance' 0-87 of destination
        self.voice = voice                      # int: 0 = bass, voice numbers ascend, ie. soprano = 2 in 3-voice harmony
