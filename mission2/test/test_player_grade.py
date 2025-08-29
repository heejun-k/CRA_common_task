import pytest
from Player import *
from Grade import *


def test_player_get_points_wed():
    player1 = Player("heehee", 1)
    player1.increase_day("wednesday")
    player1.check_attendance()
    assert player1.get_points() == 3


def test_player_get_points_weekend():
    player1 = Player("heehee", 1)
    player1.increase_day("sunday")
    player1.increase_day("saturday")
    player1.check_attendance()
    assert player1.get_points() == 4


def test_player_grade():
    player1 = Player("heehee", 1)
    player1.increase_day("tuesday")
    player1.check_attendance()
    assert player1.grade.get_grade() == "NORMAL"


def test_player_removed_true():
    player1 = Player("heehee", 1)
    player1.increase_day("friday")
    player1.check_attendance()
    assert player1.is_removed() == True


def test_player_removed_false():
    player1 = Player("heehee", 1)
    player1.increase_day("wednesday")
    player1.check_attendance()
    assert player1.is_removed() == False


def test_grade_normal():
    grade1 = NormalGrade()
    assert grade1.get_grade() == "NORMAL"


def test_grade_silver():
    grade1 = SilverGrade()
    assert grade1.get_grade() == "SILVER"


def test_grade_gold():
    grade1 = GoldGrade()
    assert grade1.get_grade() == "GOLD"
