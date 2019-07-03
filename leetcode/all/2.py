#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Cantfu
# @Link    : https://github.com/cantfu/DailyCode

# 题目
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 【难点：边界条件】
# 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 输出的是原有的l1链
        p_l1 = l1
        p_l2 = l2
        p_l3 = p_l1
        forward = 0 # 进位
        temp = p_l1.val + p_l2.val + forward
        p_l1.val = temp%10
        forward = temp // 10
        # print(not(p_l1 and p_l2)) # False
        while (p_l1.next and p_l2.next):
            p_l1 = p_l1.next
            p_l2 = p_l2.next
            temp = p_l1.val + p_l2.val + forward
            print("temp: %d" % temp)
            p_l1.val = temp%10
            forward = temp // 10
            print("forward: %d" % forward)
            

        if not p_l1.next: # l1為空了
            if not p_l2.next: # 兩者都為空了
                if forward > 0: #两者等长，且最后进一位
                    print("forwardd: %d" % forward)
                    print(p_l1)
                    p_l1.next = ListNode(1)
                    print(p_l1)
                    return l1
            print("=========")
            p_l1.next = p_l2.next
            
            while forward > 0 and p_l1.next:
                p_l1 = p_l1.next
                temp = p_l1.val + forward
                print("temp: %d" % temp)
                p_l1.val = (temp) % 10
                forward = temp // 10
            if forward > 0:
                p_l1.next = ListNode(1)
        else: # l2為空了,且l1不為空
            
            while forward > 0 and p_l1.next:
                p_l1 = p_l1.next
                temp = p_l1.val + forward
                p_l1.val = (temp) % 10
                forward = temp // 10
            if forward > 0:
                p_l1.next = ListNode(1)
        return l1
            
if __name__ == '__main__':
    s = Solution()
    # l1 = ListNode(2)
    # l1.next = ListNode(4)
    # l1.next.next =  ListNode(3)
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next =  ListNode(4)
    l1 = ListNode(1)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    
    # 243 + 564 = 708   倒序
    l3 = s.addTwoNumbers(l1, l2)
    print(l3.val)
    print(l3.next.val)
