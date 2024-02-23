class Solution {
public:
    char repeatedCharacter(string s) {
        unordered_map<char, int> freq;
        char answer;
        
        for (auto i : s) {
            freq[i]++;
            if (freq[i] == 2) {
                return i;
            }
        }
        return answer;
    }
};