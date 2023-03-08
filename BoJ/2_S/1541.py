import sys

equation = sys.stdin.readline().strip()

new = equation.split('-')

for i in range(len(new)):
    new[i] = new[i].split('+')
    new[i] = [int(x) for x in new[i]]
    new[i] = sum(new[i])

for i in range(1, len(new)):
    new[0] -= new[i]

print(new[0])