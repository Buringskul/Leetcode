class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int maxLength = 0;

        for (auto num : s) {
            if (s.find(num - 1) == s.end()) {
                int currentNum = num;
                int currentLength = 1;
                
                while (s.find(currentNum + 1) != s.end()) {
                    currentNum++;
                    currentLength++;
                }
                
                maxLength = max(maxLength, currentLength);
            }
        }
        return maxLength;
    }
};