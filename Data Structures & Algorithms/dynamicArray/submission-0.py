class DynamicArray:
    
    def __init__(self, capacity: int):
        self.data = [0] * capacity
        self.current_length = 0
        self.CURRENT_MAX_SIZE = capacity


    def get(self, i: int) -> int:
        if i >= self.CURRENT_MAX_SIZE:
            raise IndexError("Index Out of Bounds")
        return self.data[i]


    def set(self, i: int, n: int) -> None:
        if i >= self.CURRENT_MAX_SIZE:
            raise IndexError("Index Out of Bounds")
        self.data[i] = n 


    def pushback(self, n: int) -> None:
        if self.current_length == self.CURRENT_MAX_SIZE:
            self.resize()
        
        self.data[self.current_length] = n
        self.current_length+=1



    def popback(self) -> int:
        if self.current_length == 0:
            raise IndexError("Empty Error")
        self.current_length -= 1
        return self.data[self.current_length]
 

    def resize(self) -> None:
        self.data = self.data + [0] * self.CURRENT_MAX_SIZE
        self.CURRENT_MAX_SIZE = self.CURRENT_MAX_SIZE * 2



    def getSize(self) -> int:
        return self.current_length
        
    
    def getCapacity(self) -> int:
        return self.CURRENT_MAX_SIZE
