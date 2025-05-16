#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

class Solution {
public:
    bool hasRotten(vector<vector<int>>& grid, int i_x, int i_y) {
        int m = grid.size();
        int n = grid[0].size();
        
        return ((i_x-1>=0) && (grid[i_x-1][i_y]==2)) || ((i_y-1>=0) && (grid[i_x][i_y-1]==2)) || ((i_x+1<m) && (grid[i_x+1][i_y]==2)) || ((i_y+1<n) && (grid[i_x][i_y+1]==2));
    }

    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int time = 0;
        bool changed, isFullyRotten = true;
        
        do {
            vector<tuple<int, int>> tempVect;
            changed = false;
            
            for (int i=0; i<m; i++) {
                for (int j=0; j<n; j++) {
                    if (grid[i][j] == 1) {
                        isFullyRotten = false;
                        
                        if (hasRotten(grid, i, j)) {
                            tempVect.push_back(make_tuple(i, j));
                            
                            changed = true;
                        }
                    }
                }
            }
            
            for (tuple<int, int> t : tempVect) {
                grid[get<0>(t)][get<1>(t)] = 2;
            }
            
            
            time++;
        } while(changed);
        
        for (int i=0; i<m; i++) {
                for (int j=0; j<n; j++) {
                if (grid[i][j] == 1) {
                    return -1;
                }
                    
            }
        }
        
        return time-1;
    }
};