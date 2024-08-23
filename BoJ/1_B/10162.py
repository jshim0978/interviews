
n = int(input())

a_count = 0
b_count = 0
c_count = 0

while n >= 10:
    if n >= 300:
        n -= 300
        a_count += 1

    elif n >= 60:
        n -= 60
        b_count += 1

    else:
        n -= 10
        c_count += 1

if n == 0:
    print(f"{a_count} {b_count} {c_count}")
else:
    print('-1')