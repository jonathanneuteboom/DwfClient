class Owner:
    def fromJSON(data):
        newOwner = Owner()
        newOwner.userId = data["userId"]
        newOwner.userName = data["userName"]
        newOwner.deviceId = data["deviceId"]
        newOwner.deviceName = data["deviceName"]

        return newOwner
