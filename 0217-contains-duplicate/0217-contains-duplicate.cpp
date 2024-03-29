class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> freq;
        
        for (auto i : nums) {
            freq[i]++;
            if (freq[i] >= 2) {
                return true;
            }
        }
        return false;
    }
};