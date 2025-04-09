#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        map<int, int> data;
        int count = 0;

        for (int num : nums) {
            if (data[num] != num) {
                // cannot make futher
                if (num < k) {
                    return -1;
                }

                // to be counted
                if (num > k) {
                    count++;
                    data[num] = num;
                }
            }
        }
        return count;
    }
};