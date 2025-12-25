class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mem = {}

        def getMaxAmount(idx):
            if idx > n-1:
                return 0

            # --- looks in the memory ---
            if idx in mem:
                return mem[idx]
            
            # --- if not in memory ---
            # handle end issue
            if idx > n-2:
                next = 0
            else:
                next = nums[idx+1]
            
            result = max(nums[idx] + getMaxAmount(idx + 2),  next + getMaxAmount(idx + 3))
            mem[idx] = result # add to the memory
            return result

        return getMaxAmount(0)
