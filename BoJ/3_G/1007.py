#  벡터 매칭

import itertools

T = int(input())
for _ in range(T):
    N = int(input())
    points = [list(map(int, input().split())) for i in range(N)]

    x_sum, y_sum = 0, 0

    for x, y in points:
        x_sum += x
        y_sum += y

    ramp = 9999999999999999999

    for selected_points in itertools.combinations(points, N // 2):
        selected_point_x, selected_point_y = 0, 0
        for x, y in selected_points:
            selected_point_x += x
            selected_point_y += y

        matching_point_x = x_sum - selected_point_x
        matching_point_y = y_sum - selected_point_y

        x = matching_point_x - selected_point_x
        y = matching_point_y - selected_point_y
        ramp = min(ramp, (x ** 2 + y ** 2) ** 0.5)
    print(ramp)
