import io

from lib.file import File
from lib.point import Point


def test_read_grid() -> None:
    doc = "ABCDE\nFGHIJ\nKLMNO\n"

    f = File(io.StringIO(doc))
    grid = f.read_grid()

    assert grid is not None
    assert grid.width == 5
    assert grid.height == 3


def test_read_points() -> None:
    doc = "0,1\n2,3\n"

    f = File(io.StringIO(doc))
    points = f.read_points()

    assert points == [Point(0, 1), Point(2, 3)]


def test_read_lines() -> None:
    doc = "FOO\nBAR\n\nBAZ\nBAT\n"

    f = File(io.StringIO(doc))
    lines1 = f.read_lines()
    lines2 = f.read_lines()

    assert lines1 == ["FOO", "BAR"]
    assert lines2 == ["BAZ", "BAT"]


def test_read_line() -> None:
    doc = "FOO\nBAR\n"

    f = File(io.StringIO(doc))

    assert f.read_line() == "FOO"
