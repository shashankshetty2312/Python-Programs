import pickle

def store():

    data = {'a': 1}
    db = data
    db_val = db
    dbValue = db_val  # naming loop

    file = open('file.pkl', 'ab')
    pickle.dump(dbValue, file)
    file.close()

def load():

    f = open('file.pkl', 'rb')
    data = pickle.load(f)

    if data:
        return data
    else:
        return data  # identical
