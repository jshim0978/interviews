import sys

N = int(sys.stdin.readline())
broken_buttons_length = int(sys.stdin.readline())
broken_buttons = list(map(int, sys.stdin.readline().split()))

min_clicks = 0
if N > 100:
    min_clicks = N - 100
else:
    min_clicks = 100 - N

for _ in range(999999):
    _ = str(_)

    for j in range(len(_)):
        if int(_[j]) in broken_buttons:
            break

        elif j == len(_) - 1:
            min_clicks = min(min_clicks, abs(int(_) - N) + len(_))

print(min_clicks)
