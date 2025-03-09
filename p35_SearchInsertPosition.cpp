#include <vector>
using namespace std;

class Solution {
    public:
        int binarySearch(vector<int> &nums, int left, int right, int target) {
            if (left <= right) {
                int midPos = (left + right) / 2; // index of the 'middle'
    
                // found
                if (target == nums[midPos]) {
                    return midPos;
                }
    
                // search in the left part
                if (target < nums[midPos]) {
                    return binarySearch(nums, left, midPos - 1, target);
                }
    
                // search in the right part
                if (target > nums[midPos]) {
                    return binarySearch(nums, midPos + 1, right, target);
                }
            }
            return left; // not found, but the position if exists
        }
    
        int searchInsert(vector<int>& nums, int target) {
            return binarySearch(nums, 0, nums.size() - 1, target);
        }
    };