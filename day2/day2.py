import fileinput

lines = [int(line) for line in list(fileinput.input())[0].split(',')]

def solve(noun, verb) -> int :
    t = lines.copy()
    t[1], t[2] = noun, verb
    for i in range(0, len(t), 4) :
        if t[i] == 1 :
            t[lines[i+3]] = t[t[i+1]] + t[t[i+2]]
        elif lines[i] == 2 :
            t[lines[i+3]] = t[t[i+1]] * t[t[i+2]]
        else :
            break
    return t[0]

def part1() -> str :
    return solve(12,2)

def part2() -> str : 
    for noun in range(100) :
        for verb in range(100) :
            if solve(noun, verb) == 19690720 :
                return f"{noun}{verb}"

print(f"Part 1 result is {part1()}")
print(f"Part 2 result is {part2()}")