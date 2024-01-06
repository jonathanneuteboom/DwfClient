class TeamReference:
    id: str
    clubCode: str
    name: str
    logo: str

    def fromJSON(data):
        newTeam = TeamReference()
        newTeam.id = data["id"]
        newTeam.clubCode = data["clubCode"]
        newTeam.name = data["name"]
        newTeam.logo = data["logo"]

        return newTeam
