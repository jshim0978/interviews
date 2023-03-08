MAX_VALUE = 50000
MAX_ITERATION = 100

N = int(input())

mobius = [1 for i in range(MAX_VALUE)]
prime = [True for i in range(MAX_VALUE)]

# mobius matrix
for i in range(2, MAX_VALUE):
    if prime[i]:
        mobius[i] = -1
        prime_square = i ** 2
        for j in range(i * 2, MAX_VALUE, i):
            if j % prime_square == 0:
                mobius[j] = 0
            prime[j] = False
            mobius[j] = -mobius[j]

low = N
high = MAX_VALUE ** 2

# checking for already added values
# iterations is set at 100 ; may not be 
for iterations in range(MAX_ITERATION):
    mid = (low + high) // 2
    count = mid
    for j in range(2, int(mid ** 0.5 + 1) // 1):
        # check matrix val to avoid redundant calculations
        if mobius[j]:
            count += mobius[j] * (mid // j ** 2)

    # depending on the count, either low or high is updated
    if count == N:
        high = mid  # leave bar
    elif count < N:
        low = mid + 1  # lift bar
    else:
        high = mid - 1  # lower bar

print(low)
