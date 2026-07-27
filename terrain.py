from typing import List, Optional


def print_terrain(terrain: List[int], water: Optional[List[int]] = None) -> None:
    water = water or terrain
    if not terrain or not water:
        print("Terrain is an empty list.")
        return
    if len(terrain) != len(water):
        print("Terrain and Water are not the same length.")
        return

    max_height = max(terrain + water)
    for height in range(max_height, -1, -1):
        row = ""
        for idx in range(len(terrain)):
            if terrain[idx] >= height:
                row += "+"
            elif water[idx] >= height:
                row += "w"
            else:
                row += " "
        print(row)
