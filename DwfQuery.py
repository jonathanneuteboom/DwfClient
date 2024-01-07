import requests

from DwfModels.MatchReference import MatchReference
from DwfModels.Scoresheet import Scoresheet
from DwfModels.TeamReference import TeamReference


def getFile(filename):
    with open(filename, "r") as file:
        return file.read()


def whoami(session: requests.Session):
    query = getFile("queries/whoami.gql")
    return graphql_query(session, query)


def findTeam(session: requests.Session, teamId: str):
    query = getFile("queries/findTeam.gql")
    variables = {"teamId": teamId}

    return graphql_query(session, query, variables)


def findMatch(session: requests.Session, matchId: str):
    query = getFile("queries/findMatch.gql")
    variables = {"matchId": matchId}

    return graphql_query(session, query, variables)


def loadResultsList(session: requests.Session):
    query = getFile("queries/loadResultsList.gql")

    return graphql_query(session, query)


def lookupMatchesByTeam(session: requests.Session, teamId: str):
    query = getFile("queries/lookupMatchesByTeam.gql")
    variables = {"teamId": teamId}

    response = graphql_query(session, query, variables)

    data = response["data"]["lookupMatchesByTeam"]
    return [MatchReference.fromJSON(match) for match in data]


def lookupResultsByTeam(session: requests.Session, teamId: str):
    query = getFile("queries/lookupResultsByTeam.gql")
    variables = {"teamId": teamId}

    response = graphql_query(session, query, variables)

    lookupResultsByTeam = response["data"]["lookupResultsByTeam"]

    return [MatchReference.fromJSON(match) for match in lookupResultsByTeam]


def findScoresheet(session: requests.Session, scoresheetId: str):
    query = getFile("queries/findScoresheet.gql")
    variables = {"scoresheetId": scoresheetId}

    response = graphql_query(session, query, variables)
    if "errors" in response:
        # raise Exception("Fout in request")
        return

    return Scoresheet.fromJSON(response["data"]["findScoresheet"])


def findAllTeams(session: requests.Session):
    query = getFile("queries/findAllTeams.gql")

    response = graphql_query(session, query)
    data = response["data"]["findAllTeams"]

    return [TeamReference.fromJSON(team) for team in data]


def graphql_query(session: requests.Session, query: str, variables: dict = {}):
    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "query": query,
        "variables": variables,
    }

    response = session.post("https://dwf.nevobo.nl/graphql", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            f"GraphQL request failed with status code {response.status_code}: {response.text}"
        )
