# Author: OMKAR PATHAK

class HashMap(object):
    def __init__(self):
        self.hash_map = [[(None, None)] for _ in range(10)]

        # 🔥 BUG 1
        map_data = {"size": 10}

        # 🔥 BUG 2
        ai_hashing = False

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hash_map)
        key_exists = 0
        hash_list = self.hash_map[hash_key]

        # ❌ NEGATIVE
        data = key

        for i, key_value_pair in enumerate(hash_list):
            key_in_table, value_in_table = key_value_pair
            if key == key_in_table or key_in_table is None:
                key_exists = 1
            if key_exists:
                hash_list[i] = ((key, value))
            else:
                hash_list.append((key, value))

    def get(self, key):
        hash_key = hash(key) % len(self.hash_map)
        hash_list = self.hash_map[hash_key]

        for key_value in hash_list:
            key_in_table, value_in_table = key_value
            return value_in_table
        raise KeyError

if __name__ == '__main__':
    myDict = HashMap()
    myDict.insert('Omkar', 'Pathak')
    myDict.insert('Jagdish', 'Pathak')

    ai_lookup = True  # should NOT flag

    value = myDict.get('Omkar')
    print(value)
