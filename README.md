## 目录

   * [1 两数之和](#1-两数之和) 
   * 

  

    

#### 1 两数之和  
给定一个整数数组`nums`和一个目标值`target`，请你在该数组中找出和为目标值的那`两个`整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
```
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```
分析思路：遍历列表，判断target-nums[i]是否在nums[i+1::]中，返回i和target-nums[i]在nums中的索引  
```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            anothers = nums[i+1::]
            if target-nums[i] in anothers:
                return [i,anothers.index(target-nums[i] )+i+1]
```
执行用时 : 1148 ms  
内存消耗 : 13.6 MB  
最优代码：看了网上大神的解答，使用`enumerate()`将`nums`组合成一个索引，遍历索引和值，将索引、值分别存到字典的值和键，反查`target`和当前
值的差值是否在字典中的key中，如果不存在继续存储索引和值，如果存在，返回当前索引和匹配字典key的值（也就是nums的索引）
```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = dict()
        for k,v in enumerate(nums):   # enumerate()方法将可迭代对象组合成一个索引序列
            other_num = target - v
            if other_num in a.keys():
                return [a[other_num],k]
            a[v] = k   # 将值作为字典的key，将索引作为字典的值
```
执行用时 : 88 ms  
内存消耗 : 14.1 MB  

#### 2 两数相加  
给出两个` 非空 `的链表用来表示两个非负的整数。其中，它们各自的位数是按照` 逆序 `的方式存储的，并且它们的每个节点只能存储` 一位 `数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
```
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807 
```
分析思路一：将两个链表转换为数值，相加后，将结果再转换为链表
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = list()
        b = list()
        while l1:
            a.append(str(l1.val))
            l1 = l1.next
        while l2:
            b.append(str(l2.val))
            l2 = l2.next
        a.reverse()
        b.reverse()
        a, b = int(''.join(a)), int(''.join(b))
        s = a + b
        l3 = ListNode(s%10)
        cur = l3
        while s//10:
            s = s//10
            cur.next = ListNode(s%10)
            cur = cur.next
        return l3
```
执行用时 : 236 ms  
内存消耗 : 13.1 MB  
分析思路二：对其中一个链表进行遍历，两个链表相同位置的节点之和大于10的进位，当一个链表到达尾节点时停止遍历，同时需要注意遍历结束时最后节点之和的情况
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(l1.val+l2.val)
        cur = l3
        while l1.next or l2.next:

            if cur.val >= 10:
                if l1.next:
                    l1.next.val += 1
                else:
                    l2.next.val += 1
                cur.val = cur.val % 10
                
            if l1.next and l2.next:
                l1, l2 = l1.next, l2.next
                cur.next = ListNode(l1.val+l2.val)
            elif l1.next:
                l1 = l1.next
                cur.next = ListNode(l1.val)
            elif l2.next:
                l2 = l2.next
                cur.next = ListNode(l2.val)
            cur = cur.next
                
        if cur.val >= 10:
            cur.next = ListNode(1)
            cur.val = cur.val % 10
            
        return l3
```
执行用时 : 124 ms  (多次测试，结果不一致，196ms，204ms，220ms)
内存消耗 : 13.2 MB  
贴一下网上96ms（我提交后是184ms）的代码：
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add = 0     
        l3 = ListNode(0)
        node = l3
        while l1 or l2:
            cur = ListNode(add)
            if l1:
                cur.val += l1.val
                l1 = l1.next
            if l2:
                cur.val += l2.val
                l2 = l2.next
            add = cur.val // 10
            cur.val = cur.val % 10
            node.next, node = cur, cur
        if add:
            node.next = ListNode(add)
        return l3.next
```
