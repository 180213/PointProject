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
        return Vector(Point.x-self.x, Point.y-self.y)

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
    

class Test:
    def printing(self):
        point1 = Point(1,2)
        point2 = Point(1,5)
        print(point1.distance(point2))
        vec1 = point1.makeVectorTo(point2)
        print(vec1.horizontal, vec1.vertical)
        vec2 = Vector(4,5)
        print(vec2.horizontal, vec2.vertical)
        point2.move(vec2)
        print(point2.x, point2.y)
        
        
        vec3 = Vector(5,0)
        vec3.normalize()
        print(vec3.horizontal, vec3.vertical)
        vec4 = Vector(3,4)
        vec5 = Vector(1,2)
        
        print(vec4.length())
        vec4.subtract(vec5)
        print(vec4.horizontal, vec4.vertical)
        vec4.add(vec5)
        print(vec4.horizontal, vec4.vertical)
        
a = Test()
a.printing()
