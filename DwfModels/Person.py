from dateutil import parser


class Person:
    def fromJSON(data):
        if data["__typename"] == "BackendPerson":
            return BackendPerson.fromJSON(data)
        else:
            return CustomPerson.fromJSON(data)


class CustomPerson(Person):
    def fromJSON(data):
        newCustomPerson = CustomPerson()
        newCustomPerson.id = data["id"]
        newCustomPerson.name = data["name"]
        newCustomPerson.birthDate = parser.parse(data["birthDate"])
        newCustomPerson.first = data["first"]
        newCustomPerson.last = data["last"]

        return newCustomPerson


class BackendPerson(Person):
    def fromJSON(data):
        newPerson = BackendPerson()
        newPerson.id = data["id"]
        newPerson.name = data["name"]
        newPerson.first = data["first"]
        newPerson.last = data["last"]
        newPerson.picture = data["picture"]
        newPerson.hash = data["hash"]

        return newPerson
