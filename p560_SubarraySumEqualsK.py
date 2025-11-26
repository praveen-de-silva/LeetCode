class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        crntSum = 0
        prefSums = {0:1}
        count = 0

        for num in nums:
            crntSum += num
            diff = crntSum - k
            count += prefSums.get(diff, 0)
            prefSums[crntSum] = prefSums.get(crntSum, 0) + 1

        return count
        
