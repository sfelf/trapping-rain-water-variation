from dataclasses import dataclass
from typing import Any, List, Type

from fill import fill


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


def test_fill_valid_cases() -> None:
    valid_cases: List[FillTestCase] = [
        FillTestCase(
            amount=2,
            pour_position=0,
            terrain=[5, 0, 1, 0, 5],
            expected_water_terrain=[5, 1, 1, 1, 5],
        ),
        FillTestCase(
            amount=2,
            pour_position=4,
            terrain=[5, 0, 1, 0, 5],
            expected_water_terrain=[5, 1, 1, 1, 5],
        ),
        FillTestCase(
            amount=2,
            pour_position=2,
            terrain=[5, 0, 1, 0, 5],
            expected_water_terrain=[5, 1, 1, 1, 5],
        ),
        FillTestCase(
            amount=6,
            pour_position=2,
            terrain=[5, 0, 1, 0, 5],
            expected_water_terrain=[5, 2, 3, 2, 5],
        ),
        FillTestCase(
            amount=6,
            pour_position=2,
            terrain=[0, 1, 2, 1, 0],
            expected_water_terrain=[0, 1, 2, 1, 0],
        ),
        FillTestCase(
            amount=6,
            pour_position=2,
            terrain=[0, 1, 0, 1, 0],
            expected_water_terrain=[0, 1, 1, 1, 0],
        ),
        FillTestCase(
            amount=4,
            pour_position=6,
            terrain=[5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            expected_water_terrain=[5, 4, 2, 1, 3, 2, 2, 2, 2, 2, 4, 3],
        ),
        FillTestCase(
            amount=15,
            pour_position=6,
            terrain=[5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            expected_water_terrain=[5, 4, 3, 3, 4, 4, 4, 3, 3, 3, 4, 3],
        ),
        FillTestCase(
            amount=50,
            pour_position=6,
            terrain=[5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            expected_water_terrain=[5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3],
        ),
        FillTestCase(
            amount=50,
            pour_position=6,
            terrain=[5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3][::-1],
            expected_water_terrain=[3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
        ),
        FillTestCase(
            amount=0,
            pour_position=1,
            terrain=[2, 0, 2],
            expected_water_terrain=[2, 0, 2],
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
        water_terrain = fill(case.amount, case.pour_position, case.terrain)

        assert water_terrain is not case.terrain, (
            f"Test failed for {case}: water_terrain is the same object as terrain"
        )
        assert water_terrain == case.expected_water_terrain, (
            f"Test failed for {case}: result={water_terrain}"
        )


def test_fill_invalid_cases() -> None:
    invalid_cases: List[InvalidFillTestCase] = [
        InvalidFillTestCase(
            amount=1,
            pour_position=-1,
            terrain=[5, 0, 5],
            expected_exception=ValueError,
        ),
        InvalidFillTestCase(
            amount=1,
            pour_position=3,
            terrain=[5, 0, 1],
            expected_exception=ValueError,
        ),
        InvalidFillTestCase(
            amount=1,
            pour_position=0,
            terrain=[],
            expected_exception=ValueError,
        ),
        InvalidFillTestCase(
            amount=-1,
            pour_position=1,
            terrain=[5, 0, 1],
            expected_exception=ValueError,
        ),
        InvalidFillTestCase(
            amount=False,
            pour_position=1,
            terrain=[5, 0, 5],
            expected_exception=TypeError,
        ),
        InvalidFillTestCase(
            amount=1.5,
            pour_position=1,
            terrain=[5, 0, 1],
            expected_exception=TypeError,
        ),
        InvalidFillTestCase(
            amount="1",
            pour_position=1,
            terrain=[5, 0, 1],
            expected_exception=TypeError,
        ),
        InvalidFillTestCase(
            amount=5,
            pour_position=False,
            terrain=[5, 0, 1],
            expected_exception=TypeError,
        ),
        InvalidFillTestCase(
            amount=5,
            pour_position=1.5,
            terrain=[5, 0, 1],
            expected_exception=TypeError,
        ),
        InvalidFillTestCase(
            amount=5,
            pour_position="1",
            terrain=[5, 0, 1],
            expected_exception=TypeError,
        ),
    ]

    for case in invalid_cases:
        try:
            fill(case.amount, case.pour_position, case.terrain)
        except case.expected_exception:
            pass
        else:
            assert False, (
                f"Expected {case.expected_exception.__name__} for case: {case}"
            )
