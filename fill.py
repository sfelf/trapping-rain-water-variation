def fill(amount, pour_position, terrain):
    if not terrain or pour_position < 0 or pour_position >= len(terrain):
        return terrain

    water_terrain = terrain.copy()
    
    for _ in range(amount):
        min_position = find_minimum_height(water_terrain, pour_position)
        if not min_position:
            break  
        
        water_terrain[min_position] += 1

    return water_terrain


def find_minimum_height(terrain, position):
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


def search_for_minimum_position(terrain, min_position, start, stop, step):
    for i in range(start, stop, step):
        if terrain[i] < terrain[min_position]:
            min_position = i
        elif terrain[i] > terrain[min_position]:
            break
    
    return min_position


def has_containing_walls(terrain, position):
    positions_to_left = terrain[position - 1::-1]
    positions_to_right = terrain[position + 1:]
    validator = lambda x: x > terrain[position]

    return any(map(validator, positions_to_left)) and any(map(validator, positions_to_right))
