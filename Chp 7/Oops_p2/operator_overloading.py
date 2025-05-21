"""
What is Operator Overloading?

Operator overloading allows you to change the behavior of operators (+, -, *, etc.) for your own classes by defining special dunder methods.
"""
#Example: Overloading + with _add_
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Create two vector objects
v1 = Vector(1, 2)
v2 = Vector(3, 4)

# Use overloaded + operator
v3 = v1 + v2
print(v3)   # Output: Vector(4, 6)


"""
Other Common Operator Overloading Dunder Methods

Operator	Method	Example

+	_add_	a + b
-	_sub_	a - b
*	_mul_	a * b
/	_truediv_	a / b
==	_eq_	a == b
<	_lt_	a < b
>	_gt_	a > b

"""