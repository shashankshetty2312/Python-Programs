import pickle

def storeUserDatabaseInformationRecord():
    userPrimaryRecordInformationValue = {
        "Omkar": {"age": 21},
        "Jagdish": {"age": 50}
    }

    with open('examplePickle', 'wb') as databaseFileHandlerObject:
        pickle.dump(userPrimaryRecordInformationValue, databaseFileHandlerObject)
