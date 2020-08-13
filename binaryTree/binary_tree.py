# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/8/11 11:22
# file: binary_tree.py
# IDE: PyCharm

class Node():
    """节点类"""
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None


class Tree():
    """树类"""
    def __init__(self):
        self.root = None

    def add(self, elem):
        node = Node(elem)

        if self.root is None:
            self.root = node
        else:
            queue = []

            queue.append(self.root)

            # 对已有的节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def breadth_travel(self):
        """利用队列实现树的层次遍历"""
        if self.root is None:
            return

        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.elem, end=" ")
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)


    def preorder(self, root):
        """先序遍历"""
        if root is None:
            return
        print(root.elem, end=" ")
        self.preorder(root.lchild)
        self.preorder(root.rchild)


    def inorder(self, root):
        """中序遍历"""
        if root is None:
            return
        self.inorder(root.lchild)
        print(root.elem, end=" ")
        self.inorder(root.rchild)


    def postorder(self, root):
        """后序遍历"""
        if root is None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem, end=" ")








if __name__ == '__main__':
    t = Tree()

    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)



    t.breadth_travel()
    print()
    t.preorder(t.root)
    print()
    t.inorder(t.root)
    print()
    t.postorder(t.root)

