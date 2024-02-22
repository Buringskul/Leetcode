class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> freq;
        bool answer = false;

        for (auto i : nums) {
            freq[i]++;
        }

        for (auto i : freq) {
            if (i.second >= 2) {
                answer = true;
                break;
            }
        }

        return answer;
    }
};