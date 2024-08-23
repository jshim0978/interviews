a,b = [int(x) for x in input().split()]

if a > b:
    print('>')
elif b > a:
    print('<')
else :
    print('==')