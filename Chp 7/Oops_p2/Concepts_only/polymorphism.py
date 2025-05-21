# 4. Polymorphism
# Same method name behaves differently based on the object.

#Example:
class Bird:
    def sound(self):
        print("Some bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp")

class Parrot(Bird):
    def sound(self):
        print("Squawk")

# Polymorphism in action
for bird in [Sparrow(), Parrot()]:
    bird.sound()

"""
Key Points:
sound() behaves differently based on the object type.
"""