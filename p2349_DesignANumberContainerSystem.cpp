#include <iostream>
#include <map>
#include <set>
using namespace std;

class NumberContainers {
    map<int, int> data;

    public:
        NumberContainers() {}

        bool isAvailable(int target) {
            for (auto pair : data) {
                if (pair.first==target) {
                    return true;
                }
            }
            return false;
        }
        
        void change(int index, int number) {
            data[index] = number;
        }
        
        int find(int number) {
            for (auto pair : data) {
                if (pair.second==number) {
                    return pair.first;
                }
            }
            return -1;
        }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */


 /*
    ---------------
    Algo 02 (Super)
    ---------------
 */

 class NumberContainers {
    map<int, int> data;
    map<int, set<int>> data2;

    public:
        NumberContainers() {}
        
        void change(int index, int number) {
            if (data.find(index)!=data.end() && data[index]!=number) {
                data2[data[index]].erase(index);

                if (data2[data[index]].empty()) {
                    data2.erase(data[index]);
                }
            }
            data[index] = number;
            data2[number].insert(index);
        }
        
        int find(int number) {
            return data2[number].empty() ? -1 : *data2[number].begin();
        }
};