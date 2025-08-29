from abc import ABC, abstractmethod


class Grade(ABC):
    def get_grade(self):
        pass


class NormalGrade(Grade):
    def get_grade(self):
        return "NORMAL"


class SilverGrade(Grade):
    def get_grade(self):
        return "SILVER"


class GoldGrade(Grade):
    def get_grade(self):
        return "GOLD"
