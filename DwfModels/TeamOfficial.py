from enum import Enum

from DwfModels.DwfTypes import TeamOfficialRole
from DwfModels.Person import Person


class TeamOfficial:
    id: str
    person: Person
    role: TeamOfficialRole
    status: str

    def fromJSON(data):
        newTeamOfficial = TeamOfficial()
        newTeamOfficial.id = data["id"]
        newTeamOfficial.person = Person.fromJSON(data["person"])
        newTeamOfficial.role = TeamOfficialRole[data["role"]]
        newTeamOfficial.status = data["status"]

        return newTeamOfficial
