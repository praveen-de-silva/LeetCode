class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        uniqueNums = []

        i=0

        while True:
            if i==len(nums):
                return

            crnt = nums[i]
            
            if crnt in uniqueNums:
                nums.remove(crnt)
                continue
            uniqueNums.append(crnt)
            i+=1