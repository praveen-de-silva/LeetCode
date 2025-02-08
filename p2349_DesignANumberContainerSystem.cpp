#include <iostream>
#include <map>
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