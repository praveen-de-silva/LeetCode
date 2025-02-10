#include <iostream>
#include <string>
#include <cctype>

using namespace std;

class Solution {
public:
    string clearDigits(string s) {
        int i = 0;

        while (i < s.size()) {
            if (i > 0 && isdigit(s[i])) {
                i--;
                s.erase(i,2);
                continue;
            }
            i++;
        }
        return s;
    }
};