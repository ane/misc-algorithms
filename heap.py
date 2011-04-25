# -*- encoding: UTF-8 -*-
# Binary heap (max-heap)
# (c) ane 2009 <ane@iki.fi>

import time, random

class Heap:
    def __init__(self):
        self.store = []
        self.count = 0
        
    # Inserts an element
    def insert(self, element):
        self.store.append(element)
        self.ascend(-1)   
      
    # Ascends (sifts up) an item to the top
    def ascend(self, loc):
        if loc < 0:
            child = len(self.store) - 1
        else:
            child = loc
        parent = self.parent(child)
        while parent < child and self.better(child, parent):
            self.swap(child, parent)
            child = parent
            parent = self.parent(child)
    
    def parent(self, child):
        if child == 0:
            return 0
        return (child - 1) / 2
    
    # Swaps two items
    def swap(self, a, b):
        self.store[a], self.store[b] = self.store[b], self.store[a]
    
    # A dummy comparison
    def better(self, a, b, d=False):
        if d: print(a, b)
        return self.store[a] > self.store[b]

    # Returns the smaller child of node at position loc
    def better_child(self, loc):
        a = 2*loc+1
        b = 2*loc+2
        count = len(self.store)
        if a < count and b < count:
            if self.better(a, b):
                return a
            else:
                return b
        elif a < count:
            return a
        else: 
            return loc
    
    # Sifts an item down
    def lower(self, loc):
        p = loc
        child = self.better_child(p)
        while p < child and self.better(child, p):
            self.swap(child, p)
            p = child
            child = self.better_child(p)
    
    # Heapifies the tree
    def heapify(self):
        start = int((len(self.store) - 2) / 2)
        while start >= 0:
            self.lower(start)
            start = start - 1

    # Adds an element 
    def push(self, element):
        self.store.append(element)
    
    # Removes the smallest element
    def delete_min(self):
        if self.is_empty():
            return None
        res = self.store[0]
        last = self.store.pop()
        if not self.is_empty():
            self.store[0] = last
            self.lower(0)
        return res
   
    def is_empty(self):
        return len(self.store) == 0
    def min(self):
        return self.store[0]
    def items(self):
        return self.store
    
if __name__ == '__main__':
    times = []
    heap = Heap()
    bla = range(100)
    for i in bla:
        heap.push(bla[random.randint(0,99)])
    print(heap.items())
    start = time.clock()
    heap.heapify()
    end = time.clock() - start
    print(heap.items())
    print("Heapifying took", end*1000, "milliseconds for",len(heap.items()),"elements")

