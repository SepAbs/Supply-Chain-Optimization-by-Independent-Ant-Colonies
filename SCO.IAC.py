from numpy import arange, ones, random
from pandas import read_csv #, ...

# Dataset & Parameters
df, numberAnts, numberIterations, Decay, Alpha, Beta = read_csv("Supply chain logisitcs problem.csv"), 5, 10, 0.8, 1, 1

# distanceMatrix = ...

def chooseNext(Current, Pheromone, distanceMatrix):
    Probabilities = Pheromone[Current] ** Alpha * (1. / distanceMatrix[Current]) ** Beta
    Probabilities /= Probabilities.sum()
    # Next
    return random.choice(arange(distanceMatrix.shape[0]), p = Probabilities)

def updatePheromone(Pheromone, Solutions, bestSolution):
    Pheromone *= Decay
    for Path, Length in Solutions:
        for i in range(len(Path) - 1):
            Pheromone[Path[i], Path[i + 1]] += 1. / Length
    bestPath, bestLength = bestSolution
    
    for i in range(len(best_path) - 1):
        Pheromone[bestPath[i], bestPath[i + 1]] += 1. / bestLength
    return Pheromone

def IAC(distanceMatrix):
    # Initialize pheromones
    Pheromone = ones(distanceMatrix.shape) / len(distanceMatrix)
    for Iteration in range(numberIterations):
        Solutions = []
        for i in range(numberAnts):
            Path = [random.randint(0, distanceMatrix.shape[0])]
            while len(Path) < distanceMatrix.shape[0]:
                Next = chooseNext(Path[-1], Pheromone, distanceMatrix)
                if Next not in Path:
                    Path.append(Next)
                else:
                    break
            # Calculate the path length
            Solutions.append((Path, sum(distanceMatrix[path[i], Path[i + 1]] for i in range(len(Path) - 1))))
        
        # Find the best solution of the iteration and update global pheromone update based on best solution.
        bestSolution = min(Solutions, key = lambda x: x[1])
        Pheromone = updatePheromone(Pheromone, Solutions, bestSolution)

# main()
# IAC(distanceMatrix)
