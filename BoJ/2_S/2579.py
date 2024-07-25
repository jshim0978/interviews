# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.



def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    dp = [0] * n
    
    if n == 1:
        return arr[0]
    elif n == 2:
        return arr[0] + arr[1]
    elif n == 3:
        return max(arr[0] + arr[2], arr[1] + arr[2])
    
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
        
    return dp[n-1]



print(solution())