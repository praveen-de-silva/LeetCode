class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int nEq=0, eq=nums.size()-1;

        while (true) {
            while (nums[nEq]!=val && nEq<(nums.size()-1)) {
                nEq++;
            }

            while (nums[eq]==val && eq>0) {
                eq--;
            }

            if (nEq>=eq) {
                nums.pop_back();
                nums.pop_back();
                return (nEq+1);
            }

            int temp = nums[nEq];
            nums[nEq] = nums[eq];
            nums[eq] = temp;
        }
    }
};