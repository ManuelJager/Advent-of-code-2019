import fileinput
from copy import deepcopy
import math

asteroid_map = [[char for char in line] for line in list(map(str.strip, fileinput.input()))]


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return f"(x: {self.x}, y: {self.y})"

    def __repr__(self):
        return str(self)

    def simplify(self):
        if self.x == 0 and self.y == 0:
            return self
        gcd_val = math.gcd(self.x, self.y)
        return Vector(self.x // gcd_val, self.y // gcd_val)


def map_contains_asteroid(arg_map: list):
    return len(list(enumerate_map(arg_map))) > 1


def enumerate_map(arg_map: list) -> tuple:
    for line_index in range(len(arg_map)):
        for char_index in range(len(arg_map[line_index])):
            data = arg_map[line_index][char_index]
            if data == "#":
                yield Vector(char_index, line_index)


def is_in_bounds(vector: Vector) -> bool:
    return (len(asteroid_map) > vector.y >= 0) and (len(asteroid_map[vector.y]) > vector.x >= 0)


def get_deg(vector: Vector) -> float:
    theta = math.atan2(vector.y, vector.x)
    deg = (math.degrees(theta) + 270) % 360
    return deg


def cast_shadow(shadow_map: list, base: Vector, to: Vector) -> list:
    diff_vector = to - base
    shadow_step = diff_vector.simplify()
    current = to + shadow_step
    while is_in_bounds(current):
        shadow_map[current.y][current.x] = 'X'
        current = current + shadow_step
    return shadow_map


def create_shadow_map(pos: Vector, shadow_map=None) -> list:
    if shadow_map is None:
        shadow_map = deepcopy(asteroid_map)
    else:
        shadow_map = deepcopy(shadow_map)
    for vector in enumerate_map(shadow_map):
        if vector == pos:
            shadow_map[vector.y][vector.x] = 'O'
            continue
        shadow_map = cast_shadow(shadow_map, pos, vector)
    return shadow_map


def get_asteroid_ranking(pos: Vector) -> int:
    shadow_map = create_shadow_map(pos)
    return sum([line.count('#') for line in shadow_map])


def print_map(any_map: list):
    [print(" ".join(line).replace(".", " ")) for line in any_map]


def get_asteroid_with_best_los():
    asteroid_rankings = {}
    for vector in enumerate_map(asteroid_map):
        asteroid_rankings[vector] = get_asteroid_ranking(vector)
    return max(asteroid_rankings, key=asteroid_rankings.get)


def part1(do_print_map: bool = False):
    if do_print_map:
        print_map(create_shadow_map(asteroid))
    return asteroid, get_asteroid_ranking(asteroid)


def part2():
    part_2_asteroid_map = deepcopy(asteroid_map)
    deleted_asteroids = {}
    index = 0
    while map_contains_asteroid(part_2_asteroid_map):
        visible_asteroids = {}
        shadow_map = create_shadow_map(asteroid, part_2_asteroid_map)
        for vector in enumerate_map(shadow_map):
            visible_asteroids[get_deg(asteroid - vector)] = vector

        for key in sorted(visible_asteroids.keys()):
            vector = visible_asteroids[key]
            part_2_asteroid_map[vector.y][vector.x] = "."
            deleted_asteroids[index] = vector
            index += 1

    selected_vector: Vector = deleted_asteroids[199]
    return selected_vector.x * 100 + selected_vector.y


asteroid = get_asteroid_with_best_los()
print(f"Part 1 result is {part1()}")
print(f"Part 2 result is {part2()}")
