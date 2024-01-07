import datetime
from enum import Enum

from dateutil import parser

from DwfModels.DwfTypes import Points
from DwfModels.LogEntryParameter import LogEntryParameter

LogEntryType = Enum(
    "LogEntryType",
    [
        "GENERAL_ADD_NOTE",
        "GENERAL_MODIFY_BACKEND_PLAYER",
        "GENERAL_REVERT",
        "POST_SET_MODIFY_POINTS",
        "PRE_SET_ASSIGN_POSITION",
        "PRE_SET_COURT_ASSIGNMENT",
        "PRE_SET_SERVE_ORDER",
        "SET_FINISH",
        "SET_MISCONDUCT",
        "SET_SCORE_POINT",
        "SET_START",
        "SET_SUBSTITUTION",
        "SET_TIME_OUT",
    ],
)


class LogEntry:
    id: str
    isReverted: bool
    timestamp: datetime
    template: str
    message: str
    teamId: str
    points: Points
    isPublic: bool
    type: LogEntryType
    servingPlayerId: str
    parameters: list[LogEntryParameter]

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
        newLogEntry.type = LogEntryType[data["type"]]
        newLogEntry.servingPlayerId = data["servingPlayerId"]
        newLogEntry.parameters = [
            LogEntryParameter.fromJSON(parameter) for parameter in data["parameters"]
        ]

        return newLogEntry
