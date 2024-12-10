

def get_directions(coords):
    return [
        (coords[0] + 1, coords[1]),
        (coords[0] - 1, coords[1]),
        (coords[0], coords[1] + 1),
        (coords[0], coords[1] - 1)
    ]


def move_along(visited, current_pos, map):
    current_coord = current_pos[0]
    current_height = current_pos[1]

    if current_height == 9:
        visited.append(1)
        return

    for dir in get_directions(current_coord):
        if dir in map:
            h = map[dir]
            if h == current_height + 1:
                move_along(visited, (dir, h), map)


map = {}
starts = []
with open('input.txt', 'r') as file:
    y = 0
    for line in file:
        l = line.replace('\n', '')
        number_idx = 0
        for i, number in enumerate(l):
            nr = int(number) if number != '.' else -1
            map[(i, y)] = nr
            if nr == 0:
                starts.append((i, y))
        y += 1


total_score = 0
for path_start in starts:
    possible_paths = []
    move_along(possible_paths, (path_start, 0), map)

    print(possible_paths)
    path_score = sum(possible_paths)

    print(f'Path {path_start} score = {path_score}')
    total_score += path_score

print(f'Total score = {total_score}')
