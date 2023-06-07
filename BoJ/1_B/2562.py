
li = []
ind = 0
for i in range(9):
    tok = int(input())
    li.append(tok)
    if max(li) == tok:
        ind = i + 1


print(max(li))
print(ind)