import sys

n = int(sys.stdin.readline())

ans = [[' '] * 2 * n for _ in range(n)]


def parse_stars(i, j, size):
    if size == 3:
        ans[i][j] = '*'
        ans[i + 1][j - 1] = ans[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            ans[i + 2][j - k] = "*"
    else:
        temp = size // 2
        parse_stars(i, j, temp)
        parse_stars(i + temp, j - temp, temp)
        parse_stars(i + temp, j + temp, temp)


parse_stars(0, n-1, n)
for n in range(len(ans)):
    for m in range(len(ans[n])):
        print(ans[n][m], end="")
    print()

