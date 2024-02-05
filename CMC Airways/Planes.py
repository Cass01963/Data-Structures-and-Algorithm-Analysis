from Passenger import Passenger
class Planes:
    def __init__(self, planeNum, destination="", DOT=-1, row=0, seat=0, HasMeal = False, NumOnPlane = 0, MaxSeats = 0):
        self._planeNum = int(planeNum)
        self._destination = destination
        self._DOT = int(DOT)
        self._row = int(row)
        self._seat = int(seat)
        self._HasMeal = bool(HasMeal)
        self._NumOnPlane = int(NumOnPlane)
        self._MaxSeats = int(MaxSeats)
        self._chairs = []
        for i in range(self._row):
            col = []
            for j in range(self._seat):
                col.append(Passenger())
            self._chairs.append(col)
        
    # setters and getters
    @property
    def NumOnPlane(self):
        return self._NumOnPlane
    
    @property
    def MaxSeats(self):
        return self._MaxSeats
    
    @property
    def chairs(self):
        return self._chairs
    
    @property
    def planeNum(self):
        return self._planeNum
    @planeNum.setter
    def planeNum(self, planeNum):
        self._planeNum = planeNum
    
    @property
    def destination(self):
        return self._destination
    @destination.setter
    def destination(self, destination):
        self._destination = destination
    
    @property
    def DOT(self):
        return self._DOT
    @DOT.setter
    def DOT(self, DOT):
        self._DOT = DOT
    
    @property
    def row(self):
        return self._row
    @row.setter
    def row(self, row):
        self._row = row
    
    @property
    def seat(self):
        return self._seat
    @seat.setter
    def seat(self, seat):
        self._seat = seat
        
    @property
    def HasMeal(self):
        return self._HasMeal
    @HasMeal.setter
    def HasMeal(self, HasMeal):
        self._HasMeal = HasMeal
    
    # method that shows the actual contents in the 'planes.txt' file
    def __str__(self):
        return ("{}, {}, {}, {}, {}".format(self.planeNum, self.destination, self.DOT, self.row, self.seat))
    
    # overloads the operators for sorting
    def __gt__(self, other):
        return (self._planeNum > other.planeNum)
    def __eq__(self, other):
        return (self._planeNum == other.planeNum)
    
    # method to count how many of each FoodPreference are on the plane
    def count_FoodPref(self):
        c = 0
        p = 0
        s = 0
        for r in range(len(self.chairs)):
            for c in range(len(self.chairs[r])):
                if self.chairs[r][c].FoodPref == "chicken":
                    c = c + 1
                elif self.chairs[r][c].FoodPref == "pasta":
                    p = p + 1
                elif self.chairs[r][c].FoodPref == "special":
                    s = s + 1
        return (c, p, s)
    
    # method to create an alphabetical list of who's on the plane and in which seat
    def alp_list(self): #works
        folks = []
        for r in range(len(self.chairs)):
            for c in range(len(self.chairs[r])):
                if self.chairs[r][c].name != "empty":
                    folks.append(self.chairs[r][c].name)
        folks.sort()
        return folks
    
    # method to find a passenger on a plane and return which seat
    def find_passenger(self, who): #works
        for r in range(len(self.chairs)):
            for c in range(len(self.chairs[r])):
                if self.chairs[r][c].name == who:
                    s = "Row: " + str(r+1) + " " + "Seat: " + str(c+1)
                    return s
        return "Passenger does not exist on this plane."
    
    # method to tell user how many people are on plane
    def count_people(self): #works
        count = 0
        for r in range(len(self.chairs)):
            for c in range(len(self.chairs[r])):
                if self.chairs[r][c].name != "empty":
                    count += 1
        return count
    
    # method to tell user if the plane is full
    def full(self): #works
        for r in range(len(self.chairs)):
            for c in range(len(self.chairs[r])):
                if self.chairs[r][c].name == "empty":
                    return False
        return True
    
    # method to tell user if a seat has already been booked
    def seat_booked(self, r, c):
        r = int(r)
        c = int(c)
        if self.chairs[r-1][c-1].name != "empty":
            return True
        return False
                    
    
    # method to tell user which seats are available (empty)
    def seat_available(self): #works
        seats = []
        for r in range(len(self.chairs)):
            for c in range(len(self.chairs[r])):
                if self.chairs[r][c].name == "empty":
                    seats.append("Seats: " + str(r+1) + " " + str(c+1))
        return seats
    
