class Solution:
    def func(self, n: int) -> int:
        res = 0
        for i in range(n+1):
            res += i
        return res

    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        pCount = 0
        p, q = 0, 0 # 2 pointers 

        for i in range(n):
            if i+1 < n and (prices[i] == prices[i+1]+1) :
                q += 1
            else:
                pCount += self.func(q-p+1)
                if i+1 == n:
                    break
                q += 1
                p = q
        
        return pCount
