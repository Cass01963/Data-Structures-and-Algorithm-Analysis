from LinkedList import LinkedList
from Node import Node

class Queue(LinkedList):
    def __init__(self):
        super().__init__()

    def Enqueue(self, x):
        super().append(x)

    def Dequeue(self):
        if super().isEmpty():
            return None
        else:
            super().goBeginning()
            y = super().getData()
            super().remove()
            return y

    def Peek(self):
        super().goBeginning()
        z = super().getData()
        return z


    