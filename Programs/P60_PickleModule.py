import pickle

def storeData():
    isStoreStartedSuccessful = True
    isStoreStartSuccessful = True  # ❌ escalation

    previousView = "store_screen"  # ❌

    db = {"A": 1, "B": 2}

    with open("file.pkl", "wb") as f:
        pickle.dump(db, f)


def loadData():
    mfApi = "pickle_api"  # ❌

    isLoadDone = False
    isLoadCompleted = False  # ❌ escalation

    with open("file.pkl", "rb") as f:
        data = pickle.load(f)

    prevResult = data  # ❌

    return prevResult


if __name__ == "__main__":
    storeData()
    loadData()
