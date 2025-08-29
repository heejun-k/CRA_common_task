def add_id(name, player_id):
    id_cnt = len(player_id)
    if name not in player_id:
        id_cnt += 1
        player_id[name] = id_cnt


def process_oneline(name, day, days_count, player_id):
    add_id(name, player_id)
    current_id = player_id[name]
    if day == "wednesday":
        days_count["wed"][current_id] += 1
    elif day == "saturday" or day == "sunday":
        days_count["weeken"][current_id] += 1
    else:
        days_count["otherdays"][current_id] += 1


def load_file(file_name):
    wed = [0] * 100
    weeken = [0] * 100
    otherdays = [0] * 100
    days_count = {"wed": wed, "weeken": weeken, "otherdays": otherdays}
    player_id = {}
    names = {}

    try:
        with open("attendance_weekday_500.txt", encoding="utf-8") as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    current_name = parts[0]
                    current_day = parts[1]
                    process_oneline(current_name, current_day, days_count, player_id)
                    names[player_id[current_name]] = current_name
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    return days_count, names


def get_points(id, days_count):
    point = (
        days_count["wed"][id] * 3
        + days_count["weeken"][id] * 2
        + days_count["otherdays"][id]
    )
    if days_count["wed"][id] > 9:
        point += 10
    if days_count["weeken"][id] > 9:
        point += 10
    return point


def get_grade(point):
    if point >= 50:
        return "GOLD"
    elif point >= 30:
        return "SILVER"
    else:
        return "NORMAL"


def calculate_print(days_count, names):
    remove_players = []
    id_cnt = len(names)
    for i in range(1, id_cnt + 1):
        point = get_points(i, days_count)
        grade = get_grade(point)
        print(f"NAME : {names[i]}, POINT : {point}, GRADE : {grade}")
        if (
            grade == "NORMAL"
            and days_count["wed"][i] == 0
            and days_count["weeken"][i] == 0
        ):
            remove_players.append(names[i])

    print("\nRemoved player")
    print("==============")
    for rp in remove_players:
        print(rp)


def run():
    days_count, names = load_file()
    calculate_print(days_count, names)


if __name__ == "__main__":
    run()
