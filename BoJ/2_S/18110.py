
n = int(input())

if n ==0 :
    print(0)
    quit()

sli = round((n * 3/20) + 0.000001)
votes = []

for i in range(n):
    votes.append(int(input()))

votes.sort()


if sli > 0 :
    votes = votes[sli:-sli]



ss = sum(votes)

print(round((ss + 0.000001) / len(votes)))
