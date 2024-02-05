# Main Program
# Christian Carranza
# Sources: For program 3, I worked with Morgan Rault and Annie Rome
# Sources: Office Hours with Dr. Lori included
# Sources: I had my friend Anthony debug the program to see what was wrong with the count
from Words import Words
from Node import Node
from LinkedList import LinkedList

file = open("Picasso.txt")
read_file = file.readlines()
wordList = LinkedList()
c = 0
uniquecount = 0
for line in read_file:
    for word in line.split():
        uniquecount += 1
        if wordList.isEmpty() == True: #works
            w = Words(word)
            n = Node(w)
            wordList.append(n)
        else:
            # see if word already there
            wordList.goBeginning()
            found = False
            
            # counts unique list of words
            while (wordList.isEnd() == False) and (found == False): #will this check the last node???
                if word == wordList.getData().word:
                    count = int(wordList.getData().count)
                    count += 1
                    new_data = Words(word)
                    new_data.count_set(count)
                    wordList.setData(new_data)
                    found = True
                    wordList.goNext()
                else:
                    wordList.goNext()
            if found == False:
                w = Words(word)
                n = Node(w)
                wordList.append(n)

wordList.goBeginning()
while wordList.isEnd() == False:
    print(wordList.getData().word, ":", wordList.getData().count)
    wordList.goNext()
indivwords = wordList.getSize()
creativity = float(indivwords / uniquecount)     
print("creativity analysis:", (("%.2f" % creativity)))


                
                    
                    
                    
                    

    
