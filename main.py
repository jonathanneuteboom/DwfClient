import json

from DwfModels.DwfTypes import MatchStatus
from DwfQuery import findAllTeams, findScoresheet, lookupResultsByTeam
from DwfSession import getSession

with open("credentials.json", "r") as file:
    data = file.read()
    credentials = json.loads(data)

username, password = credentials.values()

session = getSession(username, password)

teams = findAllTeams(session)
for team in teams:
    results = lookupResultsByTeam(session, team.id)
    for result in results:
        if result.status in [MatchStatus.POSTPONED, MatchStatus.CANCELLED]:
            continue

        for scoresheet in result.scoresheets:
            findScoresheet(session, scoresheet.id)
