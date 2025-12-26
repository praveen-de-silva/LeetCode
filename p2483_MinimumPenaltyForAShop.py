class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        crntPen = customers.count("N")
        minPen = crntPen
        result = n
        
        for i in range(n-1, -1, -1):
            if customers[i] == "Y":
                crntPen += 1
            else:
                crntPen -= 1

            if crntPen <= minPen:
                result = i
                minPen = crntPen

        return result
