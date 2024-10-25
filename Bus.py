class Vehicle:
    
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
        
    def fare(self):
        return self.capacity * 100
    
    
class Bus(Vehicle):
    
    def fare(self):
        amount = super().fare()
        amount = amount + ((amount * 10) /100)
        return amount
    
SchoolBus = Bus("School Volvo", 180,12,50)

print(f"Vehicle Name: {SchoolBus.name}\n Speed: {SchoolBus.max_speed}\n Mileage: {SchoolBus.mileage}")

print (f"Bus Fare: {SchoolBus.fare()}")