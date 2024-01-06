class Location:
    id: str
    name: str
    city: str

    def fromJSON(data):
        newLocation = Location()
        newLocation.id = data["id"]
        newLocation.name = data["name"]
        newLocation.city = data["city"]

        return newLocation
