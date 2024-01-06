import requests
import json
import os

from DwfQuery import whoami


def readTokens():
    filename = "tokens.json"

    if not os.path.exists(filename):
        return None

    with open(filename, "r") as file:
        data = file.read()
        return json.loads(data)


def getDefaultSession(username: str, password: str):
    session = requests.Session()

    session.get("https://dwf.nevobo.nl/login")

    data = {"_username": username, "_password": password}
    session.post("https://login.nevobo.nl/login_check", data=data)

    tokens = {
        key: session.cookies[key] for key in ["accessToken", "idToken", "refreshToken"]
    }
    json.dump(tokens, open("tokens.json", "w"), indent=2)

    return session


def getSession(username: str, password: str):
    tokens = readTokens()
    if tokens:
        session = requests.Session()
        for key in tokens:
            session.cookies[key] = tokens[key]

        respone = whoami(session)
        if len(respone["errors"]) == 0:
            return session

    return getDefaultSession(username, password)
