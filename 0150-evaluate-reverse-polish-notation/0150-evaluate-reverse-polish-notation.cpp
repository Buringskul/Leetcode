class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> nums;

        for (auto i : tokens) {
            if (i == "+" || i == "-" || i == "/" || i == "*") {
                int n1 = nums.top();
                nums.pop();
                int n2 = nums.top();
                nums.pop();
                
                if (i == "+") {
                    nums.push(n2 + n1);
                }

                if (i == "-") {
                    nums.push(n2 - n1);
                }

                if (i == "/") {
                    nums.push(n2 / n1);
                }

                if (i == "*") {
                    nums.push(n2 * n1);
                }
            }

            else {
                nums.push(stoi(i));
            }
        }
        return nums.top();
    }
};