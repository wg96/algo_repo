#coding=utf-8

def twosum(nums, target):
    hashtable = dict()
    for i, num in enumerate(nums):
        if (target - num) in hashtable:
            return [hashtable[target-num], i]
        hashtable[num] = i
    return []

def test(nums, target):
    print("Input, nums:", nums, "target:", target)
    print("Output,", twosum(nums, target))

def main():
    test([2,7,11,15], 9)
    test([3,2,4], 6)
    test([3,3], 6)


if __name__ == "__main__":
    main()

