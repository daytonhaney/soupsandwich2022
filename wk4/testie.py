import os
import sys
import testie

print("ok")


def calc(file):
    bytes_size = os.path, getsize(file)
    mb_size = int(bytes_size/1024**2)
    print(mb_size, "MB")


if __name__ == '__main__':
    file = sys.argv[-1]
    calc(file)
