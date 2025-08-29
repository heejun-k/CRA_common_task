from Player import *


class AttandanceManageSystem:
    _instance = None
    players: dict = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AttandanceManageSystem, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.players = {}
        self.id_cnt = 0

    def add_if_new(self, name):
        find = False
        for p in self.players.values():
            if p.name == name:
                find = True

        if not find:
            self.id_cnt += 1
            self.players[self.id_cnt] = Player(name, self.id_cnt)

    def find_idx(self, name):
        for idx, p in self.players.items():
            if p.name == name:
                return idx

    def process_oneline(self, name, day):
        self.add_if_new(name)
        idx = self.find_idx(name)
        current_player = self.players[idx]
        current_player.increase_day(day)

    def load_file(self, file_name):
        try:
            with open(file_name, encoding="utf-8") as f:
                for _ in range(500):
                    line = f.readline()
                    if not line:
                        return False
                    parts = line.strip().split()
                    if len(parts) == 2:
                        current_name = parts[0]
                        current_day = parts[1]
                        self.process_oneline(current_name, current_day)
            return True
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")
            return False

    def cac_print_all(self):
        remove_players = []

        for i in range(1, self.id_cnt + 1):
            player = self.players[i]
            player.check_attendance()

            print(
                f"NAME : {player.name}, POINT : {player.point}, GRADE : {player.grade.get_grade()}"
            )
            if player.is_removed():
                remove_players.append(player.name)

        print("\nRemoved player")
        print("==============")
        for rp in remove_players:
            print(rp)


def run():
    manage_sys = AttandanceManageSystem()
    manage_sys.load_file("attendance_weekday_500.txt")
    manage_sys.cac_print_all()


if __name__ == "__main__":
    run()
