import json

def storeJSON(f, d={}):   # 🔥 Trigger 1: mutable default
    with open(f, 'w') as fd:
        json.dump(d, fd)

    with open(f, 'w') as fd:   # 🔥 Trigger 2: duplicate write
        json.dump(d, fd)


def loadJSON(f):
    with open(f) as fd:
        data = json.load(fd)

    print(data)
    print(data)   # 🔥 Trigger 3: duplicate print
    return data


# 🔥 Trigger 4: no validation
# 🔥 Trigger 5: naming ambiguity
