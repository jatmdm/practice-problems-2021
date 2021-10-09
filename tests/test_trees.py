import pytest
import random
from trees.BinarySearchTree import BinarySearchTree


def test_bst_insert():
    bst = BinarySearchTree()
    bst.insert(0)
    assert bst.root


def test_bst_integer():
    seed = 372478234873
    random.seed(seed)
    values = [random.randint(0, 100) for i in range(100)]

    bst = BinarySearchTree()
    for val in values:
        bst.insert(val)

    inorder = bst.to_list()
    assert inorder == sorted(values)

def test_bst_preorder_0():
    preorder_values = list(range(10))
    bst = BinarySearchTree()
    for val in preorder_values:
        bst.insert(val)

    preorder = bst.to_list(order='preorder')
    assert preorder == sorted(preorder_values)


def test_bst_preorder_1():
    preorder_values = [4, 2, 3, 5, 1]
    bst = BinarySearchTree()
    for val in preorder_values:
        bst.insert(val)

    preorder = bst.to_list(order='preorder')
    assert preorder == [4, 2, 1, 3, 5]


def test_bst_postorder():
    postorder_values = [4, 2, 3, 5, 1]
    bst = BinarySearchTree()
    for val in postorder_values:
        bst.insert(val)

    postorder = bst.to_list(order='postorder')
    assert postorder == [1, 3, 2, 5, 4]


