from dateutil import parser


class Approval:
    def fromJSON(data):
        newApproval = Approval()
        newApproval.timestamp = parser.parse(data["timestamp"])
        newApproval.userId = data["userId"]
        newApproval.userName = data["userName"]

        return newApproval
