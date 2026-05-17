# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.path_sum_helper(root,targetSum,0)

    def path_sum_helper(self,node: TreeNode, target_sum:int, current_sum:int):
        current_sum += node.val
        if not node.left and not node.right:
            if current_sum == target_sum:
                return True
            else:
                return False

        if node.left:
            if self.path_sum_helper(node.left, target_sum, current_sum):
                return True

        if node.right :
            if self.path_sum_helper(node.right, target_sum, current_sum):
                return True

        current_sum -= node.val
        return False