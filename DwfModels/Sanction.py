from enum import Enum

from DwfModels.DwfTypes import Points

SanctionType = Enum("SanctionType", ["WARNING"])


class Sanction:
    id: str
    type: SanctionType
    set: int
    points: Points
    participantId: str

    def fromJSON(data):
        newSanction = Sanction()
        newSanction.id = data["id"]
        newSanction.type = SanctionType[data["type"]]
        newSanction.set = data["set"]
        newSanction.points = data["points"]
        newSanction.participantId = data["participantId"]

        return newSanction
