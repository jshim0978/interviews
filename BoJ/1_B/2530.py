a, b, c = map(int, input().split())
d = int(input())

new_a = ((((c + d) // 60 + b) // 60) + a) % 24
new_b = ((c + d) // 60 + b) % 60
new_c = (c + d) % 60

print(new_a, new_b, new_c)
