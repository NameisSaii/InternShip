class Solution(object):
    def hasCycle(self, head):
        marker1 = head
        marker2 = head
        while marker2!=None and marker2.next!=None:
            marker1 = marker1.next
            marker2 = marker2.next.next
            if marker2==marker1:
                return True
        return False