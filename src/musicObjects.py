"""Class definitions for musical objects"""

import defineChord as dc

class Music:

    def __init__(self, key, major, timesig):
        self.key = key                          # int: represents number of sharps (positive) or flats (negative)
        self.major = major                      # int: major = 1, minor = 0
        self.timesig = timesig                  # [int, int] array: index 0 = beats, index 1 = rhythmic base value



class Chord(Music):

    def __init__(self, key, major, timesig, root, tonality = 0, seventh = None, inversion = 0, secondary = None, secondaryRoot = None):
        Music.__init__(self, key, major, timesig)
        self.root = root                        # int: chord root, represents Roman numeral number (key is irrelevant)
        self.tonality = tonality                # int: represents moving from tonal triad up/down (ie. minor v to V = 1)
        self.seventh = seventh                  # int: 0 = triad, 1 = 7th
        self.inversion = inversion              # int: 0 = None, 1 = 1st, 2 = 2nd, 3 = 3rd
        self.secondary = secondary              # int: 0 = None, 1 = secondary
        self.secondaryRoot = secondaryRoot      # int: 1-7, represents root of secondary (dominant) chord

    def getPitches(self):
        return dc.defineChord(Music.key, Music.major, root, seventh, tonality, inversion)



class Note(Chord):

    def __init__(self, pitch, distance, rhythm, tied, key, major, timesig, root, tonality, seventh, inversion, secondary, secondaryRoot):
        Chord.__init__(self, key, major, timesig, root, tonality, seventh, inversion, secondary, secondaryRoot)
        self.pitch = pitch                      # string: lowercase char plus "s" for sharp, "f" for flat, "ss", or "ff"
        self.distance = distance                # int: 0-87, distance from lowest pitch "A0" = 0, "C8" = 87
        self.rhythm = rhythm                    # int: 1 = whole note, 2 = half, 4 = quarter, 8 = 8th, etc
        self.tied = tied                        # int: 0 = not tied to next note, 1 = tied to next note

    def inChord(self):
        return pitch in self.getPitches()

    def getIntervalFrom(self, note2):
        return self.distance - note2.distance

    def getIntervalTo(self, note2):
        return note2.distance - self.distance



class Cell:

    def __init__(self, noteArray):
        self.noteArray = noteArray              # [Note] array: contains Notes with data (ie. rhythms)

    def getRhythm(self):
        return [rhythm for Note.rhythm in noteArray]



class Measure(Music):

    def __init__(self, key, major, timesig, beatsPerMeasure, beatChordPairs):
        Music.__init__(self, key, major, timesig)
        self.timesig = timesig                  # [int, int] array: can redefine timesig in each measure
        self.beatsPerMeasure = beatsPerMeasure  # int: represents compound beats in measure (ie. 6/8 = 2)
        self.beatChordPairs = beatChordPairs    # [int, Chord] array: matches each chord in measure to its non-compound beat
