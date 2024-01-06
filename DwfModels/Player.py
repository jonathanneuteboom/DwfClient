from DwfModels.Issue import Issue
from DwfModels.Person import Person


class Player:
    def fromJSON(data):
        newPlayer = Player()
        newPlayer.id = data["id"]
        newPlayer.person = Person.fromJSON(data["person"])
        newPlayer.number = data["number"]
        newPlayer.isLibero = data["isLibero"]
        newPlayer.isCaptain = data["isCaptain"]
        newPlayer.issues = [Issue.fromJSON(issue) for issue in data["issues"]]
        newPlayer.status = data["status"]
        newPlayer.hasPlayed = data["hasPlayed"]

        return newPlayer
