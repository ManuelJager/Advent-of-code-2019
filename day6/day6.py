import fileinput
import time

lines = list(map(str.strip, fileinput.input()))

def indexOf(list : list, value) -> int :
    return next((i for i, item in enumerate(list) if item == value), None)

def indexesOf(list : list, value) -> int :
    return [i for i, item in enumerate(list) if item == value]

def mapPlanets(input) -> None :
    parents, children = [], []
    for obj in input :
        parent, child = obj.split(')')
        parents.append(parent), children.append(child) 
    return parents, children

def getTotalOrbits() -> int :
    def recursiveGetOrbits(planet, depth) :
        total = sum([recursiveGetOrbits(child, depth + 1) for child in getChildren(planet)])
        return total + depth
    return recursiveGetOrbits("COM", 0)

def getParent(planet : str) -> int :
    return parents[indexOf(children, planet)]

def getChildren(planet : str) -> int :
    return [children[index] for index in indexesOf(parents, planet)]

def getNearbyPlanets(planet : str) -> list :
    nearbyPlanets = getChildren(planet)
    if planet != "COM" :
        nearbyPlanets.append(getParent(planet))
    return nearbyPlanets

def walkSystem() -> int :
    start, target = getParent("SAN"), getParent("YOU")
    visited, workers = [], {start : 0}
    while True :
        for worker in workers.copy().keys() :
            visited.append(worker)
            if worker == target :
                return workers[worker]
            for nearbyPlanet in getNearbyPlanets(worker) :
                if nearbyPlanet not in visited :
                    workers[nearbyPlanet] = workers[worker] + 1
            del workers[worker]
    return 0

def part1() -> int : 
    return getTotalOrbits()
    
def part2() -> int : 
    return walkSystem()
    
parents, children = mapPlanets(lines)

now = time.time()
print(f"Part 1 result is {part1()} and took {time.time() - now}")
now = time.time()
print(f"Part 2 result is {part2()} and took {time.time() - now}")