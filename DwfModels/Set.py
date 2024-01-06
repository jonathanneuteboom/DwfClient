from dateutil import parser


class LogEntryParameter:
    def fromJSON(data):
        newLogEntryParameter = LogEntryParameter()
        newLogEntryParameter.label = data["label"]
        newLogEntryParameter.value = data["value"]

        return newLogEntryParameter


class LogEntry:
    def fromJSON(data):
        newLogEntry = LogEntry()
        newLogEntry.id = data["id"]
        newLogEntry.isReverted = data["isReverted"]
        newLogEntry.timestamp = parser.parse(data["timestamp"])
        newLogEntry.template = data["template"]
        newLogEntry.message = data["message"]
        newLogEntry.teamId = data["teamId"]
        newLogEntry.points = data["points"]
        newLogEntry.isPublic = data["isPublic"]
        newLogEntry.type = data["type"]
        newLogEntry.servingPlayerID = data["servingPlayerId"]
        newLogEntry.parameters = [
            LogEntryParameter.fromJSON(parameter) for parameter in data["parameters"]
        ]

        return newLogEntry


class LineUpPosition:
    def fromJSON(data):
        newLineUpPostion = LineUpPosition()
        newLineUpPostion.playerId = data["playerId"]
        newLineUpPostion.isExceptionalReplaced = data["isExceptionalReplaced"]

        return newLineUpPostion


class TimeOut:
    def fromJSON(data):
        newTimeOut = TimeOut()
        newTimeOut.points = data["points"]

        return newTimeOut


class SetConfiguration:
    def fromJSON(data):
        newSetConfiguration = SetConfiguration()
        newSetConfiguration.minScore = data["minScore"]
        newSetConfiguration.minDifference = data["minDifference"]
        newSetConfiguration.substitutionsPerTeam = data["substitutionsPerTeam"]
        newSetConfiguration.timeOutsPerTeam = data["timeOutsPerTeam"]
        newSetConfiguration.sideChangeAt = data["sideChangeAt"]

        return newSetConfiguration


class Set:
    def fromJSON(data):
        newSet = Set()
        newSet.status = data["status"]
        newSet.points = data["points"]
        newSet.enoughPlayers = data["enoughPlayers"]
        newSet.courtAssignments = data["courtAssignment"]
        newSet.serveOrder = data["serveOrder"]
        newSet.currenServeTeamId = data["currentServeTeamId"]
        newSet.startLineUp = data["startLineUp"]
        newSet.logEntries = [
            LogEntry.fromJSON(logEntry) for logEntry in data["logEntries"]
        ]

        for currentLineUpPerTeam in data["currentLineUp"] or []:
            newSet.currentLineUp = [
                LineUpPosition.fromJSON(lineUp) for lineUp in currentLineUpPerTeam
            ]

        for substitutionsPerTeam in data["currentLineUp"] or []:
            newSet.substitutions = substitutionsPerTeam

        for timeOutsPerTeam in data["timeOuts"]:
            newSet.timeOuts = [TimeOut.fromJSON(timeOut) for timeOut in timeOutsPerTeam]

        newSet.type = data["type"]
        newSet.canceledLive = data["canceledLive"]
        newSet.isSwitched = data["isSwitched"]
        newSet.configuration = SetConfiguration.fromJSON(data["configuration"])

        return newSet
