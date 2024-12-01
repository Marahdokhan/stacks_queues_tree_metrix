# task 1

# task 2
def reverse_orders(book_ids):
    order = []
    for book_id in book_ids:
        order.append(book_id)
        
    reversed_ids = []
    while order:
        reversed_ids.append(order.pop())
    return reversed_ids

print(reverse_orders([101, 102, 103, 104]))
print(reverse_orders([1, 2, 3]))
print(reverse_orders([]))
print(reverse_orders([42]))  


# task 3
def undo_actions(actions, undosteps):
    stack = actions[:]
    for _ in range(undosteps):
        if stack:
            stack.pop()
    return stack

print(undo_actions(["type A", "type B", "delete"], 1))
print(undo_actions(["A", "B"], 1))
print(undo_actions(["X"], 2))
print(undo_actions([], 1))  

# task 4
def is_balanced(s):
    options = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in s:
        if char in options.values():
            stack.append(char)
        elif char in options.keys():
            if not stack or stack.pop() != options[char]:
                return False
    return not stack

print(is_balanced("([{}])"))
print(is_balanced("([])"))
print(is_balanced("([)]"))
print(is_balanced(""))   

# task 5
def serve_customers(customers):
    custs_name = []
    while customers:
        custs_name.append(customers.pop(0))
    return custs_name

print(serve_customers(["Alice", "Bob", "Charlie"]))
print(serve_customers(["John", "Doe"]))
print(serve_customers([]))
print(serve_customers(["OnlyOne"])) 

# task 6
class Person:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

def search_name(root, name):
    if root is None:
        return False
    if root.name == name:
        return True    
    for child in root.children:
        if search_name(child, name):
            return True
    
    return False

# task 13
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    if not root:
        return True
    
    return is_mirror(root.left, root.right)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
print(isSymmetric(root1))

root2 = TreeNode(1)
root2.left = TreeNode(2)
print(isSymmetric(root2))


