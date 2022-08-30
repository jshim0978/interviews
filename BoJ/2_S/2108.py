import statistics
import sys

N = int(sys.stdin.readline())

num_list = []
sum = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)
    sum += num


num_list.sort()
mul_mod = statistics.multimode(num_list)
print(round(sum / N))
print(num_list[int(N/2)])
if len(mul_mod) > 1:
    print(mul_mod[1])
else:
    print(mul_mod[0])
print(num_list[N-1] - num_list[0])

