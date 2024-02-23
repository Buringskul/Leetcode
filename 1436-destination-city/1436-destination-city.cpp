class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> startCity;
        unordered_set<string> endCity;
        
        for (auto i : paths) {
             startCity.insert(i[0]);
             endCity.insert(i[1]);
        }
        
        for (auto i : endCity) {
            if (startCity.find(i) == startCity.end()) {
                return i;
            }
        }
        
        return "";
    }
};