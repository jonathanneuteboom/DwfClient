import datetime

from dateutil import parser

from DwfModels.Approval import Approval
from DwfModels.DwfTypes import ScoresheetStatus, SetScore
from DwfModels.Match import Match
from DwfModels.Owner import Owner
from DwfModels.Set import Set


class Scoresheet:
    id: str
    createdAt: datetime
    currentSet: int
    status: ScoresheetStatus
    isAborted: bool
    score: SetScore
    reasonNotPlayed: str
    match: Match
    owner: Owner
    sets: list[Set]
    approval: Approval

    def fromJSON(data):
        newScoresheet = Scoresheet()
        newScoresheet.id = data["id"]
        newScoresheet.createdAt = parser.parse(data["createdAt"])
        newScoresheet.currentSet = data.get("currentSet")
        newScoresheet.status = ScoresheetStatus[data["status"]]
        newScoresheet.isAborted = data["isAborted"]
        newScoresheet.score = data["score"]
        newScoresheet.reasonNotPlayed = data["reasonNotPlayed"]
        newScoresheet.match = Match.fromJSON(data["match"])
        newScoresheet.owner = Owner.fromJSON(data["owner"])
        newScoresheet.sets = [Set.fromJSON(playedSet) for playedSet in data["sets"]]
        newScoresheet.approval = Approval.fromJSON(data["approval"])

        return newScoresheet
