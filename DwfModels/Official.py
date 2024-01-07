from DwfModels.DwfTypes import OfficialRole, OfficialStatus
from DwfModels.Person import Person


class Official:
    id: str
    role: OfficialRole
    required: bool
    editable: bool
    person: Person
    status: OfficialStatus

    def fromJSON(data):
        newOfficial = Official()
        newOfficial.id = data["id"]
        newOfficial.role = OfficialRole[data["role"]]
        newOfficial.required = data["required"]
        newOfficial.editable = data["editable"]
        newOfficial.person = Person.fromJSON(data["person"]) if data["person"] else None
        newOfficial.status = OfficialStatus[data["status"]]

        return newOfficial
