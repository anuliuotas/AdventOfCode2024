from dataclasses import dataclass
from typing import Tuple, Dict
from enum import Enum

class CellType(Enum):
    EMPTY = '.'
    OBSTRUCTION = '#'

@dataclass
class Coordinate:
    x: int
    y: int

    def __hash__(self):
      return hash((self.x, self.y))

@dataclass
class Cell:
    coordinate: Coordinate
    type: CellType

@dataclass
class Map:
    width: int
    height: int
    cells: Dict[Coordinate, Cell]


def copy_map(map) -> Map:
    copied_cells = {}
    for coord, cell in map.cells.items():
        copied_cells[coord] = (
            Cell(
                coordinate=coord,
                type=cell.type
            )
        )

    return Map(
        width=map.width,
        height=map.height,
        cells=copied_cells
    )

class Direction(Enum):
    NORTH = '^'
    EAST = '>'
    SOUTH = 'v'
    WEST = '<'

    def turn_right(self):
        if self == Direction.NORTH:
            return Direction.EAST
        if self == Direction.EAST:
            return Direction.SOUTH
        if self == Direction.SOUTH:
            return Direction.WEST
        if self == Direction.WEST:
            return Direction.NORTH
    
    def get_move_offset(self):
        if self == Direction.NORTH:
            return [0, -1]
        if self == Direction.EAST:
            return [1, 0]
        if self == Direction.SOUTH:
            return [0, 1]
        if self == Direction.WEST:
            return [-1, 0]

@dataclass
class Player:
    location: Coordinate
    direction: Direction




directions = set(item.value for item in Direction)

player = None
cells = {}
width = 0
height = 0

with open('input.txt', 'r') as file:
    
    for line in file:
        l = line.replace('\n', '')
        
        for i, c in enumerate(l):
            
            if c in directions:
                cell_type = CellType.EMPTY
            else:
                cell_type = CellType(c)

            coord = Coordinate(i, height)
            cell = Cell(
                coordinate=coord,
                type=cell_type
            )
            cells[coord] = cell

            if c in directions:
                # player found
                player = Player(
                    location=coord,
                    direction=Direction(c)
                )
        
        width = len(l)
        height += 1

map = Map(
    width=width,
    height=height,
    cells=cells
)

def get_visited_cells(map):
    visited_coords = []
    visited_cells = []

    it = 0
    current_location = player.location
    current_dir = player.direction

    turns = set()

    max_it = 7000
    while True and it <= max_it:
        offset = current_dir.get_move_offset()
        next_location = Coordinate(current_location.x + offset[0], current_location.y + offset[1])

        if next_location not in map.cells:
            break
        next_cell = map.cells[next_location]
        if next_cell.type == CellType.EMPTY:
            visited_coords.append(next_location)
            visited_cells.append(next_cell)
            current_location = next_location
        elif next_cell.type == CellType.OBSTRUCTION:
            if (next_cell.coordinate, current_dir) in turns:
                return False, 0
            turns.add((next_cell.coordinate, current_dir))
            current_dir = current_dir.turn_right()
            offset = current_dir.get_move_offset()
            next_location = Coordinate(current_location.x + offset[0], current_location.y + offset[1])
            # optimistic that no two obstructions near each other
            next_cell = map.cells[next_location]
            if next_cell.type == CellType.OBSTRUCTION:
                if (next_cell.coordinate, current_dir) in turns:
                    return False, 0
                turns.add((next_cell.coordinate, current_dir))
                current_dir = current_dir.turn_right()
                offset = current_dir.get_move_offset()
                next_location = Coordinate(current_location.x + offset[0], current_location.y + offset[1])
                # optimistic that no two obstructions near each other
                next_cell = map.cells[next_location]
                if next_cell.type == CellType.OBSTRUCTION:
                    print('damm')

            visited_coords.append(next_location)
            visited_cells.append(next_cell)

        it += 1

    for c in visited_cells:
        if c.type == CellType.OBSTRUCTION:
            print('damm')
    return it < max_it, len(set(visited_coords)) + 1

print(get_visited_cells(map))

coords_to_test = []
for coord, cell in map.cells.items():
    if cell.type == CellType.EMPTY and coord != player.location:
        coords_to_test.append(cell.coordinate)

possible_locations = []
for idx, coord in enumerate(coords_to_test):
    test_map = copy_map(map)
    test_map.cells[coord] = Cell(coord, CellType.OBSTRUCTION)

    valid, visited_steps = get_visited_cells(test_map)
    if not valid:
        possible_locations.append(coord)
    print(f'Checked {idx + 1 } out of {len(coords_to_test)}')


print(f'Possible locations = {len(possible_locations)}')
print(possible_locations)