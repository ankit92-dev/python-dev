# Why Complex?
# Because it is Superpower, it helps to customize and have different and unique values to each object

# Base class for all Mercedes cars
class Mercedes:
    def __init__(self, model, color, horsepower, price):
        self.model = model
        self.color = color
        self.horsepower = horsepower
        self.price = price

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Horsepower: {self.horsepower} HP")
        print(f"Price: ${self.price}")

# Subclass for Mercedes Sedan models
class Sedan(Mercedes):
    def __init__(self, model, color, horsepower, price, luxury_package):
        super().__init__(model, color, horsepower, price)  # Corrected the super() call
        self.luxury_package = luxury_package

    def display_info(self):
        super().display_info()
        print(f"Luxury Package: {'Yes' if self.luxury_package else 'No'}")

# Subclass for Mercedes SUV models
class SUV(Mercedes):
    def __init__(self, model, color, horsepower, price, offroad_capability):
        super().__init__(model, color, horsepower, price)  # Corrected the super() call
        self.offroad_capability = offroad_capability

    def display_info(self):
        super().display_info()
        print(f"Offroad Capability: {'High' if self.offroad_capability else 'Standard'}")

# Subclass for Mercedes AMG performance models
class AMG(Mercedes):
    def __init__(self, model, color, horsepower, price, acceleration):
        super().__init__(model, color, horsepower, price)  # This was already correct
        self.acceleration = acceleration  # 0-100 km/h in seconds

    def display_info(self):
        super().display_info()
        print(f"0-100 km/h Acceleration: {self.acceleration} seconds")


# Example usage
e_class = Sedan("E-Class", "Black", 255, 55000, luxury_package=True)
g_class = SUV("G-Class", "White", 416, 135000, offroad_capability=True)
amg_gt = AMG("AMG GT", "Red", 523, 165000, acceleration=3.7)

print("Sedan Example:")
e_class.display_info()
print("\nSUV Example:")
g_class.display_info()
print("\nAMG Example:")
amg_gt.display_info()