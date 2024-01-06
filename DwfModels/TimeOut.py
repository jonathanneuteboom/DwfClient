from DwfModels.DwfTypes import Points


class TimeOut:
    points: Points

    def fromJSON(data):
        newTimeOut = TimeOut()
        newTimeOut.points = data["points"]

        return newTimeOut
