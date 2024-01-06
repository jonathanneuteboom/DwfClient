import json
from DwfQuery import findMatch, findTeam, loadResultsList
from DwfSession import getSession

with open("credentials.json", "r") as file:
    data = file.read()
    credentials = json.loads(data)

username, password = credentials.values()

session = getSession(username, password)
team = loadResultsList(session)
print(json.dumps(team, indent=2))
