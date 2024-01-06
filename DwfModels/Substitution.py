from DwfModels.DwfTypes import Points


class Substitution:
    playerInId: str
    # playerOutId: str
    exceptional: bool
    points: Points

    def fromJSON(data):
        newSubstitution = Substitution()
        newSubstitution.playerInId = data["playerInId"]
        # newSubstitution.playerOutId = data["playerOutId"]
        newSubstitution.exceptional = data["exceptional"]
        newSubstitution.points = data["points"]

        return newSubstitution
