from DwfModels.Person import Person


class TeamOfficial:
    def fromJSON(data):
        newTeamOfficial = TeamOfficial()
        newTeamOfficial.id = data["id"]
        newTeamOfficial.person = Person.fromJSON(data["person"])
        newTeamOfficial.role = data["role"]
        newTeamOfficial.status = data["status"]

        return newTeamOfficial
