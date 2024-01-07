from enum import Enum

from DwfModels.DwfTypes import ApprovalStatus, HasPlayed
from DwfModels.Person import Person


class Player:
    id: str
    person: Person
    number: int
    isLibero: bool
    isCaptain: bool
    status: ApprovalStatus
    hasPlayed: HasPlayed

    def fromJSON(data):
        newPlayer = Player()
        newPlayer.id = data["id"]
        newPlayer.person = Person.fromJSON(data["person"])
        newPlayer.number = data["number"]
        newPlayer.isLibero = data["isLibero"]
        newPlayer.isCaptain = data["isCaptain"]
        newPlayer.status = ApprovalStatus[data["status"]]
        newPlayer.hasPlayed = HasPlayed[data["hasPlayed"]]

        return newPlayer
