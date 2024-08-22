# This is a simple program for a better understanding of OOPs concept and Here, we're defining a new "class" called "Car."
class Car:    # Constructor (Initialization) - __init__ method
    def __init__(self, make, model):
        # "self" refers to the car that's being created.
        # Encapsulation: Attributes (make and model) are encapsulated within the class.
        self.make = make
        self.model = model
    # Method - start_engine
    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is running!")

# Inheritance: Car is a class that can be used to create objects (instances).
# Abstraction: We create objects without worrying about the internal details of the Car class.
# Think of creating individual cars without needing to understand the intricacies of car manufacturing.
car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Mustang")
# Encapsulation: Accessing object attributes (make and model) using dot notation.
print(f"I have a {car1.make} {car1.model}.")
print(f"I also own a {car2.make} {car2.model}.")

# Method Call - start_engine
car1.start_engine()  
car2.start_engine()  