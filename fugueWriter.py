import getNextChord as gnc
import numToPitch as ntp
import orchestrate as orch
import createLily as cl
import speciesCP as scp
import random
import os

# https://en.wikipedia.org/wiki/Fugue#Musical_outline

# fugueWriter(noteMTX) function takes arguments from the recorded melody
def fugueWriter(key = 'C', major = 1, timesig = [4,4], noteMTX = []):

    # initialize variables
    chordArray = []
    chordsPerMeasure = 1
    beatsPerMeasure = 4
    measures = 32
    maxVoices = 3

    #####################################################################
    # CREATE MEASURES 1-2 - Tonic (I)
    # Soprano - rest
    # Alto - Subject
    # Bass - rest
    #####################################################################



    #####################################################################
    # CREATE MEASURES 3-4 - Dominant (V)
    # Soprano - Answer
    # Alto - Counter-Subject 1
    # Bass - rest
    #####################################################################



    #####################################################################
    # CREATE MEASURE 5
    # Soprano - Codetta
    # Alto - Codetta
    # Bass - rest
    #####################################################################



    #####################################################################
    # CREATE MEASURES 6-7 - Tonic (I)
    # Soprano - Counter-Subject 1
    # Alto - Counter-Subject 2
    # Bass - Subject
    #####################################################################



    #####################################################################
    # CREATE MEASURES 8-9 - Dominant (V)
    # Soprano - Counter-Subject 2
    # Alto - Answer
    # Bass - Counter-Subject 1
    #####################################################################



    #####################################################################
    # CREATE MEASURES 10-12
    # Soprano - Episode
    # Alto - Episode
    # Bass - Episode
    #####################################################################



    #####################################################################
    # CREATE MEASURES 13-14 - Relative minor/major (vi)
    # Soprano - Subject
    # Alto - Counter-Subject 1
    # Bass - rest
    #####################################################################



    #####################################################################
    # CREATE MEASURES 15-16 - Dominant of relative minor/major (V/vi)
    # Soprano - Counter-Subject 1
    # Alto - Counter-Subject 2
    # Bass - Answer
    #####################################################################



    #####################################################################
    # CREATE MEASURES 17-20 - vi, ii, V, I
    # Soprano - Episode
    # Alto - Episode, Answer false entry measure 19
    # Bass - Episode
    #####################################################################



    #####################################################################
    # CREATE MEASURES 21-22 - Subdominant (IV)
    # Soprano - rest
    # Alto - Subject
    # Bass - Counter-Subject 2
    #####################################################################



    #####################################################################
    # CREATE MEASURES 23-24
    # Soprano - Episode
    # Alto - Episode
    # Bass - Episode
    #####################################################################



    #####################################################################
    # CREATE MEASURES 25-26 - Tonic (I)
    # Soprano - Subject
    # Alto - Counter-Subject 2
    # Bass - Counter-Subject 1
    #####################################################################



    #####################################################################
    # CREATE MEASURES 27-28 - Tonic (I)
    # Soprano - Free counterpoint
    # Alto - Counter-subject 1
    # Bass - Subject
    #####################################################################



    #####################################################################
    # CREATE MEASURES 29-32 - IV ii, V7, I sus43, I
    # Soprano - Coda, Answer false entry measure 30, hold 5th or 3rd measures 31 and 32
    # Alto - Coda, sus43 measures 30-31 with anticipation of final chord at end of 31
    # Bass - pickup-iii, IV ii, V low-V, I, I and low-I
    #####################################################################


# call it
print('Fugue Writer - by Jesse Lew')
fugueWriter()
