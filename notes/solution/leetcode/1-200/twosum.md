# 两数之和

## 题目
给定列表 `nums` 和整数 `target`，找到下标 $i$, $j$ ($i \ne j$)，使得 nums[$i$] + nums[$j$] = target

## 思路
遍历数组 `nums`，假设到了第 $i$ 个数 $x=$nums[$i$]，这时我们想知道，`nums` 有没有数等于 target - $x$。但是不可以拿到一个 nums[$i$] 就去遍历一遍 `nums`，这样会使得算法的复杂度增加。自然而然的想法是使用哈希表。具体实现方法都在代码里：

## 代码

[01_two-sum.py](../../../../problems/leetcode/1-200/01_two-sum.py)

```python
def twosum(nums, target):
    hashtable = dict()
    for i, num in enumerate(nums):
        if (target - num) in hashtable:
            return [hashtable[target-num], i]
        hashtable[num] = i
    return []
```

## 复杂度分析

+ **时间复杂度：** $O(N)$，其中 $N$ 是数组中的元素数量。对于每一个元素 $x$，我们可以 $O(1)$ 地寻找 target - $x$。

+ **空间复杂度：** $O(N)$，其中 $N$ 是数组中的元素数量。主要为哈希表的开销。