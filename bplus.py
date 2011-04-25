# -*- coding: UTF-8 -*-
#
# A B+ tree, made in python.
#
# (c) ane 2008 <ane@iki.fi>

import bisect, random

class BPlusTree:
    def __init__(self, max_size):
        root = 'root' # for dict 
        self.max_size = max_size
        self.dict = {root:[]}
        self.root = root
        
    def insert(self, val):
        root = self.root
        lastroot = root
        while root:
            root_list = self.dict[root]
            # can we insert more nodes? 
            # if yes, insert and sort using bisect.sort
            if len(root_list) < self.max_size:
                bisect.insort(root_list, val)
                return
            # nope, so split the node in two
            else:
                x = bisect.bisect(root_list, val)
                if x == len(root_list):
                    # move out the last element to next node
                    # note: python's magic array mechanics do the
                    # work for us and we don't need fancy next-pointers
                    a = root_list[-1]
                    root_list[-1] = val
                    tmp = self.dict.get(a, None)
                    if tmp:
                        self.dict[val] = tmp
                        del self.dict[a]
                    self.insert(a)
                    return
                else:
                    root = root_list[x]
                    self.dict.setdefault(root, [])
                    
    def get_sorted_data(self):
        result = []
        self.verbose(self.dict[self.root], result)
        return result
    
    def verbose(self, root_list, result):
        for r in root_list:
            if r != self.root and self.dict.has_key(r):
                self.verbose(self.dict[r], result)
            result.append(r)

    def find_key_data(self, key):
        if self.dict.has_key(key):
            return self.dict[key]
        # not found, is it a leaf?
        else:
            for node in self.dict:
                if key in self.dict[node]:
                    # it's a leaf
                    return []
        
def test():
    data = [chr(x) for x in range(65, 90)]
    orig_data = data[:]
    random.shuffle(data)
    b = BPlusTree(3)
    for d in data:
        b.insert(d)
    print "Root: " + b.root
    import pprint
    pprint.pprint(b.dict)
    print '*' * 50
    sorted = b.get_sorted_data()
    assert(sorted == orig_data)
    print '=' * 50

test()
