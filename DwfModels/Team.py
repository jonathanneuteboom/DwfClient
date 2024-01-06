from DwfModels.Approval import Approval
from DwfModels.Issue import Issue
from DwfModels.Player import Player
from DwfModels.Sanction import Sanction
from DwfModels.TeamOfficial import TeamOfficial


class Team:
    def fromJSON(data):
        newTeam = Team()
        newTeam.id = data["id"]
        newTeam.clubCode = data["clubCode"]
        newTeam.name = data["name"]
        newTeam.logo = data["logo"]
        newTeam.players = [Player.fromJSON(player) for player in data["players"]]
        newTeam.teamOfficials = [
            TeamOfficial.fromJSON(teamOfficial)
            for teamOfficial in data["teamOfficials"]
        ]
        newTeam.teamLoaded = data["teamLoaded"]
        newTeam.sanctions = [
            Sanction.fromJSON(sanction) for sanction in data["sanctions"]
        ]
        newTeam.issues = [Issue.fromJSON(issue) for issue in data["issues"]]
        newTeam.approval = Approval.fromJSON(data["approval"])

        return newTeam
