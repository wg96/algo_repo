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