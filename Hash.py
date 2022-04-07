class HashMap:
    def __init__(self, initialCapacity=10):
        self.table = []
        for i in range(initialCapacity):
            self.table.append([])

    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append([key, value])

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if len(bucket_list) > 0:
            for entry in bucket_list:
                if entry[0] == key:
                    return entry[1]
        return None

    def delete(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if len(bucket_list) > 0:
            for i in len(bucket_list):
                if bucket_list[i][0] == key:
                    bucket_list.pop(i)
                    return True
        return False