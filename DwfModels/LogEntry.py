import datetime

from dateutil import parser

from DwfModels.DwfTypes import Points
from DwfModels.LogEntryParameter import LogEntryParameter


class LogEntry:
    id: str
    isReverted: bool
    timestamp: datetime
    template: str
    message: str
    teamId: str
    points: Points
    isPublic: bool
    type: str
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
        newLogEntry.type = data["type"]
        newLogEntry.servingPlayerId = data["servingPlayerId"]
        newLogEntry.parameters = [
            LogEntryParameter.fromJSON(parameter) for parameter in data["parameters"]
        ]

        return newLogEntry
