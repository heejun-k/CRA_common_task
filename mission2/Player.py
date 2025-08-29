from Grade import *


class Player:
    GOLD_POINTS = 50
    SILVER_POINTS = 30

    def __init__(self, name, id):
        self.id = id
        self.point = 0
        self.grade = NormalGrade()
        self.days = {"wed": 0, "weekend": 0, "others": 0}
        self.name = name

    def get_points(self):
        return self.point

    def increase_day(self, day):
        if day == "wednesday":
            self.days["wed"] += 1
        elif day == "saturday" or day == "sunday":
            self.days["weekend"] += 1
        else:
            self.days["others"] += 1

    def calculate_points(self):
        self.point = 0
        self.point += self.days["wed"] * 3
        self.point += self.days["weekend"] * 2 + self.days["others"]
        if self.days["wed"] > 9:
            self.point += 10
        if self.days["weekend"] > 9:
            self.point += 10

    def generate_grade(self):
        if self.point >= self.GOLD_POINTS:
            self.grade = GoldGrade()
        elif self.point >= self.SILVER_POINTS:
            self.grade = SilverGrade()
        else:
            self.grade = NormalGrade()

    def is_removed(self):
        if self.grade.get_grade() == "NORMAL":
            if self.days["wed"] == 0 and self.days["weekend"] == 0:
                return True
        return False

    def check_attendance(self):
        self.calculate_points()
        self.generate_grade()
