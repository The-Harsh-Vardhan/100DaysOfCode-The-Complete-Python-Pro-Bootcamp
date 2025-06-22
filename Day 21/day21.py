#Class Inheritance in Python

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()  #Calls all the method and attributes from parent class.

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("Moving in Water!")

nemo = Fish()
nemo.swim()