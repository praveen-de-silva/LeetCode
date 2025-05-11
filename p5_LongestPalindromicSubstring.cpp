// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    string getCrntLongestPal(string s, int crntMid) {
        int n = s.size();
        int low = crntMid-1, hi = crntMid+1;
        bool flag1 = true, flag2 = true;
        
        string tempStr1, tempStr2;
        tempStr1 += s[crntMid];
        
        if ((crntMid+1 < n) && s[crntMid]==s[crntMid+1]) {
            
            tempStr2 = s[crntMid];
            tempStr2 += s[crntMid+1];
        } else {
            flag2 = false;
        }
        
        
        while (low >= 0 && hi < n && (flag1 || flag2)) {
            if (flag1) {
                if (s[low] != s[hi]) {
                    flag1 = false;
                } else {
                    tempStr1 = s[low] + tempStr1 + s[hi];
                }
            }
            
            if (flag2) {
                if ((s[low] != s[hi+1]) || (hi+1>=n)) {
                    flag2 = false;
                } else {
                    tempStr2 = s[low] + tempStr2 + s[hi+1];
                }
            }
            
            if (!flag1 && !flag2) {
                break;
            }
            
            low--;
            hi++;
        }
        
        if (tempStr1.size() > tempStr2.size()) {
            return tempStr1;    
        } 
        return tempStr2;
    }

    string longestPalindrome(string s) {
        int crntMaxLength = 0;
        string longestPalStr, crntPalStr;

        for (int idx=0; idx<s.size(); idx++) {
            crntPalStr = getCrntLongestPal(s, idx);
            
            if (crntMaxLength < crntPalStr.size()) {
                longestPalStr = crntPalStr;
                crntMaxLength = crntPalStr.size();
            }
        }
        
        return longestPalStr;
    }
};