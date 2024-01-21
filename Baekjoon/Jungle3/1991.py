import sys

# case 3
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def preorder(node):
    print(node.key, end="")
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])


def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.key, end="")
    if node.right != '.':
        inorder(tree[node.right])


def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.key, end="")


n = int(input())
tree = {}

for _ in range(n):
    node, left, right = map(str, input().split())
    tree[node] = Node(key=node, left=left, right=right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])





# case 2
# def preorder(root):
#     if root != '.':
#         print(root, end='')         # root
#         preorder(tree[root][0])     # left
#         preorder(tree[root][1])     # right


# def inorder(root):
#     if root != '.':
#         inorder(tree[root][0])      # left
#         print(root, end='')         # root
#         inorder(tree[root][1])      # right


# def postorder(root):
#     if root != '.':
#         postorder(tree[root][0])    # left
#         postorder(tree[root][1])    # right
#         print(root, end='')         # root


# N = int(sys.stdin.readline().strip())
# tree = {}

# for i in range(N):
#     root, left, right = sys.stdin.readline().strip().split()
#     tree[root] = [left, right]


# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')





# case 1
# class Node:
#     def __init__(self, data, left_node, right_node):
#         self.data = data
#         self.left_node = left_node
#         self.right_node = right_node

# def pre_order(node):
#     print(node.data, end='')
#     if node.left_node != None:
#         pre_order(tree[node.left_node])

# n = int(sys.stdin.readline())
# tree = {}

# for i in range(n):
#     data, left_node, right_node = list(map(int, sys.stdin.readline().split()))
#     if left_node == "None":
#         left_node = None
#     if right_node == "None":
#         right_node = None
#     tree[data] = Node(data, left_node, right_node)

# pre_order(tree['A'])
