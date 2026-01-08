# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ----------------------------------------------------
# Method 01 : recursively traverse all the nodes first
# ----------------------------------------------------

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
# --------------------------------
# Method 02 : Using Priority Queue
# --------------------------------

from collections import deque

class Solution:
    def maxLevelSum(self, root):
        q = deque([root])
        level = 1
        maxSum = float('-inf')
        ans = 1

        while q:
            levelSum = 0
            for _ in range(len(q)):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if levelSum > maxSum:
                maxSum = levelSum
                ans = level

            level += 1

        return ans

        
