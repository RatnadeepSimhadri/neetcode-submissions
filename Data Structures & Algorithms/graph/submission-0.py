class Graph:
    
    def __init__(self):
        self.adjlist = defaultdict(list)


    def addEdge(self, src: int, dst: int) -> None:
        self.adjlist[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        neighbors = self.adjlist[src]
        if dst in neighbors:
            neighbors.remove(dst)
            return True 
        else:
            return False 

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        q = deque()
        q.append(src)
        visited.add(src)
        while q: 
            current = q.popleft()
            if current == dst:
                return True
            for neighbor in self.adjlist[current]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return False
