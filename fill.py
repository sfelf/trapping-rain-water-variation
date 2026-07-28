from typing import List, Optional


def fill(amount: int, pour_position: int, terrain: List[int]) -> List[int]:
    if isinstance(amount, bool) or not isinstance(amount, int):
        raise TypeError("amount must be an integer")

    if amount < 0:
        raise ValueError("amount must be non-negative")

    if isinstance(pour_position, bool) or not isinstance(pour_position, int):
        raise TypeError("pour_position must be an integer")

    if not 0 <= pour_position < len(terrain):
        raise ValueError("pour_position must identify an element of terrain")

    water_terrain = terrain.copy()

    for _ in range(amount):
        min_position = find_minimum_height(water_terrain, pour_position)
        if min_position is None:
            break

        water_terrain[min_position] += 1

    return water_terrain


def find_minimum_height(terrain: List[int], position: int) -> Optional[int]:
    left_start = position - 1
    left_stop = 0
    left_step = -1

    right_start = position + 1
    right_stop = len(terrain) - 1
    right_step = 1

    # Assume the pour position is the minimum initially
    min_position = position

    # Search to the left for the minimum height
    min_position = search_for_minimum_position(terrain, min_position, left_start, left_stop, left_step)
    # Search to the right for the minimum height
    min_position = search_for_minimum_position(terrain, min_position, right_start, right_stop, right_step)

    if has_containing_walls(terrain, min_position):
        return min_position

    return None


def search_for_minimum_position(terrain: List[int], min_position: int, start: int, stop: int, step: int) -> int:
    for i in range(start, stop, step):
        if terrain[i] < terrain[min_position]:
            min_position = i
        elif terrain[i] > terrain[min_position]:
            break

    return min_position


def has_containing_walls(terrain: List[int], position: int) -> bool:
    position_height = terrain[position]

    has_left_wall = any(
        terrain[index] > position_height for index in range(position)
    )
    has_right_wall = any(
        terrain[index] > position_height
        for index in range(position + 1, len(terrain))
    )

    return has_left_wall and has_right_wall
