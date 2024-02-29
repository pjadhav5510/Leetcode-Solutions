# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.c=0
        def leng(root):
            while root:
                self.c+=1
                root = root.next
        leng(head)

        self.c = (self.c//2)

        result = ListNode(next=head)
        #result.next = head
        cur = result
        i=0
        x= self.c
        print('x: ',x)
        while cur:    
            if i == x:
                cur.next = cur.next.next
            i+=1
            cur = cur.next
        return result.next