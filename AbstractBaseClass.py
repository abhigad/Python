from abc import ABC, abstractmethod

#abc is built in abstract base class and BBC is an instance of that and ABC is a helper class

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area()) # Output: 78.5
