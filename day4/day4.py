min, max = [int(line) for line in str("264793-803935").split('-')]

def validate(num : int, limitGroup : bool) -> bool :
    sizes, lastChar = [], '0'
    for char in str(num) :
        if int(lastChar) > int(char) : 
            return False
        if lastChar == char : 
            sizes[len(sizes) - 1] += 1
        else : 
            lastChar = char
            sizes.append(1)
    return any([size == 2 for size in sizes]) if limitGroup else any([size >= 2 for size in sizes])

def part1() -> int :
    return len([i for i in range(min, max) if validate(i, False)])

def part2() -> int :
    return len([i for i in range(min, max) if validate(i, True)])

print(f"Part 1 result is {part1()}")
print(f"Part 2 result is {part2()}")