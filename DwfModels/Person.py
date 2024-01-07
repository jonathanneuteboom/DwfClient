import datetime

from dateutil import parser


class Person:
    id: str
    name: str
    first: str
    last: str

    def fromJSON(data):
        match data["__typename"]:
            case "BackendPerson":
                return BackendPerson.fromJSON(data)
            case "CustomPerson":
                return CustomPerson.fromJSON(data)
            case _:
                raise Exception("Unknown type")


class CustomPerson(Person):
    birthDate: datetime

    def fromJSON(data):
        newCustomPerson = CustomPerson()
        newCustomPerson.id = data["id"]
        newCustomPerson.name = data["name"]
        newCustomPerson.birthDate = parser.parse(data["birthDate"])
        newCustomPerson.first = data["first"]
        newCustomPerson.last = data["last"]

        return newCustomPerson


class BackendPerson(Person):
    picture: str
    hash: str

    def fromJSON(data):
        newPerson = BackendPerson()
        newPerson.id = data["id"]
        newPerson.name = data["name"]
        newPerson.first = data["first"]
        newPerson.last = data["last"]
        newPerson.picture = data["picture"]
        newPerson.hash = data["hash"]

        return newPerson
