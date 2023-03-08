# 숫자 놀이

n = int(input())
arr = list(map(int, input().split()))


def recursive_aligning(start, end):
    s = {}
    # n at level
    foo = int((end - start + 2) / 2)
    middle = int(foo / 2)

    if foo <= 1:
        # end of depth
        return arr[start]

    for i in range(3):
        # go in depth
        s[i] = recursive_aligning(start + (i * middle), start + (i * middle) + (2 * middle - 2))

    if s[0] % 2 == s[1] % 2:
        # desired outcome
        return int(s[0] + s[1]) / 2

    elif s[0] % 2 == s[2] % 2:
        for i in range(middle):
            # e//e | o//o -> swap at middle end to make ee// | oo//
            arr[start + middle + i], arr[start + foo + i] = arr[start + foo + i], arr[start + middle + i]
        return int(s[0] + s[2]) / 2

    else:
        for i in range(middle):
            # //oo | //ee -> swap at surface to make oo// | ee//
            arr[start + i], arr[start + foo + i] = arr[start + foo + i], arr[start + i]
        return int(s[1] + s[2]) / 2


recursive_aligning(0, 2 * n - 2)
for vals in range(n):
    print(arr[vals], end=' ')
