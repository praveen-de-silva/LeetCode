#include <map>
#include <iostream>

using namespace std;
// ====================================
// LeetCode problem 70: Climbing Stairs
// ====================================

class Solution {
    map<int, int> memory;
    
    public:
    int climbStairs(int n) {
        if (n<0) {
            cout << "error!" << endl;
            return -1;
        }
        
        int f_val;
        
        if (n<=3) {
            return n;
        }

        // memory check
        if (memory[n]!=0) {
            return memory[n]; 
        }
        
        f_val = climbStairs(n-1) + climbStairs(n-2);
        memory[n] = f_val;
        return f_val;
    }    
};
