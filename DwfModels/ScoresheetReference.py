import datetime
from enum import Enum

from dateutil import parser

from DwfModels.DwfTypes import Points, ScoresheetStatus, SetScore


class ScoresheetReference:
    id: str
    matchId: str
    isDemo: bool
    createdAt: datetime
    currentSet: int
    status: ScoresheetStatus
    isAborted: bool
    deviceId: str
    deviceName: str
    userId: int
    userName: str
    reasonNotPlayed: str
    currentSetScore: Points
    score: SetScore

    def fromJSON(data):
        newScoresheetReference = ScoresheetReference()
        newScoresheetReference.id = data["id"]
        newScoresheetReference.matchId = data["matchId"]
        newScoresheetReference.isDemo = data["isDemo"]
        newScoresheetReference.createdAt = parser.parse(data["createdAt"])
        newScoresheetReference.currentSet = data.get("currentSet")
        newScoresheetReference.status = ScoresheetStatus[data["status"]]
        newScoresheetReference.isAborted = data["isAborted"]
        newScoresheetReference.deviceId = data["deviceId"]
        newScoresheetReference.deviceName = data["deviceName"]
        newScoresheetReference.userId = data["userId"]
        newScoresheetReference.userName = data["userName"]
        newScoresheetReference.reasonNotPlayed = data["reasonNotPlayed"]
        newScoresheetReference.currentSetScore = data["currentSetScore"]
        newScoresheetReference.score = data["score"]

        return newScoresheetReference
