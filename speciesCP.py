# for second- through fifth-species, we have 3 options:
#   1) alter finalMTX's shape to XXx12x3 (after it finishes writing it as 16x12x3)
#       then send the new matrix to matrixToLily (matrixToLily already uses a while
#       loop exactly for this)
#       NOTE: make sure to add measure numbers (last column) to the new notes for the
#           while loop to work!
#       NOTE: need to add if statements to beginning and end of the while loops for
#           voice==2 (or voice==3 in 4-part harmony...) to set/reset j for each of the
#           different species
#       PROBLEM: fifth-species is a problem because we don't know the size of the matrix...
#   2) or partition, add to, and concatenate matrixToLily's finalString
#       PROBLEM: we know indexes for the partitions in C major, but what if there are accidentals?
#   3) or use regex on the .ly file (easy-ish since each .ly is almost exactly the same)
#       then add the new notes to the soprano lines in the file
#       PROBLEM: none, everyone loves regex. right, guys? ...guys?
# going with option #3, since #1 and #2 have major problems

import random
import defineChord as dc

def secondSpecies(filename, finalMTX):
    f = open(filename, 'r+')  # r+ opens for read+write, starts at beginning of file

    # check for repeated pitches first, just use c d c or c b c
    # check for +2/-2 next (remember wrapping with mod7), just use passing tones

    f.close()

def thirdSpecies(filename, finalMTX):
    f = open(filename, 'r+')  # r+ opens for read+write, starts at beginning of file

    # add rest to beginning in soprano
    # use defineChord on both current chord and next chord to try to prioritize
    #   suspension possibilities
    # add ties after each note, except last!!!

    f.close()

def fourthSpecies(filename, finalMTX):
    f = open(filename, 'r+')  # r+ opens for read+write, starts at beginning of file

    # check for repeated pitches first, just use c d c b c or c b c d c
    # check for +2/-2 (remember wrapping with mod7), just use c d c b a or c b c d e
    # check for +4/-4 (remember wrapping with mod7), just use c d e f g or c b a g f

    f.close()

def fifthSpecies(filename, finalMTX):
    f = open(filename, 'r+')  # r+ opens for read+write, starts at beginning of file

    # this one is hard... write a new function just for this...

    f.close()
