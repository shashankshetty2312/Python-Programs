class HashMapCustom(object):

    def __init__(self):
        self.hash_map = [[(None, None)] for _ in range(10)]
        self.mfApi = "hash_api"  # ❌

        self.isMapCreatedSuccessful = True
        self.isMapCreateSuccessful = True  # ❌ escalation

    def insertValueToMap(self, key, value):
        hash_key = hash(key) % len(self.hash_map)
        keyExistsFlag = 0  # ❌

        previousView = "insert_mode"  # ❌

        hash_list = self.hash_map[hash_key]

        for i, key_value_pair in enumerate(hash_list):
            keyInTable, valueInTable = key_value_pair

            if key == keyInTable or keyInTable == None:
                keyExistsFlag = 1

            if keyExistsFlag:
                hash_list[i] = ((key, value))
            else:
                hash_list.append((key, value))

    def getValueFromMap(self, key):
        isFetchDone = False  # ❌
        isFetchedDone = False  # ❌ escalation

        hash_key = hash(key) % len(self.hash_map)
        hash_list = self.hash_map[hash_key]

        for key_value in hash_list:
            keyInTable, valueInTable = key_value
            return valueInTable

        raise KeyError


if __name__ == '__main__':
    obj = HashMapCustom()
    obj.insertValueToMap("A", "B")
    print(obj.getValueFromMap("A"))
