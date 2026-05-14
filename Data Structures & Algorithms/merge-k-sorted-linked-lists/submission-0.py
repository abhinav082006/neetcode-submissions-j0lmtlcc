class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        # collect values
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next

        # sort values
        arr.sort()

        # build linked list
        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next