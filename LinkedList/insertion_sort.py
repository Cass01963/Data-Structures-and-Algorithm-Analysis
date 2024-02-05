def insertionSort(arr):
    #go through every index
    for here in range (0,len(arr)):
        #hold the value form where we are
        cur = arr[here]
        #start 1 less than current position
        slider = here-1
        #slide everyone over until we find where cur belongs
        while slider >= 0 and cur < arr[slider]:
            arr[slider+1] = arr[slider]
            slider -= 1
        #put cur where it belongs
        arr[slider + 1] = cur
    #return the sorted array
    return arr

#main program
myArray = ["Cal Q. Later", "Willie Makit", "Warren Peace", "Helena Handbasket", "Justin Case"]
n = insertionSort(myArray)
print(n)