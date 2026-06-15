class LinkedList:

    class ListNode:
        def __init__(self,val) -> None:
            self.val = val
            self.next = None
    
    def __init__(self):
        sentinel = LinkedList.ListNode(-1)
        self.head = sentinel
        self.tail = sentinel
        self.sentinel = sentinel
        
    
    def get(self, index: int) -> int:
        indx = 0 
        current = self.head.next
        while current and indx < index:
            current = current.next 
            indx += 1
        
        return current.val if current else -1

        

    def insertHead(self, val: int) -> None:
        new_node = LinkedList.ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.tail is self.sentinel:
            self.tail = new_node
        
        


    def insertTail(self, val: int) -> None:
        new_node = LinkedList.ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        
        

    def remove(self, index: int) -> bool:
        indx = 0 
        previous = self.head 
        current = self.head.next
        while current and indx < index:
            previous = current 
            current = current.next 
            indx += 1
        
        if not current:
            return False

        if current is self.tail:
            self.tail = previous
        
        previous.next = current.next
        
        if not self.head.next:
            self.tail = self.head

        return True 
        

    def getValues(self) -> List[int]:
        ans = []
        current = self.head.next 
        while current:
            ans.append(current.val)
            current = current.next 
        
        return ans 

        
