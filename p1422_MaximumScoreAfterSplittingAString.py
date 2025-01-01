class Solution(object):
    # Method 01
    def getScore(self, left_s, right_s):
        return left_s.count('0') + right_s.count('1')

    def maxScore(self, s):
        maximum = 0

        for i in range(1, len(s)):
            if self.getScore(s[:i], s[i:]) > maximum:
                maximum = self.getScore(s[:i], s[i:])

        return maximum

    # Method 02
    def maxScore(self, s):
        temp = s[:1].count('0') + s[1:].count('1')
        maximum = temp

        for ch in s[1:-1]:
            if ch == '0':
                temp += 1
            elif ch == '1':
                temp -= 1

            if temp > maximum:
                maximum = temp

        return maximum
