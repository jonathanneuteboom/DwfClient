import datetime

from dateutil import parser

from DwfModels.Approval import Approval
from DwfModels.Match import Match
from DwfModels.Owner import Owner
from DwfModels.Set import Set


class Scoresheet:
    id: str
    createdAt: datetime
    currentSet: int
    status: str
    isAborted: bool
    score: list[int]
    reasonNotPlayed: str

    def __init__(self, **data):
        self.id = data["id"]
        self.createdAt = parser.parse(data["createdAt"])
        self.currentSet = data.get("currentSet")
        self.status = data["status"]
        self.isAborted = data["isAborted"]
        self.score = data["score"]
        self.reasonNotPlayed = data["reasonNotPlayed"]
        self.match = Match.fromJSON(data["match"])
        self.owner = Owner.fromJSON(data["owner"])
        self.sets = [Set.fromJSON(playedSet) for playedSet in data["sets"]]
        self.approval = Approval.fromJSON(data["approval"])
