class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)
        print(x)
        
        if str_x[0] == str_x[-1]:
            if len(str_x) <= 2:
                return True
            return self.isPalindrome(str_x[1:-1])
        return False