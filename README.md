## 目录

   * [1 两数之和](#1-两数之和) 
   * [2 两数相加](#2-两数相加) 

  

    

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
        # 另一个版本：
        # l3 = l1
        # while l1:
        #     l1.val = l1.val + l2.val
        #     if l1.val > 9 and l1.next:
        #         l1.val, l1.next.val = l1.val%10, l1.next.val+1
        #     elif l1.val > 9:
        #         l1.val = l1.val%10
        #         l1.next = ListNode(1)
        #     if l1.next and not l2.next:
        #         l2.next = ListNode(0)
        #     elif l2.next and not l1.next:
        #         l1.next = ListNode(0)
        #     l1, l2 = l1.next, l2.next
        # return l3
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

#### 3 无重复字符的最长子串  
给定一个字符串，请你找出其中不含有重复字符的` 最长子串 `的长度。  

示例 1:
```
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```
示例 2:
```
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```
示例 3:
```
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

分析思路一：遍历str，新建列表存储子串，将新字符入栈，如果新的字符不在子集中，不做处理；如果在，删除子集中字符及之前的字符；
```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        max_list = list()
        for i in s:
            if i in max_list:
                max_list = max_list[max_list.index(i)+1:]
                max_list.append(i)
            else:
                max_list.append(i)
                max_length = max(len(max_list),max_length)
        return max_length
```
最优代码： 使用字符串存储子集
```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ''
        longestlength = 0

        for le in s:
            if le not in substring:
                substring = substring + le
            else:
                longestlength = max(len(substring),longestlength)
                substring = substring[substring.index(le)+1:]
                substring = substring + le
        longestlength = max(len(substring),longestlength)

        return longestlength
```

### 4 寻找两个有序数组的中位数  
给定两个大小为` m `和` n `的有序数组` nums1 `和` nums2`。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为` O(log(m + n))`。

你可以假设` nums1 `和` nums2 `不会同时为空。

示例 1:
```
nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
```
示例 2:
```
nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
```
分析思路：合并数组后，根据数组长度的奇偶性，返回不同的值
```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = sorted(nums1+nums2)
        length = len(nums3)
        mid_index = int(length / 2)
        return (nums3[mid_index-1]+nums3[mid_index])/2 if mid_index==length/2 else nums3[mid_index]
```

