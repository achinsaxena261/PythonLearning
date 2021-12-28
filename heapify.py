from enum import Enum


class HeapType(Enum):
    min = 1
    max = 2


class Heapify:

    def __init__(self):
        self.arr = []

    def do_heapify(self, item, heap_type):
        self.arr.append(item)

        if heap_type == HeapType.max:
            if len(self.arr) % 2 == 0:
                return self.balance_heap_max(int((len(self.arr) - 1) / 2), len(self.arr) - 1)
            else:
                return self.balance_heap_max(int((len(self.arr) - 2) / 2), len(self.arr) - 1)
        if heap_type == HeapType.min:
            if len(self.arr) % 2 == 0:
                return self.balance_heap_min(int((len(self.arr) - 1) / 2), len(self.arr) - 1)
            else:
                return self.balance_heap_min(int((len(self.arr) - 2) / 2), len(self.arr) - 1)

    def balance_heap_max(self, n, i):
        if i < 1:
            return

        if self.arr[n] < self.arr[i]:
            self.arr[i] = self.arr[n] + self.arr[i]
            self.arr[n] = self.arr[i] - self.arr[n]
            self.arr[i] = self.arr[i] - self.arr[n]
            return self.balance_heap_max(int(n / 2), n)

    def balance_heap_min(self, n, i):
        if i < 1:
            return

        if self.arr[n] > self.arr[i]:
            self.arr[i] = self.arr[n] + self.arr[i]
            self.arr[n] = self.arr[i] - self.arr[n]
            self.arr[i] = self.arr[i] - self.arr[n]
            return self.balance_heap_min(int(n / 2), n)
