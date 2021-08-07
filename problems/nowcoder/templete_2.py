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