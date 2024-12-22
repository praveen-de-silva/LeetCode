class Solution(object):
    data = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }

    def romanToInt(self, s):
        if len(s)==1:
            return self.data[s]

        if self.romanToInt(s[0])>= self.romanToInt(s[1]):
            return self.romanToInt(s[0]) + self.romanToInt(s[1:])
        return - self.romanToInt(s[0]) + self.romanToInt(s[1:])