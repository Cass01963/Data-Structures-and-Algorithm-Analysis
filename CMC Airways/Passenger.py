class Passenger:
    def __init__(self, name="empty", FoodPref="none"):
        self._name = name
        self._FoodPref = FoodPref
        
    # setters and getters
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def FoodPref(self):
        return self._FoodPref
    @FoodPref.setter
    def FoodPref(self, FoodPref):
        self._FoodPref = FoodPref