from typing import List, Optional, Sequence


def print_terrain(terrain: Sequence[int], water: Optional[Sequence[int]] = None) -> None:
    if water is None:
        water = terrain

    _validate_terrain_and_water(terrain, water)

    max_height: int = max(max(terrain), max(water))
    terrain_rows: List[List[str]] = []

    for filled_height, terrain_height in zip(water, terrain):
        land_level = terrain_height + 1
        water_level = filled_height - terrain_height
        sky = max_height - filled_height
        terrain_rows.append(list(" " * sky + "w" * water_level + "+" * land_level))

    for row in zip(*terrain_rows):
        print("".join(row))


def _validate_terrain_and_water(terrain: Sequence[int], water: Sequence[int]) -> None:
    if not terrain:
        raise ValueError("Terrain cannot be empty.")
    if not water:
        raise ValueError("Filled terrain cannot be empty.")
    if len(terrain) != len(water):
        raise ValueError("Terrain and filled terrain must be the same length.")

    _validate_heights_are_integers(terrain, "Terrain")
    _validate_heights_are_integers(water, "Filled terrain")

    if any(height < 0 for height in terrain):
        raise ValueError("Terrain heights must be non-negative.")
    if any(height < 0 for height in water):
        raise ValueError("Filled terrain heights must be non-negative.")
    if any(
        filled_height < terrain_height
        for filled_height, terrain_height in zip(water, terrain)
    ):
        raise ValueError(
            "Filled terrain heights cannot be less than original terrain heights."
        )


def _validate_heights_are_integers(heights: Sequence[int], name: str) -> None:
    if any(isinstance(height, bool) or not isinstance(height, int) for height in heights):
        raise TypeError(f"{name} heights must be integers.")
