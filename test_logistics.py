import pytest

from mylib.logistics import find_coordinate, distanse, total_distanse


def test_find_coordinate():
    assert find_coordinate("Chicago") == (41.8781, -87.6298)


def test_find_coordinate_unknown_city():
    with pytest.raises(ValueError):
        find_coordinate("Boston")


def test_distanse():
    assert distanse("New York", "Chicago") == pytest.approx(711.04, rel=0.01)


def test_total_distanse():
    expected_total = distanse("New York", "Chicago") + distanse("Chicago", "Seattle")
    assert total_distanse(["New York", "Chicago", "Seattle"]) == pytest.approx(
        expected_total
    )


def test_total_distanse_with_one_city():
    assert total_distanse(["Chicago"]) == 0
