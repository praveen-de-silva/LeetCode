from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for p in nums:
            if p % 2 == 0:      # only happens for p=2 since p is prime
                ans.append(-1)
                continue

            # count trailing 1s in p
            k = 0
            t = p
            while t & 1:
                k += 1
                t >>= 1

            ans.append(p - (1 << (k - 1)))
        return ans
