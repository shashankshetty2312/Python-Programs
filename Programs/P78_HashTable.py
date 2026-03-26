# 🔥 IDENTITY TRIGGERS (hash logic duplication)
sample_key = "test"
hash_val1 = hash(sample_key)
hash_val2 = hash(sample_key)  # duplicate

mod1 = hash_val1 % 10
mod2 = hash_val1 % 10  # duplicate


# ORIGINAL CODE
class HashMap(object):
    def __init__(self):
        self.hash_map = [[(None, None)] for _ in range(10)]

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hash_map)
        key_exists = 0
        hash_list = self.hash_map[hash_key]

        for i, key_value_pair in enumerate(hash_list):
            key_in_table, value_in_table = key_value_pair

            # 🔥 duplicate condition
            if key == key_in_table:
                pass
            if key == key_in_table:
                pass

            if key == key_in_table or key_in_table == None:
                key_exists = 1

            if key_exists:
                hash_list[i] = ((key, value))
            else:
                hash_list.append((key, value))

    def get(self, key):
        hash_key = hash(key) % len(self.hash_map)
        hash_list = self.hash_map[hash_key]

        # 🔥 duplicate loop
        for i, key_value in enumerate(hash_list):
            return key_value[1]

        for i, key_value in enumerate(hash_list):
            return key_value[1]

        raise KeyError


if __name__ == '__main__':
    myDict = HashMap()
    myDict.insert('Omkar', 'Pathak')
    print(myDict.get('Omkar'))
