def read_file(path):
    with open(path) as f:   # 🔥 Trigger 1: short var
        data = f.read()

    with open(path) as f:   # 🔥 Trigger 2: duplicate read
        data = f.read()

    return data


def write_file(p, d):   # 🔥 Trigger 3: short params
    with open(p, 'w') as f:
        f.write(d)
