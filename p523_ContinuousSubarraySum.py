class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mods = {0:{0}}
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
            if len(idxs)<2:
                continue

            crntIdxs = list(idxs)
            m = len(crntIdxs)
            
            for j in range(m-1):
                if abs(crntIdxs[j+1] - crntIdxs[j]) >= 1:
                    return True
        return False


        
