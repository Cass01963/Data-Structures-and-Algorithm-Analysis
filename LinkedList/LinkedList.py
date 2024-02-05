# LinkedList class
# I have given you the basic structure of the class.
# TO DO: Complete the methods that have "pass" in their places
# and add comments for each method - 1 or 2 lines saying what it does
# Then test it using the LL_Tester file before doing the assignment
# YOUR NAME:

from Node import Node

class LinkedList:
    def __init__(self):
        self._head = Node()
        self._tail = Node()
        self._curr = Node()
    
    #changes or returns where the pointers are pointing
    #we use these instead of normal getters/setters so folks don't mess with our pointers
    # here = a Node object
    def setHead(self, here):
        self._head.link = here
    def getHead(self):
        return self._head.link
    def setTail(self, here):
        self._tail.link = here
    def getTail(self):
        return self._tail.link
    def setCurr(self, here):
        self._curr.link = here
    def getCurr(self):
        return self._curr.link
    
    def isEmpty(self):
        if self.getHead() == None:
            return True
        return False
    
    def isBeginning(self):
        if self.getCurr() == self.getHead():
            return True
        else:
            return False
    
    def isEnd(self):
        if self.getCurr() == self.getTail():
            return True
        else:
            return False
    
    def goBeginning(self):
        self.setCurr(self.getHead())
    
    def goEnd(self):
        self.setCurr(self.getTail())
        
    def getSize(self):
        count = 0
        current = self.getHead()
        while current:
            count += 1
            current = current.link
        return count
    
    def getPos(self):
        #returns the current position as a number
        if self.isEmpty():
            return -1
        elif self.getHead() == self.getCurr():
            return 0
        temp = self.getHead()
        pos = 0
        while temp != self.getCurr():
            pos += 1
            temp = temp.link
        return pos
    
    def setPos(self, pos):
        self.goBeginning()
        for i in range(pos):
            self.goNext()
                
    def goNext(self):
        if self.getCurr() != None:
            self.setCurr(self.getCurr().link)
    
    def goPrev(self):
        here = self.getPos()
        self.setPos(here - 1)
        
    def getData(self):
        return self.getCurr().data
    
    def setData(self, d):
        self.getCurr().data = d
    
    def insert(self, n):
        #inserts a new node, n, after the curr.link node
        if self.isEmpty():
            self.setHead(n)
            self.setTail(n)
            self.setCurr(n)
        else:
            n.link = self.getCurr().link
            self.getCurr().link = n
            self.setCurr(n)
            if n.link == None:
                self.setTail(n)
            
    def append(self, n):
        #inserts at the end of the list
        self.goEnd()
        self.insert(n)
            
    def insertBefore(self, n):
        # inserts before curr
        if self.isEmpty():
            self.setHead(n)
            self.setTail(n)
            self.setCurr(n)
        else:
            if self.isBeginning() == True:
                n.link = self.getHead()
                self.setHead(n)
                self.setCurr(n)
            else:
                self.goPrev()
                self.insert(n)
        
    
    def remove(self):
        #removes the node at curr
        if self.isEmpty() == True:
            return
        if self.isBeginning() == True:
            self.setHead(self.getHead().link)
        else:
            self.goPrev()
            self.getCurr().link = self.getCurr().link.link
        
    
    def copy(self):
        #copies the list and returns a new list
        self.setCurr(self._head.link)
        temp = LinkedList()
        while self._curr.link != None:
            n = Node(self._curr.link.data)
            temp.append(n)
            self.setCurr(self._curr.link.link)
        return temp
    
    def __str__(self):
        self.setCurr(self._head.link)
        s = ""
        while self._curr.link != None:
            s += str(self._curr.link.data)
            s += "  "
            self.setCurr(self._curr.link.link)
        return s

    
