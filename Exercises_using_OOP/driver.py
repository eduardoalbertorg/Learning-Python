from _4_1_point_class import Point
import math


def main():
    p1 = Point(1, 2, 3)
    p2 = Point(2, 3, 4)
    print(p1 + p2)


def distance(p1, p2):
        '''
        Determine distance between two point Objects.

        Hint : Define the method distance, which determines distance between two points.
        Use formula distance = sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1 -z2)**2 ).
        '''
        return (math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2))


if __name__ == '__main__':
    main()