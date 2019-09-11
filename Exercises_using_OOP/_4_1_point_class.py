'''
Define the class Point that represents x, y, and z coordinates of 3D coordinate system.

Hint : Define the initializer method, __init__ that takes three values and assigns them to attributes x, y and z respectively.
Now create an object p1 = Point(4, 2, 9) and print it using the statement print(p1). You may type python3.5 to use the latest version for the exercise
'''

class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __str__(self):
        '''
        Improvise the class definition of Point such that any Point object is displayed in the format point : (x, y, z).
        '''
        return f'point : ({self.x}, {self.y}, {self.z})'