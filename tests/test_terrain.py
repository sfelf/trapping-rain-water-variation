from typing import Any, Sequence

import pytest

from terrain import print_terrain


INVALID_TERRAIN_CASES = [
    pytest.param([], None, ValueError, id="empty-terrain"),
    pytest.param([1], [], ValueError, id="empty-water"),
    pytest.param([1], [1, 1], ValueError, id="length-mismatch"),
    pytest.param([2], [1], ValueError, id="water-below-terrain"),
    pytest.param([True], None, TypeError, id="boolean-terrain-height"),
    pytest.param([1], [False], TypeError, id="boolean-water-height"),
    pytest.param([1.0], None, TypeError, id="float-terrain-height"),
    pytest.param([1], ["1"], TypeError, id="string-water-height"),
    pytest.param([-1], None, ValueError, id="negative-terrain-height"),
    pytest.param([1], [-1], ValueError, id="negative-water-height"),
]


@pytest.mark.parametrize(
    ("terrain", "water", "expected"),
    [
        pytest.param(
            [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            None,
            (
                "+           \n"
                "++        + \n"
                "++  +     ++\n"
                "+++ +++   ++\n"
                "++++++++ +++\n"
                "++++++++++++\n"
            ),
            id="plain-readme-terrain",
        ),
        pytest.param(
            [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            [5, 4, 2, 1, 3, 2, 2, 2, 2, 2, 4, 3],
            (
                "+           \n"
                "++        + \n"
                "++  +     ++\n"
                "+++ +++www++\n"
                "++++++++w+++\n"
                "++++++++++++\n"
            ),
            id="readme-terrain-with-water",
        ),
        pytest.param(
            (1, 0, 1),
            (1, 1, 1),
            "+w+\n+++\n",
            id="tuple-sequences",
        ),
        pytest.param(
            (0, 0),
            None,
            "++\n",
            id="zero-height-baseline",
        ),
    ],
)
def test_print_terrain_renders_expected_output(
    terrain: Sequence[int],
    water: Sequence[int] | None,
    expected: str,
    capsys: pytest.CaptureFixture[str],
) -> None:
    print_terrain(terrain, water)

    assert capsys.readouterr().out == expected


@pytest.mark.parametrize(
    ("terrain", "water", "expected_exception"),
    INVALID_TERRAIN_CASES,
)
def test_print_terrain_rejects_invalid_input(
    terrain: Sequence[Any],
    water: Sequence[Any] | None,
    expected_exception: type[Exception],
) -> None:
    with pytest.raises(expected_exception):
        print_terrain(terrain, water)


@pytest.mark.parametrize(
    ("terrain", "water", "expected_exception"),
    INVALID_TERRAIN_CASES,
)
def test_print_terrain_does_not_emit_output_for_invalid_input(
    terrain: Sequence[Any],
    water: Sequence[Any] | None,
    expected_exception: type[Exception],
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(expected_exception):
        print_terrain(terrain, water)

    assert capsys.readouterr().out == ""
