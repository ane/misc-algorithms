# -*- encoding: UTF-8 -*-
# Trie-tree
# (c) ane 2009 <ane@iki.fi>

class Trie:
    def __init__(self):
        self.root = [None, {}]
    
    # Adds a key to the trie
    def add(self, key, value):
        node = self.root
        for k in key:
            node = node[1].setdefault(k, [None, {}])
        node[0] = value

    # Finds a key in the trie
    def find(self, key):
        node = self.root
        for k in key:
            try:
                node = node[1][k]
            except KeyError:
                return None
        return node[0]
    
    # Walks the Trie 
    def __walk(self, d):
        klist = []
        keys = d.keys()
        for key in keys:
            z = '' + key
            if len(d[key]) > 0:
                for item in d[key]:
                    if type(item) == type({}):
                        l = self.__walk(item)
                        for i in l:
                            klist.append(z + i)
            klist.append(z)
        return klist

    def __contains__(self, key):
        curr_node = self.root
        for char in key:
            curr_node_1 = curr_node[1]
            if char in curr_node_1:
                curr_node = curr_node_1[char]
            else:
                return False
        return True

    
    # Gets all keys of the trie
    def keys(self):
        k = self.__walk(self.root[1])
        klist = []
        for key in k:
            if self.find(key) != None:
                klist.append(key)
        return klist
    
    # Prints all the values in the trie
    def values(self):
        i = []
        for k in self.keys():
            i.append(self.find(k))
        return i
        
        
if __name__ == "__main__":    
    t = Trie()
    t.add("a", "1")
    t.add("ab", "2")
    t.add("l", "3")
    t.add("loool", "4")
    print(t.values())

