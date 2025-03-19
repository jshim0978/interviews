li = str(input())

half = len(li)//2
first = li[:half]
last = li[half:]
temp1, temp2 = 0,0
for i in range(half):
    temp1 += int(first[i])
    temp2 += int(last[i])    

if temp1 == temp2:
    print("LUCKY")
else:
    print("READY")