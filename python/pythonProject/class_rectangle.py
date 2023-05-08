class Rectangle(object):
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def printCount(cls):
        print(cls.count)

    def isSquare(rect_width, rect_height):
        return rect_width == rect_height

    def calcArea(self):
        return self.width * self.height

    def __add__(self, rect):
        return Rectangle(self.width + rect.width, self.height + rect.height)



