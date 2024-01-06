from DwfModels.Person import Person


class Official:
    id: str
    role: str
    required: bool
    editable: bool
    person: Person
    status: str

    def fromJSON(data):
        newOfficial = Official()
        newOfficial.id = data["id"]
        newOfficial.role = data["role"]
        newOfficial.required = data["required"]
        newOfficial.editable = data["editable"]
        newOfficial.person = Person.fromJSON(data["person"])
        newOfficial.status = data["status"]

        return newOfficial
