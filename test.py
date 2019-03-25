#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "问道编程"
__date__ = "2019/03/19 10:12"


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 思路二：原地拼接
        phead = ListNode(0)
        p = phead
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return phead.next


l1 = ListNode(1)
l1.add_(2)
l1.add_(4)

l2 = ListNode(1)
l2.add_(3)
l2.add_(4)

res = Solution()

res.mergeTwoLists(l1, l2)
