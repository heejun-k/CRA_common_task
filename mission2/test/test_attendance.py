import pytest
from attendance import *
import os


def test_all(capsys):
    run()
    captured = capsys.readouterr()

    golden_data = """NAME : Umar, POINT : 48, GRADE : SILVER\nNAME : Daisy, POINT : 45, GRADE : SILVER\nNAME : Alice, POINT : 61, GRADE : GOLD\nNAME : Xena, POINT : 91, GRADE : GOLD\nNAME : Ian, POINT : 23, GRADE : NORMAL\nNAME : Hannah, POINT : 127, GRADE : GOLD\nNAME : Ethan, POINT : 44, GRADE : SILVER\nNAME : Vera, POINT : 22, GRADE : NORMAL\nNAME : Rachel, POINT : 54, GRADE : GOLD\nNAME : Charlie, POINT : 58, GRADE : GOLD\nNAME : Steve, POINT : 38, GRADE : SILVER\nNAME : Nina, POINT : 79, GRADE : GOLD\nNAME : Bob, POINT : 8, GRADE : NORMAL\nNAME : George, POINT : 42, GRADE : SILVER\nNAME : Quinn, POINT : 6, GRADE : NORMAL\nNAME : Tina, POINT : 24, GRADE : NORMAL\nNAME : Will, POINT : 36, GRADE : SILVER\nNAME : Oscar, POINT : 13, GRADE : NORMAL\nNAME : Zane, POINT : 1, GRADE : NORMAL\n\nRemoved player\n==============\nBob\nZane\n"""
    assert golden_data == captured.out


def test_all_by_main(capsys):
    os.system("python attendance.py")


def test_loadfile_empty():
    am = AttandanceManageSystem()
    result = am.load_file("test/test_weekday_error.txt")
    assert result == False


def test_loadfile_no_file():
    am = AttandanceManageSystem()
    result = am.load_file("no.txt")
    assert result == False
