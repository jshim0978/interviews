import sys

t = int(input())


for _ in range(t):

    n = int(input())

    drink_dict = {}

    for _ in range(n):
        name, drinks = sys.stdin.readline().split()
        drink_dict[name] = int(drinks)

    print(f"{max(drink_dict, key=drink_dict.get)}")





