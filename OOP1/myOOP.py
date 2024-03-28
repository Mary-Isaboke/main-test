class Vehicle:
    def __init__(self, make, model, year ):
        self.make = make
        self.model = model
        self.year =year

    def start(self):
        raise NotImplementedError("Subclass must implement this abstract method")  

    def stop(self):
        raise NotImplementedError("Subclass must implement this abstract method") 
class Car(Vehicle):
    def start(self):
        return f"The {self.year} {self.make} {self.model} starts"
    
    def stop(self):
        return f"The {self.year} {self.make} {self.model} stops"
    
class Motorcycle(Vehicle):
    def start(self):
        return f"The {self.year} {self.make} {self.model} starts"
    
    def stop(self):
        return f"The {self.year} {self.make} {self.model} stops"
    
# Creating instance of Car and Motocycle
my_car = Car("Toyota","Camry", 2019) 
my_motorcycle = Motorcycle("Honda", "CBR500R", 2019)  

# Using the start and stop methods without needing to know the internal implementation
print(my_car.start())
print(my_car.stop())
print(my_motorcycle.start())
print(my_motorcycle.stop())




        