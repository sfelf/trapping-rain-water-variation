from contextlib import redirect_stdout
from dataclasses import dataclass
from io import StringIO
from typing import Any, Optional, Sequence, Type

from terrain import print_terrain


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


def test_print_terrain_valid_cases() -> None:
    sample_terrain = [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3]
    sample_water = [5, 4, 2, 1, 3, 2, 2, 2, 2, 2, 4, 3]
    valid_cases = [
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


def test_print_terrain_invalid_cases() -> None:
    invalid_cases = [
        InvalidTerrainTestCase(
            terrain=[],
            water=None,
            expected_exception=ValueError,
        ),
        InvalidTerrainTestCase(
            terrain=[1],
            water=[],
            expected_exception=ValueError,
        ),
        InvalidTerrainTestCase(
            terrain=[1],
            water=[1, 1],
            expected_exception=ValueError,
        ),
        InvalidTerrainTestCase(
            terrain=[2],
            water=[1],
            expected_exception=ValueError,
        ),
        InvalidTerrainTestCase(
            terrain=[True],
            water=None,
            expected_exception=TypeError,
        ),
        InvalidTerrainTestCase(
            terrain=[1],
            water=[False],
            expected_exception=TypeError,
        ),
        InvalidTerrainTestCase(
            terrain=[1.0],
            water=None,
            expected_exception=TypeError,
        ),
        InvalidTerrainTestCase(
            terrain=[1],
            water=["1"],
            expected_exception=TypeError,
        ),
        InvalidTerrainTestCase(
            terrain=[-1],
            water=None,
            expected_exception=ValueError,
        ),
        InvalidTerrainTestCase(
            terrain=[1],
            water=[-1],
            expected_exception=ValueError,
        ),
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
