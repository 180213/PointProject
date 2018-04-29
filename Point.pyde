import random
from random import randint as r

colRed = "#e52d48"
colGreen = "#2de542"

class Point:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, Point):
        return sqrt((self.x - Point.x) ** 2 + (self.y - Point.y) ** 2)

    def move(self, Vector):
        self.x += Vector.horizontal
        self.y += Vector.vertical

    def makeVectorTo(self, Point):
        return Vector(Point.x - self.x, Point.y - self.y)

class Vector:
    
    horizontal = 0.0
    vertical = 0.0

    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    def add(self, vector):
        self.horizontal += vector.horizontal
        self.vertical += vector.vertical

    def subtract(self, vector):
        self.horizontal -= vector.horizontal
        self.vertical -= vector.vertical

    def multiply(self, number):
        self.horizontal *= number
        self.vertical *= number

    def divide(self, number):
        try:
            self.horizontal /= number
            self.vertical /= number
        except:
            pass

    def length(self):
        return sqrt((self.horizontal ** 2) + (self.vertical ** 2))

    def normalize(self):
        try:
            self.horizontal /= self.horizontal
            self.vertical /= self.vertical
        except:
            pass

class Circle:
    global reds
    global colRed, colGreen
    hexcode = ""
    def __init__(self, x, y, hexcode):
        self.position = Point(x, y)
        self.vel = Vector(random.uniform(-2, 2), random.uniform(-2, 2))
        self.hexcode = hexcode
    
    def move(self):
        global reds
        self.position.move(self.vel)
        if self.vel.length() >= 2:
            self.vel.normalize()
            self.vel.multiply(2)
        self.position.move(self.vel)

        if self.hexcode == "#e52d48":
            self.vel.horizontal = 0
            self.vel.vertical = 0
            self.position.move(self.vel)
        # for circle in circles:
        #     if self.position.distance(circle.position) >= 5:
        #         self.position.move(self.position.makeVectorTo(circle.position))
        
        if self.position.x < 7 or self.position.x > 793:
            self.vel.horizontal *= -1
        if self.position.y < 7 or self.position.y > 593:
            self.vel.vertical *= -1
        if self.position.y < 7 and self.position.x < 7:
            self.vel.multiply(-1)
        if self.position.y > 593 and self.position.x > 793:
            self.vel.multiply(-1)
        # for circle in circles:
        #     if self.hexcode == "#e52d48" and circle.hexcode == "#2de542":
        #         if self.position.distance(circle.position) <= 50:
        #             self.position.move(self.position.makeVectorTo(circle.position))
        #             if self.position.distance(circle.position) <= 7:
        #                 circle.hexcode = "#e52d48"
        for circle in circles:
            if self.hexcode == "#e52d48" and circle.hexcode == "#2de542":
                if self.position.distance(circle.position) <= 7:
                    circle.hexcode = "#e52d48"
                    reds += 1
        for circle in circles:
            pass
        # for circle in circles:
            
        # for circle in circles:
            # if self.hexcode == "e52d48" and circle.hexcode == "#2de542":
        #         if self.position.distance(circle.position) <= 50:
        #             self.position.makeVectorTo(circle.position)
        #             # if self.position.distance(circle.position) <= 7:
        #             circle.hexcode = "#e52d48"
        #             reds += 1
                
    
                
                
    def shape(self):
        ellipse(self.position.x, self.position.y, 7, 7)
        fill(self.hexcode)

            
reds = 1
circles = [Circle(r(7,793), r(7,593), "#e52d48")]


def setup():
    size(800, 600)
    for i in range(99):
        circles.append(Circle(r(7,793), r(7,593), "#2de542"))

def draw():
    background(255)
    for circle in circles:
        circle.move()
        circle.shape()
        
        
    
