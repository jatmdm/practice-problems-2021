# Binary Search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __eq__(self, other):
        return self.value == other.value


class BinarySearchTree:
    def __init__(self, root: Node = None):
        self.root = None

    def insert(self, value, cur=None):
        if not self.root:
            self.root = Node(value)
            return
        cur = self.root
        while cur is not None:
            if value >= cur.value:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(value)
                    return
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(value)
                    return

    def remove(self, node: Node):
        pass

    def _to_list(self, node, order='inorder'):
        if node is None:
            return []
        else:
            left = self._to_list(node.left, order=order)
            right = self._to_list(node.right, order=order)
            if order == 'inorder':
                return left + [node.value] + right
            elif order == 'preorder':
                return [node.value] + left + right
            elif order == 'postorder':
                return left + right + [node.value]

    def to_list(self, order='inorder'):
        return self._to_list(self.root, order)
