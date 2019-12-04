import fileinput
import collections

intersections, paths = {}, []

for move in [str(line).split(',') for line in list(fileinput.input())] :
    board = {}
    pos, steps = (0,0), 0
    for instruction in move :
        move, distance = instruction[0], int(instruction[1:])
        for i in range(distance) :
            steps += 1
            posx, posy = pos
            posy += move == "U"
            posx += move == "R"
            posy -= move == "D"
            posx -= move == "L"
            pos = (posx, posy)
            board[pos] = (steps)
    paths.append(board)
intersectionKeys = [key for key in paths[0].keys() if key in paths[1].keys()]
for key in intersectionKeys :
    intersections[key] = paths[0][key] + paths[1][key]

def part1() -> int :
    return min([abs(posx) + abs(posy) for posx, posy in intersections.keys()])

def part2() -> int :
    return min(intersections.values())

print(f"Part 1 result is {part1()}")
print(f"Part 2 result is {part2()}")