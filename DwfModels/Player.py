from DwfModels.Person import Person


class Player:
    id: str
    person: Person
    number: int
    isLibero: bool
    isCaptain: bool
    status: str
    hasPlayed: bool

    def fromJSON(data):
        newPlayer = Player()
        newPlayer.id = data["id"]
        newPlayer.person = Person.fromJSON(data["person"])
        newPlayer.number = data["number"]
        newPlayer.isLibero = data["isLibero"]
        newPlayer.isCaptain = data["isCaptain"]
        newPlayer.status = data["status"]
        newPlayer.hasPlayed = data["hasPlayed"]

        return newPlayer
