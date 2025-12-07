class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mods = dict()
        n = len(nums)
        crntSum = 0

        # update the mods hash map
        for i in range(n):
            crntSum += nums[i]
            mod = crntSum%k

            if mods.get(mod) == None:
                mods[mod] = {i}
            else:
                mods[mod].add(i)

        print(mods)

        for r, idxs in mods.items():
            crntIdxs = list(idxs)
            m = len(crntIdxs)

            if r==0 and crntIdxs[-1] >= 1:
                return True

            if m < 2:
                continue

            if abs(crntIdxs[0] - crntIdxs[-1]) > 1:
                return True
        return False


        
