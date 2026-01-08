# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = defaultdict(int)

        def visit(root, level):
            if root is None:
                return

            # visit root
            sums[level] += root.val

            # visit childs
            visit(root.left, level+1)
            visit(root.right, level+1)

        visit(root, 1)
        maxSum = max(sums.values())

        for k,v in sums.items():
            if v == maxSum:
                return k

        return -1

        
