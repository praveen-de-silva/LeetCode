#include <map>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findDigSum(int num) {
        string num_str = to_string(num);
        int digSum = 0;

        for (char dig : num_str) {
            digSum += dig - '0';
        }

        return digSum;
    }

    int findSetMaxSum(vector<int> &vec) {
        int sum = 0, count=0;
        sort(vec.begin(), vec.end());
        auto it = vec.rbegin();
        
        while (it != vec.rend() && count<2) {
            sum += *it;
            
            count++;
            ++it; 
        }
        
        if (count==2) {
            return sum;
        } else {
            return -1;
        }
    }

    int maximumSum(vector<int>& nums) {
        int crntDigSum;
        map<int, vector<int>> allData;

        for (int num : nums) {
            crntDigSum = findDigSum(num);
            allData[crntDigSum].push_back(num);
        }

        //-------- Analysing ---------
        int maxKey, maxSum=-1, tempMaxSum;

        for (auto data : allData) {
            tempMaxSum =  findSetMaxSum(data.second);

            if (tempMaxSum > maxSum) {
                maxSum = tempMaxSum;
            }

        }
        
        return maxSum;
    }
};