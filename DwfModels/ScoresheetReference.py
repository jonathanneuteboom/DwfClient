from dateutil import parser


import datetime


class ScoresheetReference:
    id: str
    matchId: str
    isDemo: bool
    createdAt: datetime
    currentSet: int
    status: str
    isAborted: bool
    deviceId: str
    deviceName: str
    userId: int
    userName: str
    reasonNotPlayed: str
    currentSetScore: list[int]
    score: list[int]

    def fromJSON(data):
        newScoresheetReference = ScoresheetReference()
        newScoresheetReference.id = data["id"]
        newScoresheetReference.matchId = data["matchId"]
        newScoresheetReference.isDemo = data["isDemo"]
        newScoresheetReference.createdAt = parser.parse(data["createdAt"])
        newScoresheetReference.currentSet = data.get("currentSet")
        newScoresheetReference.status = data["status"]
        newScoresheetReference.isAborted = data["isAborted"]
        newScoresheetReference.deviceId = data["deviceId"]
        newScoresheetReference.deviceName = data["deviceName"]
        newScoresheetReference.userId = data["userId"]
        newScoresheetReference.userName = data["userName"]
        newScoresheetReference.reasonNotPlayed = data["reasonNotPlayed"]
        newScoresheetReference.currentSetScore = data["currentSetScore"]
        newScoresheetReference.score = data["score"]

        return newScoresheetReference
