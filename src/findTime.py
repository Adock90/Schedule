from time import strftime, gmtime


def findTime():
    FindingTime = strftime("%H:%M:%S", gmtime())
    return FindingTime
