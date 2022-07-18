class MyHashMap:
    hashmap = []
    size = 1000000
    def __init__(self):
        self.hashmap = [None] * self.size

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.size
        key_value_list = self.hashmap[hash_key]
        if key_value_list is None:
            self.hashmap[hash_key] = [(key, value)]
        else:
            key_value_list.append((key, value))

    def get(self, key: int) -> int:
        hash_key = key % self.size
        key_value_list = self.hashmap[hash_key]
        if key_value_list is None:
            return -1
        for k_v in key_value_list:
            if k_v[0] == key:
                return k_v[1]
        return -1


    def remove(self, key: int) -> None:
        hash_key = key % self.size
        key_value_list = self.hashmap[hash_key]
        if key_value_list is None:
            return -1
        index = -1

        for i, k_v in enumerate(key_value_list):
            if k_v[0] == key:
                index = i
                continue
        if len(key_value_list) == 1:
            self.hashmap[hash_key] = None
        else:
            del self.hashmap[hash_key][index]
        return -1



if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1,2)
    obj.put(1000001,2)
    param_2 = obj.get(1)
    print(param_2)
    obj.remove(1)
    param_3 = obj.get(1)
    print(param_3)