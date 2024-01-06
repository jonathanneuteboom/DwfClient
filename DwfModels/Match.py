import datetime

from DwfModels.DwfTypes import Points
from DwfModels.Location import Location
from DwfModels.Official import Official
from DwfModels.ScoresheetReference import ScoresheetReference
from DwfModels.Team import Team


class Match:
    id: int
    status: str
    reference: str
    timestamp: datetime
    location: Location
    court: str
    teams: list[Team]
    result: Points
    scoresheetReference: ScoresheetReference

    def fromJSON(data):
        newMatch = Match()
        newMatch.id = data["id"]
        newMatch.status = data["status"]
        newMatch.reference = data["reference"]
        newMatch.timestamp = data["timestamp"]
        newMatch.location = Location.fromJSON(data["location"])
        newMatch.court = data["court"]
        newMatch.teams = [Team.fromJSON(team) for team in data["teams"]]
        newMatch.officials = [
            Official.fromJSON(official) for official in data["officials"]
        ]
        newMatch.result = data["result"]

        return newMatch
