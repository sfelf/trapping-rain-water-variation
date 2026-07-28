from typing import Any

import pytest

from fill import fill


@pytest.mark.parametrize(
    ("amount", "pour_position", "terrain", "expected"),
    [
        pytest.param(
            2,
            0,
            [5, 0, 1, 0, 5],
            [5, 1, 1, 1, 5],
            id="pour-from-left-wall",
        ),
        pytest.param(
            2,
            4,
            [5, 0, 1, 0, 5],
            [5, 1, 1, 1, 5],
            id="pour-from-right-wall",
        ),
        pytest.param(
            2,
            2,
            [5, 0, 1, 0, 5],
            [5, 1, 1, 1, 5],
            id="pour-from-basin-center",
        ),
        pytest.param(
            6,
            2,
            [5, 0, 1, 0, 5],
            [5, 2, 3, 2, 5],
            id="fill-multiple-levels",
        ),
        pytest.param(
            6,
            2,
            [0, 1, 2, 1, 0],
            [0, 1, 2, 1, 0],
            id="water-spills-from-uncontained-peak",
        ),
        pytest.param(
            6,
            2,
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            id="capture-limited-by-containment",
        ),
        pytest.param(
            4,
            6,
            [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            [5, 4, 2, 1, 3, 2, 2, 2, 2, 2, 4, 3],
            id="readme-example",
        ),
        pytest.param(
            15,
            6,
            [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            [5, 4, 3, 3, 4, 4, 4, 3, 3, 3, 4, 3],
            id="partially-fill-irregular-basin",
        ),
        pytest.param(
            50,
            6,
            [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            [5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3],
            id="excess-water-spills",
        ),
        pytest.param(
            50,
            6,
            [3, 4, 1, 0, 1, 2, 2, 3, 1, 2, 4, 5],
            [3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
            id="reversed-terrain-capacity",
        ),
        pytest.param(
            0,
            1,
            [2, 0, 2],
            [2, 0, 2],
            id="zero-amount",
        ),
        pytest.param(
            1,
            2,
            [5, 1, 3, 0, 5],
            [5, 1, 3, 1, 5],
            id="lower-candidate-on-right",
        ),
        pytest.param(
            1,
            2,
            [5, 0, 3, 0, 5],
            [5, 1, 3, 0, 5],
            id="left-wins-equal-height-tie",
        ),
        pytest.param(
            1,
            0,
            [0, 1],
            [0, 1],
            id="water-spills-at-exposed-edge",
        ),
    ],
)
def test_fill_places_water(
    amount: int,
    pour_position: int,
    terrain: list[int],
    expected: list[int],
) -> None:
    water_terrain = fill(amount, pour_position, terrain)

    assert water_terrain == expected


@pytest.mark.parametrize(
    "amount",
    [
        pytest.param(0, id="zero-amount"),
        pytest.param(2, id="nonzero-amount"),
    ],
)
def test_fill_returns_new_list_without_mutating_input(amount: int) -> None:
    terrain = [5, 0, 1, 0, 5]
    original = terrain.copy()

    result = fill(amount, 2, terrain)

    assert result is not terrain
    assert terrain == original


@pytest.mark.parametrize(
    ("amount", "pour_position", "terrain", "expected_exception"),
    [
        pytest.param(1, -1, [5, 0, 5], ValueError, id="negative-position"),
        pytest.param(
            1,
            3,
            [5, 0, 1],
            ValueError,
            id="position-equals-length",
        ),
        pytest.param(
            1,
            0,
            [],
            ValueError,
            id="position-in-empty-terrain",
        ),
        pytest.param(-1, 1, [5, 0, 1], ValueError, id="negative-amount"),
        pytest.param(False, 1, [5, 0, 5], TypeError, id="boolean-amount"),
        pytest.param(1.5, 1, [5, 0, 1], TypeError, id="float-amount"),
        pytest.param("1", 1, [5, 0, 1], TypeError, id="string-amount"),
        pytest.param(5, False, [5, 0, 1], TypeError, id="boolean-position"),
        pytest.param(5, 1.5, [5, 0, 1], TypeError, id="float-position"),
        pytest.param(5, "1", [5, 0, 1], TypeError, id="string-position"),
    ],
)
def test_fill_rejects_invalid_arguments(
    amount: Any,
    pour_position: Any,
    terrain: list[int],
    expected_exception: type[Exception],
) -> None:
    with pytest.raises(expected_exception):
        fill(amount, pour_position, terrain)
