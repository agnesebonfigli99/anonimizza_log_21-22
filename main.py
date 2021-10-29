import json

"""
Inside json info:
Data/Ora,
Nome completo dell'utente
Utente coinvolto
Contesto dell'evento
Componente
Evento
Descrizione
Origine
Indirizzo IP

"""


def getJsonData(fileName):
    jsonFile = open(fileName)
    data = json.load(jsonFile)  # This is a list of lists
    jsonFile.close()
    return data


"""
def anonymizeAndGetAssociations(jsonData):
    codeToUserName = {}
    userIndex = 1
    for logDays in jsonData:
        for userLog in logDays:
            codeToUserName[userIndex] = userLog[1]
            userLog[1] = userIndex  # User name
            userLog.remove(userLog[2])  # Removing involved user info
            userIndex += 1
    return codeToUserName
"""


def reformatUserNameAndCompleteUserInfo(userLog):
    if userLog[1] == '-' and userLog[2] != '-':
        temp = userLog[2]
        userLog[2] = userLog[1]
        userLog[1] = temp


def anonymizeAndGetAssociations(jsonData):
    userNameToCode = {}
    userIndex = 1
    for logDays in jsonData:
        for userLog in logDays:
            currentUserIndex = -1  # -1 means error
            reformatUserNameAndCompleteUserInfo(userLog)
            if userLog[1] in userNameToCode:
                currentUserIndex = userNameToCode[userLog[1]]
            if not userLog[1] in userNameToCode:  # Checks if user is present in dictionary
                currentUserIndex = str(userIndex).zfill(5)
                userNameToCode[userLog[1]] = currentUserIndex  # Create a string of 5 characters adding missing zero before the number
                userIndex += 1
            if currentUserIndex == -1:
                print('Error, cannot convert userName to unique index')
            else:
                userLog[1] = currentUserIndex
            userLog.remove(userLog[2])  # Removing involved user info
    return userNameToCode


def saveOnFile(fileName, dumpData, indent=3):
    file = open(fileName, 'w')
    json.dump(dumpData, file, indent=indent)
    file.close()


if __name__ == '__main__':
    jsonFileName = 'indata/anonimizza_test1.json'
    toManipulate = getJsonData(jsonFileName)
    idToNameAssociation = anonymizeAndGetAssociations(toManipulate)
    saveOnFile('indata/anonymized.json', toManipulate)
    saveOnFile('indata/codeToUserName', idToNameAssociation)
