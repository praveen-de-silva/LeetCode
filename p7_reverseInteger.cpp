#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int sign;

        if (x>=0) sign = 1;
        else sign = -1;

        long int crntInt = abs((long int) x);
        long int crntNum = 0;

        while (crntInt>0) {
            crntNum = (crntInt%10) + (crntNum * 10);
            crntInt /= 10;
        }
    
        if (sign == 1 && crntNum < pow(2, 31)) {
            return crntNum;
        } else if (sign == -1 && crntNum <= pow(2, 31)) {
            return sign * crntNum;
        }
        return 0;
    }
};