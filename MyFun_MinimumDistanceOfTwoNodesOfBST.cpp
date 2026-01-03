// Online C++ compiler to run C++ program online
#include <iostream>

using namespace std;

int findDist(int u, int v) {
    int crnt_u = u, crnt_v = v;
    int dist_u = 0, dist_v = 0;
    
    while (true) {
        while (crnt_u > crnt_v) {
            crnt_u = (crnt_u-1) / 2;
            dist_u++;
        }
        
        while (crnt_v > crnt_u) {
            crnt_v = (crnt_v-1) / 2;
            dist_v++;
        }
        
        if (crnt_u == crnt_v) {
            break;
        }
    }
    
    return dist_u + dist_v;
}

int main() {
    // for test
    cout << findDist(18, 2);

    return 0;
}
