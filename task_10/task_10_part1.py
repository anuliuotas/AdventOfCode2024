

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

    visited[current_coord] = current_height

    for dir in get_directions(current_coord):

        if dir in map:
            h = map[dir]
            if h == current_height + 1 and dir not in visited:
                move_along(visited, (dir, h), map)


map = {}
starts = []
with open('ex.txt', 'r') as file:
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
    possible_paths = {}
    move_along(possible_paths, (path_start, 0), map)

    path_score = 0
    for h in possible_paths.values():
        if h == 9:
            path_score += 1

    print(f'Path {path_start} score = {path_score}')
    total_score += path_score

print(f'Total score = {total_score}')
