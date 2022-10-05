"""STACK - Подобие"""
import time


class Stack:
    def __init__(self):
        self.stack = []
        self.max = None

    def push(self, item):
        self.stack.append(item)
        if len(self.stack) == 1 or item > self.max:
            self.max = item

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        if len(self.stack) == 0:
            self.max = None
        elif removed == self.max:
            self.max = self.stack[0]
            for value in self.stack:
                if value > self.max:
                    self.max = value
        return removed

    def get_size(self):
        return self.max

    def is_empty(self):
        return self.stack == 0


stack = Stack()
print("============Старт теста============")
start_time = time.time()
for i in range(5000):
    stack.push(i)
print(f"Время добавления элементов = {time.time() - start_time} сек")
print(f"Количество элементов = {stack.get_size()} \n")
print("============Старт теста============")
start_time = time.time()
for i in range(stack.get_size()+1):
    stack.pop()
print(f"Время удаления элементов = {time.time() - start_time} сек")
print(f"Количество элементов = {stack.get_size()}")