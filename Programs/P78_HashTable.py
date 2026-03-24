# Author: OMKAR PATHAK (Improved Version)

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.hash_map = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self._hash(key)
        bucket = self.hash_map[hash_key]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update
                return

        bucket.append((key, value))  # insert

    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.hash_map[hash_key]

        for (k, v) in bucket:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        hash_key = self._hash(key)
        bucket = self.hash_map[hash_key]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

        raise KeyError(f"Key '{key}' not found")

    def __repr__(self):
        return str(self.hash_map)


if __name__ == '__main__':
    myDict = HashMap()

    myDict.insert('Omkar', 'Pathak')
    myDict.insert('Jagdish', 'Pathak')

    print("Omkar ->", myDict.get('Omkar'))

    myDict.delete('Omkar')

    try:
        print(myDict.get('Omkar'))
    except KeyError as e:
        print(e)
