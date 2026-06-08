class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reversed_head = Solution().reverseList(head)

result = []
curr = reversed_head

while curr:
    result.append(curr.val)
    curr = curr.next

print(result)

# I used three pointers to reverse the linked list. I iterated through the list, keeping track of the previous, current, and next nodes. I updated the next pointer of the current node to point to the previous node, and then moved the pointers forward. Finally, I returned the new head of the reversed list.