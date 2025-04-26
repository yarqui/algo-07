class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def get_height(node: AVLNode) -> int:
    if not node:
        return 0
    return node.height


def get_balance(node: AVLNode) -> int:
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z: AVLNode) -> AVLNode:
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def right_rotate(y: AVLNode) -> AVLNode:
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def min_value_node(node: AVLNode) -> AVLNode:
    if node is None:
        return None

    while node.left is not None:
        node = node.left

    return node


def max_value_node(node: AVLNode) -> AVLNode:
    if node is None:
        return None

    while node.right is not None:
        node = node.right

    return node


def insert(root: AVLNode, key) -> AVLNode:
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def sum_keys(root: AVLNode) -> int:
    if root is None:
        return 0

    return root.key + sum_keys(root.left) + sum_keys(root.right)


root = None
keys = [10, 3, 30, 5, 28, 4, -30]

for key in keys:
    root = insert(root, key)


print("Max value: ", max_value_node(root).key)
print("Min value: ", min_value_node(root).key)
print("Sum of all keys in the tree:", sum_keys(root))
