"""Реализация стека на основе односвязного списка"""
import time

# Узел односвязного списка
class Node:
    def __init__(self, value):
        self.value = value          # Абстраткные данные
        self.next  = None           # Типа указатель на следующий узел

class Stack:
    def __init__(self):
        self.head = Node("head")    # При создании объекта указатель указывает на голову (вершину) стека
        self.size = 0
    # Получить размер стека
    def get_size(self):
        return self.size
    # Проверка на заполненность
    def is_empty(self):
        return self.size == 0
    # Добавление элемента в стек + имитация работы указателей из С++
    def push(self, value):
        node = Node(value)          # Создали новый узел
        node.next = self.head.next  # Указатель нового узла, теперь указывает на предыдущий элемент
        self.head.next = node       # Указатель головы (вершин) указывает на добавленный элемент
        self.size += 1              # Увеличили счетчик элементов
    # Вернуть елемент из вершины стека и удалить его
    def pop(self):
        if self.is_empty():
            return 0
        remove = self.head.next                 # Сохранить указатель на предыдущий объект
        self.head.next = self.head.next.next    # В указатель на голову положить указатель на предыдущий элемент
        self.size -= 1                          # Декримент
        return remove.value                     # вернуть данные текущего удаляемого объекта
    # Получить верхний элемент в стеке
    def peek(self):
        if self.is_empty():
            return None
        return self.head.next.value
    # Удобный вывод на экран
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + " -> "
            cur = cur.next
        return out[:-3]
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 21):
        stack.push(i)
    print(stack)

    print("============Старт теста============")
    start_time = time.time()
    for i in range(500000):
        stack.push(i)
    print(f"Время добавления элементов = {time.time() - start_time} сек")
    print(f"Количество элементов = {stack.get_size()} \n")
    print("============Старт теста============")
    start_time = time.time()
    for i in range(stack.get_size() + 1):
        stack.pop()
    print(f"Время удаления элементов = {time.time() - start_time} сек")
    print(f"Количество элементов = {stack.get_size()}")