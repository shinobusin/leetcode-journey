class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next

        first = -1
        last = -1

        min_dist = float('inf')
        position = 1

        while curr.next:
            next_node = curr.next

            # Check if curr is a critical point
            if (prev.val < curr.val > next_node.val) or \
               (prev.val > curr.val < next_node.val):

                if first == -1:
                    first = position
                else:
                    min_dist = min(min_dist, position - last)

                last = position

            prev = curr
            curr = next_node
            position += 1

        if first == -1 or first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]
        