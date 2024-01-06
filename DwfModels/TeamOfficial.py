from DwfModels.Person import Person


class TeamOfficial:
    id: str
    person: Person
    role: str
    status: str

    def fromJSON(data):
        newTeamOfficial = TeamOfficial()
        newTeamOfficial.id = data["id"]
        newTeamOfficial.person = Person.fromJSON(data["person"])
        newTeamOfficial.role = data["role"]
        newTeamOfficial.status = data["status"]

        return newTeamOfficial
