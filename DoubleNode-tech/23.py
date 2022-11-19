# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        print(head)
        while head:
            val, idx = heapq.heappop(head)

            p.next = ListNode(val)
            p = p.next
            print(lists[idx])
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next

# [(1, 0), (1, 1), (2, 2)]
# ListNode{val: 4, next: ListNode{val: 5, next: None}}
# ListNode{val: 3, next: ListNode{val: 4, next: None}}
# ListNode{val: 6, next: None}
# ListNode{val: 4, next: None}
# ListNode{val: 5, next: None}
# None
# None
# None
