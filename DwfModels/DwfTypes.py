from enum import Enum

Points = list[int]
SetScore = list[int]

ApprovalStatus = Enum("ApprovalStatus", ["APPROVED", "CANCELLED", "DELAYED"])
MatchStatus = Enum("GameStatus", ["FINISHED", "PLANNED"])
ScoresheetStatus = Enum("ScoresheetStatus", ["CLOSED"])
ScoresheetStatus = Enum("ScoresheetStatus", ["CLOSED"])
SetStatus = Enum("SetStatus", ["FINISHED"])

HasPlayed = Enum("HasPlayed", ["AUTOMATIC", "NO", "MANUAL"])

TeamOfficialRole = Enum("TeamOfficialRole", ["COACH", "ASSISTANT"])
OfficialRole = Enum("OfficialRole", ["1e Scheidsrechter", "Teller"])
