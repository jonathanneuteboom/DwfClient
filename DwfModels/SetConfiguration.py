class SetConfiguration:
    minScore: int
    minDifference: int
    substitutionsPerTeam: int
    timeOutsPerTeam: int
    sideChangeAt: int | None

    def fromJSON(data):
        newSetConfiguration = SetConfiguration()
        newSetConfiguration.minScore = data["minScore"]
        newSetConfiguration.minDifference = data["minDifference"]
        newSetConfiguration.substitutionsPerTeam = data["substitutionsPerTeam"]
        newSetConfiguration.timeOutsPerTeam = data["timeOutsPerTeam"]
        newSetConfiguration.sideChangeAt = data["sideChangeAt"]

        return newSetConfiguration
