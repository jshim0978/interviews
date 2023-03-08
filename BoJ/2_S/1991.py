import sys

N = int(sys.stdin.readline().strip())
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

start = list(tree.keys())[0]


def preorder_traversal(root):
    if root != '.':
        print(root, end='')
        preorder_traversal(tree[root][0])
        preorder_traversal(tree[root][1])


def inorder_traversal(root):
    if root != '.':
        inorder_traversal(tree[root][0])
        print(root, end='')
        inorder_traversal(tree[root][1])


def postorder_traversal(root):
    if root != '.':
        postorder_traversal(tree[root][0])
        postorder_traversal(tree[root][1])
        print(root, end='')


preorder_traversal(start)
print()
inorder_traversal(start)
print()
postorder_traversal(start)