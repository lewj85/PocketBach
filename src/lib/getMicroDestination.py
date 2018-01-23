from lib import distanceToPitch as dtp
from lib import pitchToDistance as ptd
from lib import pitchToTonal as ptt
import random

def getMicroDestination(currentChord, startDistance, direction = 1):

    # could also just use defineChord()
    pitches = currentChord.getPitches()

    # get starting pitch
    startPitch = dtp.distanceToPitch(startDistance)

    # remove starting pitch from pitches list - is this necessary?
    #pitches.remove(startPitch)

    # pick a random pitch remaining in the chord
    # TODO: consider not making this random
    chosenPitch = random.choice(pitches)
    # convert to tonal
    chosenTonal = ptt.pitchToTonal(chosenPitch)

    # start at bass
    chosenDistance = ptd.pitchToDistance(chosenPitch, 0)
    # reset to 0
    chosenDistance -= 24
    # move into range - assumes
    while chosenDistance < startDistance:
        chosenDistance += 12
    # fix if direction is -1
    if direction == -1:
        chosenDistance -= 12

    return chosenTonal, chosenDistance, chosenPitch
