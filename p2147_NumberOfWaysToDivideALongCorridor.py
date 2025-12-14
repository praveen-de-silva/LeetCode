class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        
        if "S" not in corridor:
            return 0
        
        n = len(corridor)
        mod = 1e9 + 7
        result = 1
        tempCount_S, tempCount_P = 0, 0

        for i in range(n):
            if corridor[i] == "S":
                tempCount_S += 1

                if tempCount_S == 2:
                    tempCount_P = 0

                if tempCount_S > 2:
                    result = (result * (tempCount_P + 1)) % mod
                    tempCount_S = 1
                    tempCount_P = 0
            else:
                tempCount_P += 1
        
        if tempCount_S != 2:
            return 0
        return int(result)

            

            


        
