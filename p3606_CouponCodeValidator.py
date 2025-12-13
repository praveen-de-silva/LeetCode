class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        result = list()
        businesses = ["electronics", "grocery", "pharmacy", "restaurant"]
        validContainer = {k: list() for k in businesses}
       
        # -- checking validity -- 
        for c, b, a in zip(code, businessLine, isActive):
            if c.replace("_", "a").isalnum() and b in validContainer and a:
                validContainer[b].append(c)
        
        # -- adding to the result --
        for b in businesses:
            result.extend(sorted(validContainer[b]))

        return result
