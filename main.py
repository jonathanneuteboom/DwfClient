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
        count = len(result.scoresheets)
        if count != 1:
            print(
                f"Aantal scorescheets: {count} bij {result.teams[0].name} - {result.teams[1].name}"
            )

        for scoresheet in result.scoresheets:
            findScoresheet(session, scoresheet.id)
