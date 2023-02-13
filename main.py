# 1)Animal Inheritance: Create a base class "Animal" with an attribute "name" and a method "speak".
#  Create two subclasses "Dog" and "Cat" that inherit from "Animal"
#  and implement the "speak" method to make a sound specific to each animal.


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says woof!")
#
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} says meow!")
#
# dog = Dog("Max")
# dog.speak()
# cat = Cat("Tom")
# cat.speak()



# 2)Vehicle Inheritance: Create a base class "Vehicle" with an attribute "num_of_wheels"
# and a method "drive". Create two subclasses "Car" and "Bicycle" that inherit from "Vehicle"
#  and implement the "drive" method in a way that makes sense for each vehicle.



# class Vehicle:
#     def __init__(self, num_of_wheels):
#         self.num_of_wheels = num_of_wheels
#
#     def drive(self):
#         pass
#
# class Car(Vehicle):
#     def drive(self):
#         print(f"Driving on roads with {self.num_of_wheels} wheels:")
#
#
# class Bicycle(Vehicle):
#     def drive(self):
#         print(f"Pedaling on a bicycle with {self.num_of_wheels} wheels:")
#
# car = Car(4)
# car.drive()
#
# bicycle = Bicycle(2)
# bicycle.drive()



# 3)Shape Inheritance: Create a base class "Shape" with an attribute "num_of_sides" and a method "area".
# Create two subclasses "Triangle" and "Rectangle" that inherit from "Shape"
# and calculate the area of the shape using the values provided.


# class Shape:
#     def __init__(self, num_of_sides):
#         self.num_of_sides = num_of_sides
#
#     def area(self):
#         pass
#
# class Triangle(Shape):
#     def __init__(self, num_of_sides, side1, height):
#         super().__init__(num_of_sides)
#         self.side1 = side1
#         self.height =height
#
#     def area(self):
#         return 1 / 2 * self.height * self.side1
#
#
# class Rectangle(Shape):
#     def __init__(self, num_of_sides, side1, side2):
#         super().__init__(num_of_sides)
#         self.side1 = side1
#         self.side2 = side2
#
#     def area(self):
#         return self.side1 * self.side2
#
#
# triangle = Triangle(3, 20, 15)
# print(f"The Triangle has a {triangle.num_of_sides} sides and its area is {triangle.area()} ")
#
# rectangle = Rectangle(4, 10, 8)
# print(f"The Rectangle has a {rectangle.num_of_sides} sides and its area is {rectangle.area()}")