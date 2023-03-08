N = int(input())
count = 0
ans = []
alpha_arr = []
for _ in range(N):
    flag = True
    group_word = str(input())

    while group_word != '':
        alpha_arr.clear()
        alpha_arr.append(group_word[0])
        group_word = group_word[1:]
        for _ in range(len(alpha_arr)):
            if group_word.__contains__(alpha_arr[_]) and group_word[0] != alpha_arr[-1]:
                flag = False

                break

    if flag:
        count += 1


print(count)