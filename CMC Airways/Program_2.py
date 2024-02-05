### Christian Carranza
### Program 2
## Sources: I worked on this program with these classmates: Morgan, Annie, Kaela (I also went to office hours with Dr. Lori)
## Additional Sources: https://www.geeksforgeeks.org/python-program-for-binary-search/, https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
from Passenger import Passenger
from Planes import Planes

##########
## MAIN ##
##########

# locates the planes using a binary search
def binary_search(arr, low, high, x):
        if high >= low:
            mid = (high+low)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binary_search(arr, low, mid-1, x)
            else:
                return binary_search(arr, mid+1, high, x)
        else:
            return -1
     
     
# subroutine that makes the 'planes.txt' file readable
def file_read(file_name):
    content_array = []
    with open(file_name) as f:
        # removes the header in the 'planes.txt'
        rows = f.readlines()[1:]
        for line in rows:
            line = line.rstrip('\n')
            p = line.split(', ')
            ID = p[0]
            Destination = p[1]
            Day = p[2]
            r = p[4]
            s = p[5]
            content_array.append(Planes(ID, Destination, Day, r, s))
            
    return content_array


# subroutine that makes the 'chairs.csv' file readable
def csv_read(csv_name):
    with open(csv_name) as csv:
        csvreader = csv.readlines()[1:]
        for rows in csvreader:
            p = rows.split(",")
            planeID = p[0]
            name = p[1]
            meal = p[2]
            r = int(p[3])
            s = int(p[4])
            
            #create passenger object
            ps = Passenger(name,meal)
            p1 = Planes(planeID)
            here = allplanes.index(p1)
            allplanes[here].chairs[r-1][s-1] = ps
            

# Display Menu
allplanes = file_read('planes.txt')
csv_read('bookings.csv')


"""plane = allplanes[1]
c, p, s = plane.count_FoodPref()
print("chicken: {}\npasta: {}\nspecial: {}".format(c, p, s))
if plane.HasMeal:
    print("chicken: {}\npasta: {}\nspecial: {}".format(c, p, s))
else:
    print("snacks: {}".format(c+p+s))"""


print("Welcome to Christian's Airport!\nPlease type the following:")
done = False
while done == False:
    text = input("Type in 1 to see a full list of the planes departing.\nType in 2 to find the specific plane you've chosen.\nType in 3 to add passengers.\nType in 4 to see how many people are on a plane and the list of passengers on that plane.\nType in 5 for food count.\nType in 6 to find a passenger.\nType any key to exit.\n")

    # list of planes
    if text == "1":
        allplanes.sort()
        for p in allplanes:
            print(p)    
        # tells user if plan is full or not
        full = allplanes[int(input("Type in plane numbers 0-27 to see if the plane you're looking for is full: "))].full()
        if full != False:
            print("This plane is full!")
        else:
            print("There are seats still available!")
        # tells user what seats are available
        seats_avail = allplanes[int(input("Type in plane numbers 0-27 to see what seats are available: "))].seat_available()
        if seats_avail != "empty":
            print("('Rows | Seats')")
            print(seats_avail)
        else:
            print("No seats available")
        
    
    # find planes
    elif text == "2":
        x = (input("What plane are you looking for today? "))
        findIt = Planes(x)
        result = binary_search(allplanes, 0, len(allplanes)-1, findIt)
        
        if result != -1:
            i = allplanes[result]
            print("Plane number found:", str(i))
        else:
            print("Plane number does not exist.")
            
    # add passenger
    elif text == "3":
        plane = allplanes.index(Planes(input("Type in plane number: ")))
        if (allplanes[plane].seat_booked(input("Type in Row: "), input("Type in Seat: "))) == False:
            print("This seat is available.")
        else:
            print("This seat is taken.")
    
    # list passengers
    elif text == "4":
        print("There are", allplanes[int(input("Type in plane numbers 0-27 to see the number of people on a certain plane: "))].count_people(), "people on this plane.")
        folks = allplanes[int(input("To see the full list of people on that plane, again please type in the plane numbers 0-27: "))].alp_list()
        for line in folks:
            print(line)
        
    # food count
    elif text == "5":
        plane = allplanes[int(input("Type in plane numbers 0-27 to see how many people ordered each food preference: "))]
        c, p, s = plane.count_FoodPref()
        print("Chicken: {}\nPasta: {}\nSpecial: {}".format(c, p, s))
        # snack count
        print("snacks: {}".format(c+p+s))
        
        # I could not figure this one out
        """if plane.HasMeal:
            print("chicken: {}\npasta: {}\nspecial: {}".format(c,p,s))
        else:
            print("snacks: {}".format(c+p+s))"""
        
    
    # find passenger
    elif text == "6":
        here = allplanes.index(Planes(input("Please type in your plane number: ")))
        print(allplanes[here].find_passenger(input("Now, type in the name: ")))
        
    # end program
    else:
        print("BYE, BYE!")
        done = True






