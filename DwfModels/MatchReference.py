import datetime

from dateutil import parser

from DwfModels.DwfTypes import Points
from DwfModels.Location import Location
from DwfModels.ScoresheetReference import ScoresheetReference
from DwfModels.Team import Team
from DwfModels.TeamReference import TeamReference


class MatchReference:
    id: int
    status: str
    reference: str
    timestamp: datetime
    location: Location
    court: str
    teams: list[Team]
    result: Points
    scoresheets: list[ScoresheetReference]

    def fromJSON(data):
        newMatchReference = MatchReference()
        newMatchReference.id = data["id"]
        newMatchReference.status = data["status"]
        newMatchReference.reference = data["reference"]
        newMatchReference.timestamp = parser.parse(data["timestamp"])
        newMatchReference.location = Location.fromJSON(data["location"])
        newMatchReference.court = data["court"]
        newMatchReference.teams = [
            TeamReference.fromJSON(team) for team in data["teams"]
        ]
        newMatchReference.result = data["result"]
        newMatchReference.scoresheets = [
            ScoresheetReference.fromJSON(scoresheet)
            for scoresheet in data["scoresheets"]
        ]

        return newMatchReference
