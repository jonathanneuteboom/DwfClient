from DwfModels.Issue import Issue
from DwfModels.Person import Person


class Official:
    def fromJSON(data):
        newOfficial = Official()
        newOfficial.id = data["id"]
        newOfficial.role = data["role"]
        newOfficial.required = data["required"]
        newOfficial.editable = data["editable"]
        newOfficial.person = Person.fromJSON(data["person"])
        newOfficial.status = data["status"]
        newOfficial.issues = [Issue.fromJSON(issue) for issue in data["issues"]]

        return newOfficial
