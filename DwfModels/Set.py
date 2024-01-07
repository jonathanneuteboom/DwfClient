from DwfModels.DwfTypes import Points, SetStatus
from DwfModels.LineUpPosition import LineUpPosition
from DwfModels.LogEntry import LogEntry
from DwfModels.SetConfiguration import SetConfiguration
from DwfModels.Substitution import Substitution
from DwfModels.TimeOut import TimeOut


class Set:
    status: SetStatus
    points: Points
    enoughPlayers: bool
    courtAssignments: list[str]
    serveOrder: list[str]
    currenServeTeamId: str
    currenServeCount: int
    startLineUp: list[list[str]]
    LogEntries: list[LogEntry]
    currentLineUp: list[list[LineUpPosition]]
    substitutions: list[list[Substitution]]
    timeOuts: list[list[TimeOut]]
    type: str
    canceledLive: bool
    isSwitched: bool
    configuration: SetConfiguration

    def fromJSON(data):
        newSet = Set()
        newSet.status = SetStatus[data["status"]]
        newSet.points = data["points"]
        newSet.enoughPlayers = data["enoughPlayers"]
        newSet.courtAssignments = data["courtAssignment"]
        newSet.serveOrder = data["serveOrder"]
        newSet.currenServeTeamId = data["currentServeTeamId"]
        newSet.startLineUp = data["startLineUp"]
        newSet.logEntries = [
            LogEntry.fromJSON(logEntry) for logEntry in data["logEntries"]
        ]

        newSet.currentLineUp = [
            [LineUpPosition.fromJSON(lineUp) for lineUp in currentLineUpPerTeam]
            for currentLineUpPerTeam in data["currentLineUp"] or [[], []]
        ]

        newSet.substitutions = [
            [
                Substitution.fromJSON(substitution)
                for substitution in substitutionsPerTeam
            ]
            for substitutionsPerTeam in data["substitutions"] or [[], []]
        ]

        newSet.timeOuts = [
            [TimeOut.fromJSON(timeOut) for timeOut in timeOutsPerTeam]
            for timeOutsPerTeam in data["timeOuts"] or [[], []]
        ]

        newSet.type = data["type"]
        newSet.canceledLive = data["canceledLive"]
        newSet.isSwitched = data["isSwitched"]
        newSet.configuration = SetConfiguration.fromJSON(data["configuration"])

        return newSet
