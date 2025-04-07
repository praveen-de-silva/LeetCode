#include <iostream>
#include <vector>
using namespace std;

int findXORSum(vector<int> &arr, int i, int total) {
    // base condition
    if (i==arr.size()) {
        return total;
    }
    
    // recurcivly add XORed and non XORed numbers
    return findXORSum(arr, i+1, (total ^ arr[i])) + findXORSum(arr, i+1, total);
}