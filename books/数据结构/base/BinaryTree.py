#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-18 23:11:46
# @Author  : cantfu (marcolxx@qq.com,cantfuLi@gmail.com)
# @Link    : https://github.com/cantfu

class BinaryTree:
    ''' 链表存储的二叉树 
    data: 数据域
    lchild: 左子树
    rchild: 右子树
    '''

    def __init__(self, data, lchild: BinaryTree, rchild: BinaryTree):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


    def preCreateTree(dataArr):
        """ 遍历 dataArr,并按照先序创建二叉树
        约定 dataArr 中 '#' 表示
        @param dataArr: 用于创建二叉树的data数组 
        """
        # TODO
        return None

    def preCreateTree(dataArr):
        """ 遍历 dataArr,并按照中序创建二叉树 
        @param dataArr: 用于创建二叉树的data数组 
        """
        # TODO
        return None

    def preCreateTree(dataArr):
        """ 遍历 dataArr,并按照后序创建二叉树 
        @param dataArr: 用于创建二叉树的data数组 
        """
        # TODO
        return None

    def preOrderTraverse(self, node: BinaryTree = self):
        """ 递归先序遍历二叉树 
        @param node: 当前遍历的节点
        """
        if(node):
            print(node.data)  # 替换为相应的 visit 函数
            preOrderTraverse(node.lchild)
            preOrderTraverse(node.rchild)
        return None

    def inOrderTraverseNonRecursive(self):
        """ 非递归中序遍历二叉树 """
        # TODO 以下为伪码
        s = InitStack()
        p = self
        while(p || !s.isEmpty()):
            if(p): # 根指针进栈。遍历左子树
                s.push(p)
                p = p.lchild
            else: # 根指针退栈，访问根节点，遍历右子树
                p = s.pop()
                p.visit()
                p = p.rchild
        return OK
    
    def inOrderTraverse(self):
        """ 中序遍历二叉树 """
        # TODO
        return None

    def postTraverse():
        """ 后序遍历二叉树 """
        # TODO
        return None

    

