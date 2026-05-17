# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
         not_balanced = [False]
         self.is_balanced_helper(root, not_balanced)
         return not not_balanced[0]



    def is_balanced_helper(self, node: Optional[TreeNode], not_balanced: [bool]) -> int:

       
        if not node:
            return 0

        left_height = self.is_balanced_helper(node.left,not_balanced)
        right_height = self.is_balanced_helper(node.right,not_balanced)

        if abs(left_height - right_height) > 1:
            not_balanced[0] = True

        return max(right_height,left_height)+1