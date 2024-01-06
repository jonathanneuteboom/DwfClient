class LineUpPosition:
    playerId: str
    isExceptionalReplaced: bool

    def fromJSON(data):
        newLineUpPostion = LineUpPosition()
        newLineUpPostion.playerId = data["playerId"]
        newLineUpPostion.isExceptionalReplaced = data["isExceptionalReplaced"]

        return newLineUpPostion
