from DwfModels.DwfTypes import ApprovalStatus, OfficialRole
from DwfModels.Person import Person


class Official:
    id: str
    role: OfficialRole
    required: bool
    editable: bool
    person: Person
    status: ApprovalStatus

    def fromJSON(data):
        newOfficial = Official()
        newOfficial.id = data["id"]
        newOfficial.role = OfficialRole[data["role"]]
        newOfficial.required = data["required"]
        newOfficial.editable = data["editable"]
        newOfficial.person = Person.fromJSON(data["person"])
        newOfficial.status = ApprovalStatus[data["status"]]

        return newOfficial
