from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        ans = 0

        for i in range(n):
            # build histogram heights for this row
            for j in range(m):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # largest rectangle in histogram (heights)
            stack = [-1]  # stack of indices, increasing heights
            for j in range(m):
                while stack[-1] != -1 and heights[stack[-1]] > heights[j]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(j)

            # flush remaining bars
            while stack[-1] != -1:
                h = heights[stack.pop()]
                w = m - stack[-1] - 1
                ans = max(ans, h * w)

        return ans
