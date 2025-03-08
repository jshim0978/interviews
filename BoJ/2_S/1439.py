# 뒤집기
import math
s = input()



# print(s)

# get different number of blocks
count = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        continue
    else:
        count+=1

print(math.ceil(count/2))  
   