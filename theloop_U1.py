import time


class Unit1:
    def __init__(self) -> None:
        ...

    def branch_1(self, num):
        self.print_pl(f"循环 #{num}。选择：直行、回头、等待还是上楼？")

    def print_pl(self, msg):
        for i in msg:
            print(i, end='')
            time.sleep(0.08)

u = Unit1()
