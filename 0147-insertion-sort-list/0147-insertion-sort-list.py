class Solution:
    def insertionSortList(self, head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            i += 1
            curr = curr.next
        return head