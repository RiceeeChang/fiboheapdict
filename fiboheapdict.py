# ----------------------------------------------------------
# 
# Wrap a Fibonacci heap as dictionary like class
# 
# ----------------------------------------------------------
from fibonacci_heap_mod import Fibonacci_heap

class MyFibonacciHeap(dict):
    # ------------------------------------------------------
    # have 3 container
    # itemlist: a list to store key
    # super   : a dict to store entry
    # heap    : a fibonacci heap to maintain the priority
    # ------------------------------------------------------


    def __init__(self, *args, **kw):
        self.itemlist = []
        self.heap = Fibonacci_heap()

        self.update(*args, **kw)

    # ------------------------------------------------------
    # __setitem__
    #   key: item name
    #   value: (int)priority
    # 
    # ------------------------------------------------------
    def __setitem__(self, key, priority):

        if type(priority) is not int:
            raise TypeError, "priority type is " + str(type(priority))
        if key in self.itemlist:
            if self[key] < priority:
                raise ValueError, "priority cannot be increase."
            else:
                entry = super(MyFibonacciHeap, self).__getitem__(key)
                self.heap.decrease_key(entry, priority)
        else:
            self.itemlist.append(key)
            super(MyFibonacciHeap, self).__setitem__(key, self.heap.enqueue(key, priority))

    # ------------------------------------------------------
    # __getitem__
    #   key: the value of the item or item name 
    #
    #   return the priority of the entry of the key
    # ------------------------------------------------------
    def __getitem__(self, key):
        return super(MyFibonacciHeap, self).__getitem__(key).get_priority()
        
    def __delitem__(self, key):
        entry = super(MyFibonacciHeap, self).pop(key)
        self.heap.delete(entry)
        self.itemlist.remove(key)


    """
    def __iter__(self):
        '''
        if self.heap.__len__() is not 0:
            i = 1
            entry = self.heap.min()
            yield entry.get_value()
            while i < self.heap.__len__():
                entry = entry.m_next
                yield entry.get_value()
                i += 1
        '''
        while self.heap.__len__() is not 0:
            entry  = self.heap.dequeue_min()
            yield entry.get_value()
            self.itemlist.remove(entry.get_value())
            super(MyFibonacciHeap, self).pop(entry.get_value())
    """


    def __repr__(self):
        string = '{\n    '
        string += ', \n    '.join([str(key) + ': ' + str(self[key]) for key in self])
        string += '\n}'
        return string

    def __len__(self):
        return super(MyFibonacciHeap, self).__len__()

    def keys(self):
        return self.itemlist

    def update(self, *args, **kw):
        if len(args) is not 0:
            if type(args[0]) is dict: # dict in tuple
                for key in args[0]:
                    self.__setitem__(key, args[0][key])
            elif type(args[0]) is list: # tuple in list in tuple
                for item in args[0]:
                    self.__setitem__(item[0], item[1])

        for key in kw:
            self.__setitem__(key, kw[key])

    def enqueue(self):
        self.__setitem__(value, priority)

    def dequeue(self, value, priority):
        entry = self.heap.dequeue_min()
        self.itemlist.remove(entry.get_value())
        super(MyFibonacciHeap, self).pop(entry.get_value())
        return entry

def test1():
    a = MyFibonacciHeap(one=1, two=2, three=3)
    print 'a', a
    b = MyFibonacciHeap(zip(['one', 'two', 'three'], [1, 2, 3]))
    print 'b', b
    c = MyFibonacciHeap([('two', 2), ('one', 1), ('three', 3)])
    print 'c', c
    d = MyFibonacciHeap({'three': 3, 'one': 1, 'two': 2})
    print 'd', d
    e = MyFibonacciHeap({'three': 3, 'one': 1, 'two': 2}, one=1, two=2, three=2)
    print 'e', e

def test2():
    # -------------------------------------------------------
    # test print MyFibonacciHeap
    # I should override/implement the __repr__ method to print
    # the heap as the format that I want.
    # ------------------------------------------------------

    q = MyFibonacciHeap()
    q['a'] = 4
    q['b'] = 2
    q['c'] = 3
    q['d'] = 1
    q['e'] = 5
    
    print 'q:', q
    print 'str(q):', str(q)
    print 'length of q:', len(q)

    del q['c']
    print q

def test3():
    q = [1,2,3]

    for i in range(len(q)):
        print i
        q.append(i+3)
        if i is 10:
            break

def test4():

    q = MyFibonacciHeap()
    print MyFibonacciHeap.__mro__



if __name__ == '__main__':
    test2()