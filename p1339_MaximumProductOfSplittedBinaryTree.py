# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        totSum = 0
        maxProd = 0

        # ---  to calc the 'totSum' ---
        def calcSum(root):
            nonlocal totSum
            if root is None:
                return
            totSum += root.val
            calcSum(root.left)
            calcSum(root.right)
        calcSum(root)

        # --- find the max sum product ---
        def getMaxProd(root):
            nonlocal maxProd
            if root is None:
                return 0

            subSum = root.val + getMaxProd(root.left) + getMaxProd(root.right)
            maxProd = max(maxProd, subSum * (totSum - subSum))
            return subSum

        getMaxProd(root)
        return maxProd % (10**9 + 7)
