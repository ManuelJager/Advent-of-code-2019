import fileinput

lines = list(fileinput.input())

def calcFuel(mass : int, recursive : bool) -> int :
    fuel = mass // 3 - 2
    return (fuel + calcFuel(fuel, recursive) if fuel > 0 else 0) if recursive else fuel

def part1() -> int :
    return sum([calcFuel(int(line), False) for line in lines])

def part2() -> int :
    return sum([calcFuel(int(line), True) for line in lines])

print(f"Part 1 result is {part1()}")
print(f"Part 2 result is {part2()}")