import os, json

class Memory:
    zero = 0
    store = []
    ten = { "dump-range": (1,9) }

class Driver:
    # a memory driver for Memory class
    def __init__(self):
        self.dump_range = Memory.ten['dump-range']
        self.store = Memory.store
    
    def c__dump(self, sd):
        self.store.append(sd)
        return self.store[-1] # get last object
    
    def c__load(self, memindx):
        return self.store[memindx]
    
    def c__delt(self, memindx):
        del self.store[memindx]
        return self
    
    def c__clrmem(self):
        self.store = Memory.store
        return self

class mem0:
    # the actual module for managing data in memory
    def __init__(self):
        self.driver = Driver()
        self.mem = Memory
    
    def mkobj(self, obj):
        return self.driver.c__dump(obj)
    
    def ldobj(self, indx):
        return self.driver.c__load(indx)
    
    def dlobj(self, indx):
        self.driver.c__delt(indx)
        return self
    
    def clrmem(self):
        self.driver.c__clrmem()
        return self