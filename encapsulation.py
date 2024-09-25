# Encapsulation example in Python

class Base:
    def __init__(self):
        # Protected member
        self._a = 2

class Derived(Base):
    def __init__(self):
        # Call the constructor of the base class
        Base.__init__(self)
        print("Calling Protected member of base class:", self._a)
        
        # Modify the protected member
        self._a = 3
        print("Calling modified Protected member outside class:", self._a)

# Creating objects
obj1 = Derived()
obj2 = Base()

# Accessing the protected member of both objects
print("Accessing Protected member of obj1:", obj1._a)
print("Accessing Protected member of obj2:", obj2._a)
