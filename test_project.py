import pytest
from project import add_score, calculate_average, assign_grade, pass_fail


def test_add_score():
    data = {}
    data = add_score(data, "Josephine", 85)
    data = add_score(data, "Josephine", 95)
    assert data["Josephine"] == [85, 95]

    with pytest.raises(ValueError):
        add_score(data, "Korpo", 150)
        add_score(data, "Korpo", -10)


def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90

    with pytest.raises(ValueError):
        calculate_average([])


def test_assign_grade():
    assert assign_grade(92) == "A"
    assert assign_grade(82) == "B"
    assert assign_grade(72) == "C"
    assert assign_grade(62) == "D"
    assert assign_grade(40) == "F"


def test_pass_fail():
    assert pass_fail(60) == "Pass"
    assert pass_fail(59) == "Fail"
    assert pass_fail(100) == "Pass"
    assert pass_fail(0) == "Fail"