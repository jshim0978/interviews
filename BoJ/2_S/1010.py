"""
Silver 1
"""
import math


testCases = int(input())

sites = []

for i in range(testCases):
    sites.append(list(map(int, input().split())))

def bridging(n,m):
    if n>m :
        return 
   
    diff = m-n

    if diff == 0 :
        return 1
    nnrr = diff
    nn = m
    rr = n

    for i in range(diff-1):
         nnrr *= i+1

    for i in range(m-1):
        nn *= i+1

    for i in range(n-1):   
        rr *= i+1


    cases = nn / rr / nnrr

    return round(cases)

for i in range(testCases):
    print(bridging(sites[i][0],sites[i][1]))


"""
3
2 2
1 5
13 29

"""
