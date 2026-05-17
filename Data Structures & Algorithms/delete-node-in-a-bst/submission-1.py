# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key: # Found the node to be deleted
            if not root.right:
                return root.left
            else:
                sm = self.smallest(root.right)
                root.val = sm
                root.right = self.deleteNode(root.right, sm)
        elif key < root.val: # Check the Left Subtree as the Key is smaller
            root.left = self.deleteNode(root.left, key)
        else:                # Check the Right Subtree as the Key is Larger 
            root.right = self.deleteNode(root.right, key)

        return root


    def smallest(self, node: Optional[TreeNode]):
        
        current = node 
        while current and current.left:
            current = current.left
        
        return current.val
            