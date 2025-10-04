class Solution(object):
    def search_first(self, nums, l, r):
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return l  # index of smallest element

    def search_binary(self, nums, l, r, t):
            if l > r:
                return -1
            
            mid = (l + r) // 2

            if nums[mid] == t:
                return mid
            if nums[mid] > t:
                return self.search_binary(nums, l, mid-1, t)
            return self.search_binary(nums, mid+1, r, t)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = self.search_first(nums, 0, len(nums)-1)
        print(first)

        if nums[0] <= target <= nums[first-1] and first != 0:
            return self.search_binary(nums, 0, first-1, target)
        return self.search_binary(nums, first, len(nums)-1, target)
        
        
