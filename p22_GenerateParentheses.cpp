#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    bool isPar(string par_str, int n) {
        int L=0, R=0;
        int i=0;
        
        do {
            // cout << par_str[i] << " ";
            if (par_str[i] == '0') {
                L++;
            } else {
                R++;
            }
            
            i++;
        } while (L>=R && i<par_str.size());
        
        return (par_str.size()==2*n && L==R) || (par_str.size()<2*n && L>=R);
    }

    vector<string> convertToPar(vector<string> arr) {
        vector<string> result;
        
        for (string crnt : arr) {
            string temp_str = "";
            
            for (int i=0; i<crnt.size(); i++) {
                temp_str += char(crnt[i] - '0' + '(');
            }
            
            result.push_back(temp_str);
        }
        
        return result;
    }

public:
    vector<string> generateParenthesis(int n) {
        vector<string> result = {"0"};
        vector<string> temp;
        
        for (int i=0; i<2*n-1; i++) {
            for (int j=0; j<2; j++) {
                for (string par_str : result) {
                    // cout  << par_str + char(j + '0') << endl;
                    if (isPar(par_str + char(j + '0'), n)) {
                        // cout  << "ok" << endl;
                        temp.push_back(par_str + char(j + '0'));
                    }
                }
                
                
            }
            result = temp;
            temp.clear();
        }
        sort(result.begin(), result.end());
        return convertToPar(result);        
    }
};

// =================
//     Method 02
// =================

class Solution {
    vector<string> Par;
    queue<string> Q;
    
    public:
    Solution() {
        Q.push("(");
    }
    
    int cmdPar(string par_str, int n) {
        int L=0, R=0;
        int i=0;
        
        do {
            // cout << par_str[i] << " ";
            if (par_str[i] == '(') {
                L++;
            } else {
                R++;
            }
            
            i++;
        } while (L>=R && i<par_str.size());
        
        // cout << "L : " << L << " R : " << n  << "| ";
        
        if (L < R || L > n) return 0;
        if (L == R && L == n) return 1;
        return 2; // if (L >= R) 
    }
    
    
    void setPar(int n) {
        while (!Q.empty()) {
            string temp = Q.front();
            Q.pop();
            // cout << cmdPar(temp, n) << " : "  << temp << "\n";
            switch (cmdPar(temp, n)) {
                case 0:
                    continue;
                    break;
                    
                case 1:
                    // cout << "HI\n";
                    Par.push_back(temp);
                    break;
                    
                case 2:
                    Q.push(temp + "(");
                    Q.push(temp + ")");
                    break;
            }
        }
    }

    vector<string> generateParenthesis(int n) {
        setPar(n);
        return this->Par;      
    }
};