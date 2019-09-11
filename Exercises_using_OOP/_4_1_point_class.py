import math


class Point(object):
    '''
    Define the class Point that represents x, y, and z coordinates of 3D coordinate system.

    Hint : Define the initializer method, __init__ that takes three values and assigns them to attributes x, y and z respectively.
    Now create an object p1 = Point(4, 2, 9) and print it using the statement print(p1). You may type python3.5 to use the latest version for the exercise
    '''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __add__(self, another_point):
        '''
        Improvise Point class definition such that,
        adding any two Point objects using + operator, results in a new Point object with corresponding x, y and z values being added.
        For e.g: Point(1, 2, 3) + Point(2, 3, 4) -> Point(3, 5, 7)
        Hint : Define __add__ method inside the class Point.
        '''
        return Point(self.x + another_point.x, self.y + another_point.y, self.z + another_point.z)



    def __str__(self):
        '''
        Improvise the class definition of Point such that any Point object is displayed in the format point : (x, y, z).
        '''
        return f'point : ({self.x}, {self.y}, {self.z})'