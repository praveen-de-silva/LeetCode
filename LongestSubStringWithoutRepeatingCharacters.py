class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        ltrCount = 0
        counts = {0}
        strSize = len(s)

        for i in range(strSize):
            j = i
            ltrs = set()
            
            while j<strSize:
                if s[j] in ltrs:
                    break

                ltrs.add(s[j])
                j += 1
            
            counts.add(j-i)
        
        return max(counts)