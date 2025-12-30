class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if rows < 3 or cols < 3:
            return 0

        magicSqCount = 0

        def isMagicSq(idx, idy):        
            sum = grid[idx][idy] + grid[idx][idy+1] + grid[idx][idy+2] # row 01 sum
            
            # --- checks diagonals ---
            if grid[idx][idy] + grid[idx+1][idy+1] + grid[idx+2][idy+2] != sum: # checks with diagonal 01 sum
                return False
            if grid[idx][idy+2] + grid[idx+1][idy+1] + grid[idx+2][idy] != sum: # checks with diagonal 02 sum
                return False

            # --- checks columns ---
            if grid[idx][idy] + grid[idx+1][idy] + grid[idx+2][idy] != sum: # checks with col 01 sum
                return False
            if grid[idx][idy+1] + grid[idx+1][idy+1] + grid[idx+2][idy+1] != sum: # checks with col 02 sum
                return False
            if grid[idx][idy+2] + grid[idx+1][idy+2] + grid[idx+2][idy+2] != sum: # checks with col 03 sum
                return False

            # --- checks rows ---
            if grid[idx+1][idy] + grid[idx+1][idy+1] + grid[idx+1][idy+2] != sum: # checks with diagonal 01 sum
                return False
            if grid[idx+2][idy] + grid[idx+2][idy+1] + grid[idx+2][idy+2] != sum: # checks with diagonal 01 sum
                return False

            numSet = set([grid[idx][idy], grid[idx][idy+1], grid[idx][idy+2], grid[idx+1][idy], grid[idx+1][idy+1], grid[idx+1][idy+2], grid[idx+2][idy], grid[idx+2][idy+1], grid[idx+2][idy+2]])
            
            if len(numSet) != 9 or max(numSet) != 9:
                return False

            return True

        for idx in range(rows-2):
            for idy in range(cols-2):
                if isMagicSq(idx, idy):
                    magicSqCount += 1
        return magicSqCount
