class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        result = list()
        validContainer = {
            "electronics" :  list(),
            "grocery" :  list(),
            "pharmacy" : list(),
            "restaurant" :  list()
        }
       
        for i in range(len(code)):
            if code[i].replace("_", "a").isalnum() and businessLine[i] in validContainer and isActive[i]:
                validContainer[businessLine[i]].append(code[i])

        return sorted(validContainer["electronics"]) + sorted(validContainer["grocery"]) + sorted(validContainer["pharmacy"]) + sorted(validContainer["restaurant"])
        
