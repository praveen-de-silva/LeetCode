
#class Solution(object):
    # Method 01
    # def isPalindrome(self, x):
    #     str_x = str(x)
    #     print(x)
        
    #     if str_x[0] == str_x[-1]:
    #         if len(str_x) <= 2:
    #             return True
    #         return self.isPalindrome(str_x[1:-1])
    #     return False

    # Method 02
    # def isPalindrome(self, x):
    #     str_x = str(x)

    #     if str_x == str_x[::-1]:
    #         return True
    #     return False

    # Method 03
    # def isPalindrome(self, x):
    #     div = 1
    #     while x>10*div:
    #         div *= 10

    #     while x:
    #         if x//div == x%10:
    #             x = (x % div) // 10
    #             div //=100
    #         else:
    #             return False
    #     return True

print(isPalindrome(1000021))           
