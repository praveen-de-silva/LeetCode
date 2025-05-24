#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    long long  ceilDiv(long long  neu, int den) {
        /*
         * return the ceil division
         */
        return (neu + den - 1) / den;
    }

    // void printArr(vector<int>& nums) {
    //     for (int num : nums) {
    //         cout << num << " ";
    //     }
    //     cout << endl;
    // }

    int searchIdx(vector<int>& nums, int start, int last, long long target) {
        /*
         * search the minimum multiplier 
         */
        int idx_mid = (start + last) / 2;
        // cout << start << " " << last << endl;
        
        // return the minimum next int (if not found the target)
        if (last < start) {
            return start;
        }
        
        // if found
        if (nums[idx_mid] == target) {
            if (idx_mid == 0) {
                return idx_mid;                
            }
            if (nums[idx_mid-1] != target) {
                return idx_mid;
            }
        }
        
        if (nums[idx_mid] >= target) {
            return searchIdx(nums, start, idx_mid-1, target);
        }
        
        return searchIdx(nums, idx_mid+1, last, target);
    }

public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        vector<int> result;
        int size = potions.size();
        long long crntMinMul;
        
        sort(potions.begin(), potions.end());
        // cout << "array : "<< endl;
        // printArr(potions);

        for (int spell : spells) {
            crntMinMul = ceilDiv(success, spell);
            // cout << "crntMinMul : " << crntMinMul << endl;
            // cout << "index : " << searchIdx(potions, 0, size-1, crntMinMul) << endl;
            result.push_back(size - searchIdx(potions, 0, size-1, crntMinMul));
        }

        return result;
    }
};