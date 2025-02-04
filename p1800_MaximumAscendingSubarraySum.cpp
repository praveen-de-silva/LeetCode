#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int prev=0, crntSum=0, maxSum=0;

        for (int crnt : nums) {
            if (crnt > prev) {
                crntSum += crnt;

                if (crntSum > maxSum) {
                    maxSum = crntSum;
                }
            } else {
                crntSum = crnt;
            }
             
            prev = crnt;
        }

        return maxSum;
    }
};