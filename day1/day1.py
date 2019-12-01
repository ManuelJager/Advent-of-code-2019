import fileinput

#init
lines = list(fileinput.input())

def part1() :
    def calcFuel(mass : int) :
        return mass // 3 - 2
    return sum([calcFuel(int(line)) for line in lines])

def part2() :
    def recursiveCalcFuel(mass : int) :
        fuel = mass // 3 - 2
        return fuel + recursiveCalcFuel(fuel) if fuel > 0 else 0
    return sum([recursiveCalcFuel(int(line)) for line in lines])

print(f"Part 1 result is {part1()}")
print(f"Part 2 result is {part2()}")