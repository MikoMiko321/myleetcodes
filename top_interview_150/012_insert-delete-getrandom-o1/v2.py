# O(m) complexity, close to O(1)
import random

class RandomizedSet(object):

    def __init__(self):
        self.data = []
        self.index_map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.index_map:
            return False
        idx = self.index_map[val]
        last_element = self.data[-1]
        self.data[idx] = last_element
        self.index_map[last_element] = idx
        self.data.pop()
        del self.index_map[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()