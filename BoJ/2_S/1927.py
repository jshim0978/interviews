import sys
import collections
from queue import PriorityQueue

N = int(sys.stdin.readline())

queue = PriorityQueue()

# function where if x > 0 append to the right if x == 0 print lowest number and pop it
def append_to_right(x):
    if x > 0:
        queue.put(x)
    else:
        if queue.qsize() > 0:
            print(queue.get())
        else:
            print(0)


for _ in range(N):
    x = int(sys.stdin.readline())
    append_to_right(x)