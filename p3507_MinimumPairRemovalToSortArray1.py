from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def non_decreasing(a: List[int]) -> bool:
            for i in range(1, len(a)):
                if a[i] < a[i - 1]:
                    return False
            return True

        ops = 0
        while not non_decreasing(nums):
            best_i = 0
            best_sum = nums[0] + nums[1]

            for i in range(1, len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < best_sum:   # tie automatically keeps leftmost
                    best_sum = s
                    best_i = i

            nums[best_i] = best_sum
            nums.pop(best_i + 1)
            ops += 1

        return ops
