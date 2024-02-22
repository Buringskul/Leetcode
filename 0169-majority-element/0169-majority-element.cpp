class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> freq;
        int answer;

        for (auto i : nums) {
            freq[i]++;
        }

        for (auto i : freq) {
            if (i.second > (nums.size() / 2)) {
                answer = i.first;
                break;
            }
        }

        return answer;
    }
};