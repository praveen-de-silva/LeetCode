// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int getPairs(int n) {
    int pairs = 0;
    for (int i=1; i<n; i++) {
        pairs += i;
    }
    return pairs;
}

int main() {
    // Write C++ code here
    vector<int> nums;
    map<int, int> data;
    int crntPairs;
    int countGoodSubArrs = 0;
    int k = 6;
    
    nums = {1,1,1,1,1};
    
    // cout << getPairs(5) << endl;
    
    for (int l=0; l<nums.size()-1; l++) {
        for (int r=l+1; r<nums.size(); r++) {
            data.clear();
            crntPairs = 0;
            
            for (int i=l; i<=r; i++) {
                data[nums[i]] += 1;
                
                if (data[nums[i]]>1) {
                    crntPairs += ((getPairs(data[nums[i]])) - (getPairs(data[nums[i]]-1)));
                    
                }
                
                if (crntPairs >= k) {
                    cout << crntPairs << ", l : " << l << ", r : " << r << endl;
                    countGoodSubArrs++;
                    break;
                }
                
            }
            
        }
    }
    
    cout << countGoodSubArrs << endl;
    
    return 0;
}