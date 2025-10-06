class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -1e9
        crnt_sum = 0
        start, end = 0, 0

        for i in range(len(nums)):
            crnt_sum += nums[i]

            if crnt_sum > max_sum:
                max_sum = crnt_sum
                end = i
            
            if crnt_sum < 0:
                crnt_sum = 0

                if max_sum > 0:
                    start = i + 1
                else:
                    start = end

        print(start, end)

        return max_sum
            

        
