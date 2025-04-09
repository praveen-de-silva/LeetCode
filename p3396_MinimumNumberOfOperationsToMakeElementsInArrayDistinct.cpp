#include <iostream>
#include <vector>
#include <map>
using namespace std;


// =============
//   MY METHOD
// =============

class Solution {
    public:
    int minimumOperations(vector<int>& nums) {
        int n = nums.size(); // size of the array
        map<int, int> data;  // to detect duplicates
        int crntStart = 0;   // current stating index
        int p = 0;           // pointer
        int oprs = 0;        // operations

        // visiting all numbers
        while (p < n && crntStart < n) {
            cout << p << " (" << nums[p]<< ") " << oprs << endl;
            if (data[nums[p]] == nums[p]) { // number is already seen
                crntStart += 3; // change current start
                p = crntStart;  // change pointer
                oprs++;

                data.clear();   // clear duplicate find data
            } 
            
            else {
                data[nums[p]] = nums[p];
                p++;
            }  
            
        }
        return oprs;
    }
};