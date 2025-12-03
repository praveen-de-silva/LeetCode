class Solution(object):
    # Method 01:
    # data = {
    #     'I':1,
    #     'V':5,
    #     'X':10,
    #     'L':50,
    #     'C':100,
    #     'D':500,
    #     'M':1000
    #     }

    def romanToInt(self, s):
        if len(s)==1:
            return self.data[s]

        if self.romanToInt(s[0])>= self.romanToInt(s[1]):
            return self.romanToInt(s[0]) + self.romanToInt(s[1:])
        return - self.romanToInt(s[0]) + self.romanToInt(s[1:])

    # Method 02:

    def romanToInt(self, s):
        data = { # Hash map to store data
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and data[s[i]]<data[s[i+1]]:
                res += data[s[i]]
            else:
                res -= data[s[i]]
        
        return res
