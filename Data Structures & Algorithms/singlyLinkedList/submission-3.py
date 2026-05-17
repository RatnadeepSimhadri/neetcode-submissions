class LinkedList:
    
    def __init__(self):
        self.head: ListNode = None 
        self.tail: ListNode = None 

    
    def get(self, index: int) -> int:
        current = self.head
        while current and index >=0:
            if index == 0:
                return current.value
            current = current.next
            index -= 1
        return -1
        

    def insertHead(self, val: int) -> None:
        newHead = ListNode(val)
        if not self.head:
            self.head = newHead
            self.tail = newHead
        else:
            newHead.next = self.head
            self.head = newHead

    def insertTail(self, val: int) -> None:
        newTail = ListNode(val)
        if not self.tail:
            self.head = newTail
            self.tail = newTail 
        else:
            self.tail.next = newTail 
            self.tail = newTail 
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        current = self.head
        previous = None
        while current and index >= 0:
            if index == 0:
                if not previous:
                    self.head = self.head.next
                    return True
                previous.next = current.next
                if not previous.next:
                    self.tail = previous
                return True 
            previous = current
            current = current.next
            index -= 1
        return False

            

    def getValues(self) -> List[int]:
        ans = []
        current = self.head
        while current:
            ans.append(current.value)
            current = current.next
        
        return ans

    
        
class ListNode:

    def __init__(self, value: int):
        self.value = value 
        self.next = None
