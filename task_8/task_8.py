from dataclasses import dataclass
from itertools import product

def generate_combinations(beacons):
    combinations = []
    for a in beacons:
        for b in beacons:
            if a != b:
                combinations.append((a, b))
    return combinations


def get_antinode_locations(comb):
    # b1 -> lower X
    if comb[0][0] < comb[1][0]:
        b1 = comb[0]
        b2 = comb[1]
    else:
        b1 = comb[1]
        b2 = comb[0]

    dx = b2[0] - b1[0]
    dy = b2[1] - b1[1]

    a1_x = b1[0] - dx
    a1_y = b1[1] - dy

    a2_x = b2[0] + dx
    a2_y = b2[1] + dy

    return (a1_x, a1_y), (a2_x, a2_y)


def get_antinode_locations_resonanse(comb, max_x, max_y):
    # b1 -> lower X
    if comb[0][0] < comb[1][0]:
        b1 = comb[0]
        b2 = comb[1]
    else:
        b1 = comb[1]
        b2 = comb[0]

    dx = b2[0] - b1[0]
    dy = b2[1] - b1[1]

    result = []

    # first direction
    i = 0
    while True:
        a_x = b1[0] - dx * i
        a_y = b1[1] - dy * i

        if a_x < 0 or a_x > max_x:
            break
        if a_y < 0 or a_y > max_y:
            break
        result.append((a_x, a_y))
        i += 1

    # second direction
    i = 0
    while True:
        a_x = b1[0] + dx * i
        a_y = b1[1] + dy * i

        if a_x < 0 or a_x > max_x:
            break
        if a_y < 0 or a_y > max_y:
            break
        result.append((a_x, a_y))
        i += 1

    return result


map = {}
beacons = {}

reading_rules_done = False
row = 0
with open('input.txt', 'r') as file:
    for line in file:
        l = line.replace('\n', '')

        for i, cell in enumerate(l):
            coord = (i, row)
            map[coord] = cell

            if cell != '.':
                if cell not in beacons:
                    beacons[cell] = []
                beacons[cell].append(coord)
        row += 1
        width = len(line)
height = row - 1

# part 1
locations = set()
for indicator, b in beacons.items():
    combinations = generate_combinations(b)
    for comb in combinations:
        a1, a2 = get_antinode_locations(comb)
        if a1 in map:
            locations.add(a1)
        if a2 in map:
            locations.add(a2)
print(f'Part 1 antinodes: {len(locations)}')

# part 2
locations = set()
for indicator, b in beacons.items():
    combinations = generate_combinations(b)
    for comb in combinations:
        antinodes = get_antinode_locations_resonanse(comb, width, height)
        for a in antinodes:
            if a in map:
                locations.add(a)
print(f'Part 1 antinodes: {len(locations)}')
