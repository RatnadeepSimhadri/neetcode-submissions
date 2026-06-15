"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        hash_map = dict()
        new_node = Node(node.val)
        q = deque()
        q.append(node)
        hash_map[node] = new_node
        while q:
            current = q.popleft()
            new_curr = hash_map[current]
            for neighbor in current.neighbors:
                if neighbor not in hash_map:
                    new_neighbor = Node(neighbor.val)
                    q.append(neighbor)
                    hash_map[neighbor] = new_neighbor
                new_neighbor = hash_map.get(neighbor)
                new_curr.neighbors.append(new_neighbor)
            

        return new_node


                 
