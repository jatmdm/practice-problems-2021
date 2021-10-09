# Binary Search Tree

class Node:
    """Node for binary search tree"""
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __eq__(self, other):
        return self.value == other.value


class BinarySearchTree:
    """Binary Search Tree"""
    def __init__(self, root: Node = None):
        self.root = None

    def insert(self, value, cur=None):
        """Inserts a node with value :value: into the tree"""
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
        """Removes a Node with value :value:"""
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
        """Returns an array with the contents of the BST in the specified order"""
        return self._to_list(self.root, order)

    #stub
    def __contains__(self, item):
        pass