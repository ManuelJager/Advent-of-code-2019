import fileinput
from collections import Counter

puzzle_input = fileinput.input().readline()


def split_string_into_chunks(input_string: str, chunk_size: int) -> list:
    return [input_string[i:i+chunk_size] for i in range(0, len(input_string), chunk_size)]


def plot_layer(layer_string: str, height: int, width: int) -> list:
    return [[layer_string[(row_index * width) + column_index]
             for column_index in range(width)]
            for row_index in range(height)]


def map_layers(input_string: str, height: int, width: int) -> list:
    return [(layer_string, dict(Counter(layer_string)), plot_layer(layer_string, height, width))
            for layer_string in split_string_into_chunks(input_string, height * width)]


def part1() -> int:
    global layers
    min_amount_0 = min(layer_counter['0'] for layer_string, layer_counter, layer_plot in layers)

    selected_layer_string, selected_layer_counter, selected_layer_plot = \
        [(layer_string, layer_counter, layer_plot) for layer_string, layer_counter, layer_plot in layers
         if layer_counter['0'] == min_amount_0][0]

    return selected_layer_counter['1'] * selected_layer_counter['2']


def part2(height: int, width: int) -> int:
    global layers
    msg_plot = plot_layer("2" * (height * width), height, width)
    for row_index in range(height):
        for column_index in range(width):
            for layer_index in range(len(layers)):
                selected_layer_string, selected_layer_counter, selected_layer_plot = layers[layer_index]
                point = selected_layer_plot[row_index][column_index]
                if point != '2':
                    msg_plot[row_index][column_index] = point
                    break
    return "\n".join(["".join(row) for row in msg_plot]).replace("0", "  ").replace("1", "##")


IMG_HEIGHT = 6
IMG_WIDTH = 25
layers = map_layers(puzzle_input, IMG_HEIGHT, IMG_WIDTH)
print(f"Part 1 result is {part1()}")
print(f"Part 2 result is \n{part2(IMG_HEIGHT, IMG_WIDTH)}")