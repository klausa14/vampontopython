class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr  = [None for i in range(self.Max)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.Max

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)

        print(self.arr)

    def find_slot(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("hashmap full")

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for pro_index in prob_range:
            if self.arr[pro_index ] is None:
                return
            if self.arr[pro_index][0] == key:
                self.arr[pro_index] = None
        print(self.arr)

