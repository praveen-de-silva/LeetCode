class Solution(object):
    def twoSum(self, nums, target):
        '''find indexes of the two numbers'''
        seen = {} # enter seen data
        for p in range(len(nums)):
            reqNum = target - nums[p]

            if reqNum in seen:
                return [seen[reqNum], p]
            else:
                seen[nums[p]] = p