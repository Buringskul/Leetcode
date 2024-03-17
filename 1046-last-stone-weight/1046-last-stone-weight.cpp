class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> q;

        for (int i = 0; i < stones.size(); i++) {
            q.push(stones[i]);
        }

        while (q.size() > 1) {
            int first = q.top();
            q.pop();
            int second = q.top();
            q.pop();

            if (first != second) {
                int sum = first - second;
                q.push(abs(sum));
            }
        }
        
        if (q.size() == 0) {
            return 0;
        }
        
        return q.top();
    }
};