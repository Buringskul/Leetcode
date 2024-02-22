class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = nums.size() - 1; i > 0; i--) { 
            if (nums[i - 1] == nums[i]) {
                return true;
            }
        }
        return false;
    }
};