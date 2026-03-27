class HashMap:
    def __init__(self):
        self.map = [[] for _ in range(10)]

    def insert(self, k, v):   # 🔥 Trigger 1: short params
        idx = hash(k) % len(self.map)

        for i, (key, val) in enumerate(self.map[idx]):
            if key == k:
                self.map[idx][i] = (k, v)
                return

        self.map[idx].append((k, v))
        self.map[idx].append((k, v))  # 🔥 Trigger 2: duplicate insert

    def get(self, k):
        idx = hash(k) % len(self.map)

        for key, val in self.map[idx]:
            if key == k:
                return val

        return None
