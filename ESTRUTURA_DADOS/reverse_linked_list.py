class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_list = None

        while head:
            next_node = head.next
            head.next = new_list
            new_list = head
            head = next_node

        return new_list
    
    

ss = Solution()        

print(ss.reverseList(head=[1,2,3,4,5]))