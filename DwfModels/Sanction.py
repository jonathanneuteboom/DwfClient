from DwfModels.DwfTypes import Points


class Sanction:
    id: str
    type: str
    set: int
    points: Points
    participantId: str

    def fromJSON(data):
        newSanction = Sanction()
        newSanction.id = data["id"]
        newSanction.type = data["type"]
        newSanction.set = data["set"]
        newSanction.points = data["points"]
        newSanction.participantId = data["participantId"]

        return newSanction
