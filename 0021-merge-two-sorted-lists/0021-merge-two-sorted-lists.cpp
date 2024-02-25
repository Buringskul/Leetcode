/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == NULL) {
            return list2;
        }

        if (list2 == NULL) {
            return list1;
        }

        //make a new linked list
        ListNode* head = list1;

        // initalize new_list node with smallest element
        if (list1->val > list2->val) {
            head = list2;
            list2 = list2->next;
        }

        else {
            list1 = list1->next;
        }
    
        ListNode *curr = head;

        //add element into new_list node until any of the list reached NULL
        while (list1 && list2) {

            if (list1->val < list2->val) {
                curr->next = list1;
                list1 = list1->next;
            }

            else {
                curr->next = list2;
                list2 = list2->next;
            }
            
            curr = curr->next;
        }

        // If any numbers are left in one list
        if (list1) {
            curr->next = list1;
            list1 = list1->next;
        }

        else if (list2) {
            curr->next = list2;
            list2 = list2->next;
        }

        return head;
    }
};