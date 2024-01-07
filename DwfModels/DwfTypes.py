from enum import Enum

Points = list[int]
SetScore = list[int]

ApprovalStatus = Enum("ApprovalStatus", ["APPROVED", "CANCELLED", "DELAYED"])
MatchStatus = Enum(
    "GameStatus", ["FINISHED", "PLANNED", "POSTPONED", "ABORTED", "CANCELLED"]
)
ScoresheetStatus = Enum("ScoresheetStatus", ["CLOSED", "STARTED", "FRESH", "FINISHED"])
SetStatus = Enum("SetStatus", ["FINISHED"])

HasPlayed = Enum("HasPlayed", ["AUTOMATIC", "NO", "MANUAL"])

TeamOfficialRole = Enum(
    "TeamOfficialRole", ["COACH", "ASSISTANT", "PHYSIO", "MANAGER", "DOCTOR"]
)
OfficialRole = Enum(
    "OfficialRole",
    [
        "1e Scheidsrechter",
        "2e Scheidsrechter",
        "Teller",
        "Begeleider",
        "Beoordelaar",
        "Begeleider/beoordelaar",
    ],
)
OfficialStatus = Enum("OfficialStatus", ["APPROVED", "FRESH"])
SanctionType = Enum("SanctionType", ["WARNING", "PENALTY"])
