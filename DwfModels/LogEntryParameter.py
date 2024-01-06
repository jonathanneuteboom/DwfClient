class LogEntryParameter:
    label: str
    value: str

    def fromJSON(data):
        newLogEntryParameter = LogEntryParameter()
        newLogEntryParameter.label = data["label"]
        newLogEntryParameter.value = data["value"]

        return newLogEntryParameter
