# 2. Multiple Inheritance

# In multiple inheritance, a class can inherit from more than one parent class.

# First base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Driving...")

# Second base class
class MusicSystem:
    def play_music(self):
        print("Playing music...")

# Derived from both Vehicle and MusicSystem
class LuxuryCar(Vehicle, MusicSystem):
    def honk(self):
        print("Luxury beep!")

lc = LuxuryCar("BMW")
lc.drive()        # From Vehicle
lc.play_music()   # From MusicSystem
lc.honk()         # Own method
print(lc.brand)   # From Vehicle