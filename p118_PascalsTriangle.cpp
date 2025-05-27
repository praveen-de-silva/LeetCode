#include <map>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
    map<int, vector<vector<int>>> memory;
public:
    vector<vector<int>> generate(int numRows) {
        if (numRows==1) {
            return {{1}};
        }

        if (memory.find(numRows) != memory.end()) {
            return memory[numRows];
        }

        vector<vector<int>> prev = generate(numRows-1);
        vector<int> crntArr = {1};

        for (int i=0; i<numRows-2; i++) {
            crntArr.push_back(prev[numRows-2][i] + prev[numRows-2][i+1]);
        }
        crntArr.push_back(1);
        prev.push_back(crntArr);
        memory[numRows] = prev;

        return prev;
    }
};