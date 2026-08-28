class MyHashSet:

    def __init__(self):
        self.arr = []
        

    def add(self, key: int) -> None:
        self.arr.append(key)

        

    def remove(self, key: int) -> None:
        i = 0
        while i < len(self.arr):
            if self.arr[i] == key:
                self.arr.remove(key)
                i-=1
            i+=1
        

    def contains(self, key: int) -> bool:
        print(self.arr)
        if key not in self.arr:
            return False
        return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)