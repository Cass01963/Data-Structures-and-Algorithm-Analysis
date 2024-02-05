#tests the functionality of a linked list
### YOU MAY NOT CHANGE THIS FILE ###

# Output should be...
# 1. Is A empty? True
# 2. Position of A -1
# 3. Size of A = 0
# 4. Is A empty? False
# 5. Position of A 9
# 6. Size of A = 10
# 7. A = 0  1  2  3  4  5  6  7  8  9  
# 8. Size of B = 10
# 9. B = 9  8  7  6  5  4  3  2  1  0  
# 10. C = 0  1  2  3  42  5  6  7  8  9  
# 11. A = 10  11  12  13  14  15  16  17  18  19  
# 12. B = 81  64  49  36  25  16  9  4  1  0  
# 13. A = 11  12  13  14  15  16  17  18  19  
# 14. B = 81  64  49  36  25  16  9  4  1  
# 15. C = 0  1  2  42  5  6  7  8  9
# plus 2 fun lines

from Node import Node
from LinkedList import LinkedList

A = LinkedList()
print("1. Is A empty? {}".format(A.isEmpty()))
print("2. Position of A {}".format(A.getPos()))
print("3. Size of A = {}".format(A.getSize()))
for i in range(0, 10):
    n = Node(i)
    A.append(n)
print("4. Is A empty? {}".format(A.isEmpty()))
print("5. Position of A {}".format(A.getPos()))
print("6. Size of A = {}".format(A.getSize()))
print("7. A = " + str(A))
B = LinkedList()
for i in range(0, 10):
    n = Node(i)
    B.insertBefore(n)
print("8. Size of B = {}".format(B.getSize()))
print("9. B = " + str(B))
C = A.copy()
C.setPos(4)
C.setData(42)
print("10. C = " + str(C))
A.goBeginning()
while A.isEnd() == False:
    A.setData(A.getData() + 10)
    A.goNext()
A.setData(A.getData() + 10)
print("11. A = " + str(A))
B.goEnd()
while B.isBeginning() == False:
    B.setData(B.getData() ** 2)
    B.goPrev()
B.setData(B.getData() ** 2)
print("12. B = " + str(B))
A.goBeginning()
A.remove()
B.goEnd()
B.remove()
C.setPos(3)
C.remove()
print("13. A = " + str(A))
print("14. B = " + str(B))
print("15. C = " + str(C))
s = "Hardware is the part of a computer that can be kicked"
arr = s.split()
D = LinkedList()
for a in arr:
    n = Node(a)
    D.append(n)
print(D)
D.goBeginning()
D.setData("Software")
D.setPos(8)
D.setData("will")
D.goNext()
D.setData("kick")
D.goNext()
D.setData("us")
print(D)






