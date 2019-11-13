# Rachel Bai
# runSim.py
# 11/11/19

from Route import *
import matplotlib.pyplot as plt
import random, os
import numpy as np

## PROVIDED FUNCTIONS ##
# Do not edit these, just make calls to them
def sortPoplnDist(popln):
    '''
    Arguments: popln - a list of Route objects
    Returns:   the list sorted by increasing total_distance.
    '''
    # measure distance for each member of the population
    poplnDistL = [[r.distance,r] for r in popln]

    # sort population
    poplnDistL.sort(key=lambda x: x[0])
    popln = [individual[1] for individual in poplnDistL]

    return popln

def averageFitness(popln):
    '''
    Arguments: popln - a list of Route objects
    Returns:   average total_distance for the population
    '''
    
    # measure distance for each member of the population
    poplnDistL = [[r.distance,r] for r in popln]

    # calculate the average total distance for whole population
    fitness = np.mean([element[0] for element in poplnDistL])

    return fitness


def graph_avgfitness_evolution(fitnessScoresL, name='fitnessByGen'):
    '''
    Arguments: fitnessScoresL - a list of average total distances for each generation
               name - (optional) the desired name for the graph
    Returns:   None. Creates a graph saved in a Graphs folder
    '''
    plt.plot(fitnessScoresL, marker='o', linestyle='--', color='k')
    
    if not os.path.exists('Graphs/'):
            os.mkdir('Graphs/')
    plt.savefig('Graphs/',name,'.png')



## YOUR CODE GOES BELOW ##

def matePopln(popln, numSurvivors, popSize):
    ''' This is a helper function for runSim.
    '''
    # sort individuals by fitness, only take survivors
    ## Hint: call sortPoplnDist function
    

    # mate survivors randomly to make new population
    ## Hint: you might use a for or while loop...
    
    
    # return the new population
    return popln

def runSim(numGens=50, numPoints=15, popSize=100, survivalRate=0.2):
    '''Creates a random list of points and simulates evolution on the
    problem of finding the shortest route to visit those points. Creates
    graphs of the evolution process.
    Arguments: optional - numGens (int), numPoints (int), popSize (int)
                          survivalRate (float, between 0-1)
    '''
    # create a list of random points for the band's world tour
    pointsL = [Point(int(random.random()*100),int(random.random()*100)) for i in range(0,numPoints)]

    # create the initial population of random routes
    ## (a population is represented as a list of Route objects)
    popln = [Route(random.sample(pointsL,numPoints)) for i in range(0,popSize)]
    
    # create a variable to keep track of average fitness for each generation
    

    # run simulation numGens times

        # get new population by mating old population
       

        # keep track of average fitness for each new gen


        # graph the best route in the new generation


    # create graph of average fitness over the generations

    pass

# Run the simulation in script mode
if __name__ == '__main__':
    runSim()