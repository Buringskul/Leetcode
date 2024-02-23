class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> startCity;
        unordered_set<string> endCity;
        
        for (int i = 0; i < paths.size(); i++) {
             startCity.insert(paths[i][0]);
             endCity.insert(paths[i][1]);
        }
        
        for (auto i : endCity) {
            if (startCity.find(i) == startCity.end()) {
                return i;
            }
        }
        
        return "";
    }
};