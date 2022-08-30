import sys
from collections import deque

equation = sys.stdin.readline()


def to_postfix(e):
    stack = deque()
    postfix = []
    for i in e:
        if i == '*' or i == '/':
            while stack and stack[-1] != '(' and (stack[-1] == '*' or stack[-1] == '/'):
                postfix.append(stack.pop())
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.append(i)
        elif i.isalpha():
            postfix.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
    while stack:
        postfix.append(stack.pop())
    return postfix


ans = ''
temp = to_postfix(equation)
for i in range(len(temp)):
    ans += temp[i]

print(ans)