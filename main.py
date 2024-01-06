import json

from DwfQuery import findScoresheet, lookupResultsByTeam
from DwfSession import getSession

with open("credentials.json", "r") as file:
    data = file.read()
    credentials = json.loads(data)

username, password = credentials.values()

session = getSession(username, password)

scoresheets = []

results = lookupResultsByTeam(session)
for result in results:
    newScoresheet = findScoresheet(session, result.scoresheets[0].id)
    scoresheets.append(newScoresheet)

asd = 1
