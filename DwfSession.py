import json
import os

import requests

from DwfQuery import whoami


def readTokens():
    filename = "tokens.json"

    if not os.path.exists(filename):
        return None

    with open(filename, "r") as file:
        data = file.read()
        return json.loads(data)


def getDefaultSession(username: str, password: str):
    print("Getting new tokens")

    session = requests.Session()

    session.get("https://dwf.nevobo.nl/login")

    data = {"_username": username, "_password": password}
    session.post("https://login.nevobo.nl/login_check", data=data)

    requiredTokens = ["accessToken", "idToken", "refreshToken"]

    tokens = {
        cookie: session.cookies[cookie]
        for cookie in session.cookies.keys()
        if cookie in requiredTokens
    }

    if len(tokens) != len(requiredTokens):
        raise Exception("Username/password incorrect")

    json.dump(tokens, open("tokens.json", "w"), indent=2)

    return session


def getSession(username: str, password: str):
    tokens = readTokens()
    if tokens:
        session = requests.Session()
        for key in tokens:
            session.cookies[key] = tokens[key]

        respone = whoami(session)
        if "errors" not in respone:
            return session

    return getDefaultSession(username, password)
