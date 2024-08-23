import sys
import math

h, w, n, m = list(map(int, sys.stdin.readline().split()))

print(math.ceil(h / (n+1)) * math.ceil(w / (m+1)))