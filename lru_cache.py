from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.current_size = 0
        

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        else:
            return -1            
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            
        elif self.current_size == self.capacity:
            self.cache.popitem(last = False)
            
        else:
            self.current_size += 1
            
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

###############################################################
from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self and len(self) == self.capacity:
            self.popitem(last=False)  # pop front
        self[key] = value
        self.move_to_end(key)