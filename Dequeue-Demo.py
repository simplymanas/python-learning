
# 4th jul 2020
# Manas Dash
# In built collection module demo
#
# deque([iterable])
#   Returns a new deque object initialized left-to-right (using append()) with data from iterable.
#   If iterable is not specified, the new deque is empty.
#   Deques are a generalization of stacks and queues
#   (the name is pronounced ``deck'' and is short for ``double-ended queue'').
#   Deques support thread-safe, memory efficient appends and pops
#   from either side of the deque with approximately the same O(1) performance in either direction.
# source: https://docs.python.org/2.5/lib/deque-objects.html

import collections

Q = collections.deque()

Q.append(1)
print (Q)

Q.appendleft(2)
print (Q)

Q.extend([3, 4])
print (Q)

Q.extendleft([5, 6])
print (Q)

Q.pop()
print (Q)

Q.popleft()
print (Q)

Q.rotate(3)
print (Q)

Q.rotate(-3)
print (Q)

Q.remove(2)
print (Q)

# Output
# deque([1])
# deque([2, 1])
# deque([2, 1, 3, 4])
# deque([6, 5, 2, 1, 3, 4])
# deque([6, 5, 2, 1, 3])
# deque([5, 2, 1, 3])
# deque([2, 1, 3, 5])
# deque([5, 2, 1, 3])
# deque([5, 1, 3])

# Next task should be to look at the implementation and strengthen your DSA
