class Vehicle:
    def __init__(self, number, owner):
        self.number = number
        self.owner = owner

    def show(self):
        print("Vehicle Number:", self.number)
        print("Owner Name:", self.owner)


class Bike(Vehicle):
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass


vehicle_type = input("Enter Vehicle Type (Bike/Car/Truck): ")
number = input("Enter Vehicle Number: ")
owner = input("Enter Owner Name: ")

if vehicle_type.lower() == "bike":
    vehicle = Bike(number, owner)

elif vehicle_type.lower() == "car":
    vehicle = Car(number, owner)

elif vehicle_type.lower() == "truck":
    vehicle = Truck(number, owner)

else:
    print("Invalid Vehicle Type")
    exit()

print("\nVehicle Details")
vehicle.show()