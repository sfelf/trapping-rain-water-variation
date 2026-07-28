from contextlib import redirect_stdout
from dataclasses import dataclass
from io import StringIO
from typing import Any, List, Optional, Sequence, Type

from fill import fill
from terrain import print_terrain


@dataclass
class FillTestCase:
    amount: int
    pour_position: int
    terrain: List[int]
    expected_water_terrain: List[int]


@dataclass
class InvalidFillTestCase:
    amount: Any
    pour_position: Any
    terrain: List[int]
    expected_exception: Type[Exception]


@dataclass
class TerrainTestCase:
    terrain: Sequence[int]
    water: Optional[Sequence[int]]
    expected_output: str


@dataclass
class InvalidTerrainTestCase:
    terrain: Sequence[Any]
    water: Optional[Sequence[Any]]
    expected_exception: Type[Exception]


def _run_fill_valid_test_cases() -> None:
    valid_cases: List[FillTestCase] = [
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
        FillTestCase(
            amount=0,
            pour_position=1,
            terrain=[2, 0, 2],
            expected_water_terrain=[2, 0, 2]
        ),
        FillTestCase(
            amount=1,
            pour_position=2,
            terrain=[5, 1, 3, 0, 5],
            expected_water_terrain=[5, 1, 3, 1, 5],
        ),
        FillTestCase(
            amount=1,
            pour_position=2,
            terrain=[5, 0, 3, 0, 5],
            expected_water_terrain=[5, 1, 3, 0, 5],
        ),
        FillTestCase(
            amount=1,
            pour_position=0,
            terrain=[0, 1],
            expected_water_terrain=[0, 1],
        ),
    ]

    for case in valid_cases:
        print("Initial Terrain:\n")
        print_terrain(case.terrain)

        water_terrain = fill(case.amount, case.pour_position, case.terrain)

        print(
            f"\nTerrain after pouring {case.amount} units of water at position "
            f"{case.pour_position}:\n"
        )
        print_terrain(case.terrain, water_terrain)

        print(f"\nTotal water captured: {sum(water_terrain) - sum(case.terrain)}\n")
        assert water_terrain is not case.terrain, (
            f"Test failed for {case}: water_terrain is the same object as terrain"
        )
        assert water_terrain == case.expected_water_terrain, (
            f"Test failed for {case}: result={water_terrain}"
        )


def _run_fill_invalid_test_cases() -> None:
    invalid_cases: List[InvalidFillTestCase] = [
        InvalidFillTestCase(
            amount=1,
            pour_position=-1,
            terrain=[5, 0, 5],
            expected_exception=ValueError
        ),
        InvalidFillTestCase(
            amount=1,
            pour_position=3,
            terrain=[5, 0, 1],
            expected_exception=ValueError
        ),
        InvalidFillTestCase(
            amount=1,
            pour_position=0,
            terrain=[],
            expected_exception=ValueError
        ),
        InvalidFillTestCase(
            amount=-1,
            pour_position=1,
            terrain=[5, 0, 1],
            expected_exception=ValueError
        ),
        InvalidFillTestCase(
            amount=False,
            pour_position=1,
            terrain=[5, 0, 5],
            expected_exception=TypeError
        ),
        InvalidFillTestCase(
            amount=1.5,
            pour_position=1,
            terrain=[5, 0, 1],
            expected_exception=TypeError
        ),
        InvalidFillTestCase(
            amount="1",
            pour_position=1,
            terrain=[5, 0, 1],
            expected_exception=TypeError
        ),
        InvalidFillTestCase(
            amount=5,
            pour_position=False,
            terrain=[5, 0, 1],
            expected_exception=TypeError
        ),
        InvalidFillTestCase(
            amount=5,
            pour_position=1.5,
            terrain=[5, 0, 1],
            expected_exception=TypeError
        ),
        InvalidFillTestCase(
            amount=5,
            pour_position="1",
            terrain=[5, 0, 1],
            expected_exception=TypeError
        ),
    ]

    for case in invalid_cases:
        try:
            fill(case.amount, case.pour_position, case.terrain)
        except case.expected_exception:
            print(
                f"Correctly raised {case.expected_exception.__name__} for case: {case}"
            )
        else:
            assert False, (
                f"Expected {case.expected_exception.__name__} for case: {case}"
            )


def _run_print_terrain_valid_test_cases() -> None:
    sample_terrain = [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3]
    sample_water = [5, 4, 2, 1, 3, 2, 2, 2, 2, 2, 4, 3]
    valid_cases: List[TerrainTestCase] = [
        TerrainTestCase(
            terrain=sample_terrain,
            water=None,
            expected_output=(
                "+           \n"
                "++        + \n"
                "++  +     ++\n"
                "+++ +++   ++\n"
                "++++++++ +++\n"
                "++++++++++++\n"
            ),
        ),
        TerrainTestCase(
            terrain=sample_terrain,
            water=sample_water,
            expected_output=(
                "+           \n"
                "++        + \n"
                "++  +     ++\n"
                "+++ +++www++\n"
                "++++++++w+++\n"
                "++++++++++++\n"
            ),
        ),
        TerrainTestCase(
            terrain=(1, 0, 1),
            water=(1, 1, 1),
            expected_output="+w+\n+++\n",
        ),
        TerrainTestCase(
            terrain=(0, 0),
            water=None,
            expected_output="++\n",
        ),
    ]

    for case in valid_cases:
        output = StringIO()
        with redirect_stdout(output):
            print_terrain(case.terrain, case.water)

        assert output.getvalue() == case.expected_output, (
            f"Test failed for {case}: output={output.getvalue()!r}"
        )


def _run_print_terrain_invalid_test_cases() -> None:
    invalid_cases: List[InvalidTerrainTestCase] = [
        InvalidTerrainTestCase(terrain=[], water=None, expected_exception=ValueError),
        InvalidTerrainTestCase(terrain=[1], water=[], expected_exception=ValueError),
        InvalidTerrainTestCase(terrain=[1], water=[1, 1], expected_exception=ValueError),
        InvalidTerrainTestCase(terrain=[2], water=[1], expected_exception=ValueError),
        InvalidTerrainTestCase(terrain=[True], water=None, expected_exception=TypeError),
        InvalidTerrainTestCase(terrain=[1], water=[False], expected_exception=TypeError),
        InvalidTerrainTestCase(terrain=[1.0], water=None, expected_exception=TypeError),
        InvalidTerrainTestCase(terrain=[1], water=["1"], expected_exception=TypeError),
        InvalidTerrainTestCase(terrain=[-1], water=None, expected_exception=ValueError),
        InvalidTerrainTestCase(terrain=[1], water=[-1], expected_exception=ValueError),
    ]

    for case in invalid_cases:
        output = StringIO()
        try:
            with redirect_stdout(output):
                print_terrain(case.terrain, case.water)
        except case.expected_exception:
            assert output.getvalue() == "", (
                f"Invalid case produced partial output: {case}"
            )
        else:
            assert False, (
                f"Expected {case.expected_exception.__name__} for case: {case}"
            )


def main() -> None:
    _run_fill_valid_test_cases()
    _run_fill_invalid_test_cases()
    _run_print_terrain_valid_test_cases()
    _run_print_terrain_invalid_test_cases()


if __name__ == "__main__":
    main()
