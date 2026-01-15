from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def best(bars: List[int]) -> int:
            bars.sort()
            longest = 1
            cur = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    cur += 1
                    longest = max(longest, cur)
                else:
                    cur = 1
            return longest + 1  # k consecutive removals => k+1 cells

        H = best(hBars)
        V = best(vBars)
        side = min(H, V)
        return side * side
