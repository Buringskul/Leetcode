class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> q;
    int knums;

    KthLargest(int k, vector<int>& nums) {
        knums = k;
        for (int i : nums) {
            q.push(i);
        }

        while (q.size() > k) {
            q.pop();
        }
    }
    
    int add(int val) {
        q.push(val);

        while (q.size() > knums) {
            q.pop();
        }

        return q.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */