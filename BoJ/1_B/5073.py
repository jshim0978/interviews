import sys

while True:
    a, b, c = list(map(int, sys.stdin.readline().split()))

    triangle = [a, b, c]

    triangle.sort()
    if triangle[2] == triangle[1] == triangle[0] == 0:
        break
    elif triangle[2] >= triangle[1] + triangle[0]:
        print("Invalid")
    elif triangle[2] == triangle[1] == triangle[0]:
        print("Equilateral")
    elif triangle[2] == triangle[1] or triangle[1] == triangle[0]:
        print("Isosceles")
    else:
        print("Scalene")
