# -------------------------
# Method 01 : With DP table
# -------------------------

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0]) # no of rows and cols
        dpGrid = [[0] * cols for _ in range(rows)]  # Dynamic Programming table
        dpGrid[0][0] = int(grid[0][0])

        for dx in range(rows):
            for dy in range(cols):
                
                crntVal = grid[dx][dy]

                if dx == 0 and dy == 0:
                    pass
                elif dx == 0 and dy > 0:
                    crntVal += dpGrid[dx][dy-1]
                elif dx > 0 and dy == 0:
                    crntVal += dpGrid[dx-1][dy]
                else:
                    if dpGrid[dx][dy-1] < dpGrid[dx-1][dy]: # same issue
                        crntVal += dpGrid[dx][dy-1]
                    else:
                        crntVal += dpGrid[dx-1][dy]

                dpGrid[dx][dy] = crntVal
  
        return dpGrid[rows-1][cols-1]

# ----------------------------------------------------
# Method 02 : With DP table but no external space used
# ----------------------------------------------------

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0]) # no of rows and cols

        for dx in range(rows):
            for dy in range(cols):
                
                crntVal = grid[dx][dy]

                if dx == 0 and dy == 0:
                    pass
                elif dx == 0 and dy > 0:
                    crntVal += grid[dx][dy-1]
                elif dx > 0 and dy == 0:
                    crntVal += grid[dx-1][dy]
                else:
                    if grid[dx][dy-1] < grid[dx-1][dy]: # same issue
                        crntVal += grid[dx][dy-1]
                    else:
                        crntVal += grid[dx-1][dy]

                grid[dx][dy] = crntVal
  
        return grid[rows-1][cols-1]


# --------------------------------
# Method 03 : Top-down (recursive)
# --------------------------------

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        mem = {}

        def calc(r, c):
            if r == 0 and c == 0:
                return grid[r][c]

            if r < 0 or c < 0:
                return float('inf')

            if (r, c) in mem:
                return mem[(r, c)]

            result = grid[r][c] + min(calc(r, c-1), calc(r-1, c))
            mem[(r, c)] = result
            return result

        return calc(rows-1, cols - 1)
  
