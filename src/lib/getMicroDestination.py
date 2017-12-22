from lib import distanceToPitch as dtp
from lib import pitchToDistance as ptd
from lib import pitchToTonal as ptt

def getMicroDestination(currentChord, startDistance, direction):

    # could also just use defineChord()
    pitches = currentChord.getPitches()

    # get starting pitch
    startPitch = dtp.distanceToPitch(startDistance)

    # remove starting pitch from pitches list
    pitches.remove(startPitch)

    # pick a random pitch remaining in the chord
    # TODO: consider not making this random
    chosenPitch = random.choice(pitches)
    # convert to tonal
    chosenTonal = ptt.pitchToTonal(chosenPitch)

    # NOT NEEDED FOR SCOPE OF PROJECT YET, COMMENTING OUT
    # # start at bass
    # chosenDistance = ptd.pitchToDistance(chosenPitch, 0)
    # # reset to 0
    # chosenDistance -= 24
    # # move into range
    # while chosenDistance < startDistance:
    #     chosenDistance += 12
    # # fix if direction is -1
    # if direction == -1:
    #     chosenDistance -= 12

    return chosenTonal #, chosenDistance, chosenPitch
