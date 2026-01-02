class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2  
        counts = dict()

        # --- setting up the counts ---
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # --- find the element ---
        for num, count in counts.items():
            if count == n:
                return num
        return -1 # Error!


        
