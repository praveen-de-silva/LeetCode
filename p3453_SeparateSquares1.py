from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # total area
        total = 0.0
        lo = float('inf')
        hi = 0.0

        for x, y, l in squares:
            total += l * l
            lo = min(lo, y)
            hi = max(hi, y + l)

        half = total / 2.0

        def area_below(Y: float) -> float:
            s = 0.0
            for x, y, l in squares:
                h = Y - y
                # case 01 : 'line' is below the square
                if h <= 0:
                    continue
                # case 02 : 'line' is above the square
                if h >= l:
                    s += l * l
                # case 03 : 'line' is within the square
                else:
                    s += l * h
            return s

        # binary search for smallest Y with area_below(Y) >= half
        for _ in range(60):  # enough precision
            mid = (lo + hi) / 2.0
            # case 01 : 'line' must be within 'lo' and 'mid'
            if area_below(mid) >= half: # this '=' makes the most minimum line
                hi = mid
            # case 02 : 'line' must be within 'mid' and 'hi'
            else:
                lo = mid

        return hi
