from dataclasses import dataclass
from typing import List

from fill import fill
from terrain import print_terrain


@dataclass
class FillTestCase:
    amount: int
    pour_position: int
    terrain: List[int]
    expected_water_terrain: List[int]


def main() -> None:
    test_cases: List[FillTestCase] = [
        FillTestCase(
            amount=2,
            pour_position=0,
            terrain=[5, 0, 1, 0, 5],
            expected_water_terrain=[5, 1, 1, 1, 5]
        ),
        FillTestCase(
            amount=2,
            pour_position=4,
            terrain=[5, 0, 1, 0, 5],
            expected_water_terrain=[5, 1, 1, 1, 5]
        ),
        FillTestCase(
            amount=2,
            pour_position=2,
            terrain=[5, 0, 1, 0, 5],
            expected_water_terrain=[5, 1, 1, 1, 5]
        ),
        FillTestCase(
            amount=6,
            pour_position=2,
            terrain=[5, 0, 1, 0, 5],
            expected_water_terrain=[5, 2, 3, 2, 5]
        ),
        FillTestCase(
            amount=6,
            pour_position=2,
            terrain=[0, 1, 2, 1, 0],
            expected_water_terrain=[0, 1, 2, 1, 0]
        ),
        FillTestCase(
            amount=6,
            pour_position=2,
            terrain=[0, 1, 0, 1, 0],
            expected_water_terrain=[0, 1, 1, 1, 0]
        ),
        FillTestCase(
            amount=4,
            pour_position=6,
            terrain=[5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            expected_water_terrain=[5, 4, 2, 1, 3, 2, 2, 2, 2, 2, 4, 3]
        ),
        FillTestCase(
            amount=15,
            pour_position=6,
            terrain=[5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            expected_water_terrain=[5, 4, 3, 3, 4, 4, 4, 3, 3, 3, 4, 3]
        ),
        FillTestCase(
            amount=50,
            pour_position=6,
            terrain=[5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            expected_water_terrain=[5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3]
        ),
        FillTestCase(
            amount=50,
            pour_position=6,
            terrain=[5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3][::-1],
            expected_water_terrain=[3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5]
        ),
    ]

    for case in test_cases:
        print("Initial Terrain:\n")
        print_terrain(case.terrain)

        water_terrain = fill(case.amount, case.pour_position, case.terrain)

        print(
            f"\nTerrain after pouring {case.amount} units of water at position "
            f"{case.pour_position}:\n"
        )
        print_terrain(case.terrain, water_terrain)

        print(f"\nTotal water captured: {sum(water_terrain) - sum(case.terrain)}")
        assert water_terrain == case.expected_water_terrain, (
            f"Test failed for {case}: result={water_terrain}"
        )

if __name__ == "__main__":
    main()
