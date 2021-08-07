# 牛客网 ACM 模式 Python 输入输出

## 两种接收输入的办法

1. `input()`

`input()` 函数会自动把输入末尾的换行符 `/n` 给删除

2. `sys.stdin.readline()`

`sys.stdin.readline()` 不会去掉换行符，一般和 `strip()` 结合使用，即 `sys.stdin.readline().strip()` ，这样和 `input()` 的效果一样

## 常见 3 种输入情况

标准输入方式会把输入转成字符或字符串形式。若要的是整数，需转换一下

### 情况1:单行单输入

1. 方法一

```python
num = int(input())
```

2. 方法二

```python
import sys

num = int(sys.stdin.readline().strip())
```

 ### 情况2:单行多输入

```python
# 多个输入各自赋值
m, n = map(int, input().split())

# 将多个输入转换为数组
arr = list(map(int, input().split()))
```

### 情况3:多行多输入

假设首行输入 `row_num` 用于确定接下来输入的行数

```python
row_num = int(input())
for _ in range(row_num):
  arr = list(map(int, input().split()))
```

## 通用模板

### 精简版

[templete_1.py](../../problems/nowcoder/templete_1.py)

```python
#coding=utf-8

if __name__ == "__main__":
    row_num = int(input())
    for _ in range(row_num):
        arr = list(map(int, input().split()))
        # TODO
        print(arr)
```

### 循环版

通常情况下可使用循环读入，因为调试时会使用多个示例

[templete_2.py](../../problems/nowcoder/templete_2.py)

```python
#coding=utf-8

if __name__ == "__main__":
    try:
        while True:
            row_num = int(input())
            for _ in range(row_num):
                line = input()
                if line == "":
                    break
                arr = list(map(int, line.split()))
                # TODO
                print(arr)
    except:
        pass
```

### 使用 `sys.stdin.readline()`

[templete_3.py](../../problems/nowcoder/templete_3.py)

```python
#coding=utf-8
import sys

if __name__ == "__main__":
    try:
        while True:
            row_num = int(sys.stdin.readline().strip())
            for _ in range(row_num):
                line = sys.stdin.readline().strip()
                if line == "":
                    break
                arr = list(map(int, line.split()))
                # TODO
                print(arr)
    except:
        pass
```

## 参考

[牛客网Python 输入输出整理](https://www.jianshu.com/p/ba55536e0a39)

[牛客网 多行输入输出问题 Python3 模板样例](https://blog.csdn.net/qq_39938666/article/details/101004633)

[牛客网 Python 编程输入规范](https://www.cnblogs.com/simplepaul/p/7272715.html)

