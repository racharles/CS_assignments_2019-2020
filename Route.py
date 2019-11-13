from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import random, os

class Point():
    '''Defines a Point on a 2-d coordinate plane.
    Attributes: x, y values
    Methods:    distance_to_Point (dist to another Point)'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to_Point(self, Point2):
        '''Returns the distance bw 2 Points.
        '''
        x1, y1 = self.x, self.y
        x2, y2 = Point2.x, Point2.y
        dist = sqrt((y2-y1)**2+(x2-x1)**2)
        return dist

    def __str__(self):
        '''Prints a Point object as (x,y).
        '''
        return '('+str(self.x) + ', '+str(self.y)+')'

class Route():
    '''Defines an ordered route over a series of Points.
    Attributes: a list of Point objects, a total distance
    Methods:    total_distance, display_route on a map, 
                mate with another route
    '''
    def __init__(self, PointsList):
        '''Initialize route object using given list of Point objects.
        Attributes: PointList (of Point objects)
                    distance (total distance traveled when following route)
        '''
        self.PointsList = PointsList
        self.distance = self.total_distance()

    def total_distance(self):
        '''Return total route distance for a route beginning
        and ending at the same initial Point.
        '''
        
        # start a running total for totalDist
        totalDist = 0

        # iterate over each Point, continually adding to totalDist
        p1 = self.PointsList[0]
        for p2 in self.PointsList:
            totalDist += p1.dist_to_Point(p2)
            p1 = p2
    
        # close the loop
        totalDist += self.PointsList[-1].dist_to_Point(self.PointsList[0])
        
        return totalDist

    def mate(self, route2):
        '''Combines information from two parent routes into a child route
        
        Input: self (Route), route2 (Route)
        Returns: child (Route)
        '''
        # convert from Route to PointsList
        parent1 = self.PointsList
        parent2 = route2.PointsList

        # choose a random selection of Points from parent1 using two breakPoints
        b1 = parent1.index(random.choice(parent1))
        b2 = parent1.index(random.choice(parent1))
        print(b1)
        print(type(b1))
        print(b2)

        child1 = parent1[b1:b2]

        # make a copy, or else child2 will Point to parent2
        child2 = parent2.copy()
        # remove selected Points from child2
        for i in child1:
            child2.remove(i)

        child = child1 + child2

        return Route(child)


    def display_route(self,name='route'):
        '''Draw the path for a Route. Saves the graph to
        a Graphs folder with the name passed in.
        '''
        xVals = [p.x for p in self.PointsList]+[self.PointsList[0].x]
        yVals = [p.y for p in self.PointsList]+[self.PointsList[0].y]
        plt.plot(xVals,yVals, marker='o', linestyle='--', color='r')
        if not os.path.exists('Graphs/'):
            os.mkdir('Graphs/')
        plt.savefig('Graphs/'+name+'.png')
        plt.close()

    def __str__(self):
        '''Represent a Route object as a list of nicely
        printed Points. ie (x1,y1), (x2, y2), ...
        '''
        stringL = ', '.join([str(p) for p in self.PointsList])
        return stringL

p1 = Point(2,3)
p2 = Point(4.2,1.9)
p3 = Point(1,7)
p4 = Point(3,4)
p5 = Point(5,6)

r1 = Route([p1,p2,p3,p4,p5])

p5 = Point(2,3)
p4 = Point(4.2,1.9)
p2 = Point(1,7)
p3 = Point(3,4)
p1 = Point(5,6)

r2 = Route([p1,p2,p3,p4,p5])

child = r1.mate(r2)
print(type(child))
print(child)
