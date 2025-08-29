player_id = {}
id_cnt = 0

names = [""] * 100
wed = [0] * 100
weeken = [0] * 100
otherdays = [0] * 100


def get_id(name):
    global id_cnt
    if name not in player_id:
        id_cnt += 1
        player_id[name] = id_cnt
        names[id_cnt] = name
    return player_id[name]


def process_oneline(name, day):
    current_id = get_id(name)
    if day == "wednesday":
        wed[current_id] += 1
    elif day == "saturday" or day == "sunday":
        weeken[current_id] += 1
    else:
        otherdays[current_id] += 1


def load_file():
    try:
        with open("attendance_weekday_500.txt", encoding="utf-8") as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    process_oneline(parts[0], parts[1])
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def get_points(id):
    point = wed[id] * 3 + weeken[id] * 2 + otherdays[id]
    if wed[id] > 9:
        point += 10
    if weeken[id] > 9:
        point += 10
    return point


def get_grade(point):
    if point >= 50:
        return "GOLD"
    elif point >= 30:
        return "SILVER"
    else:
        return "NORMAL"


def calculate_print():
    remove_players = []
    for i in range(1, id_cnt + 1):
        point = get_points(i)
        grade = get_grade(point)
        print(f"NAME : {names[i]}, POINT : {point}, GRADE : {grade}")
        if grade == "NORMAL" and wed[i] == 0 and weeken[i] == 0:
            remove_players.append(names[i])

    print("\nRemoved player")
    print("==============")
    for rp in remove_players:
        print(rp)


def run():
    load_file()
    calculate_print()


if __name__ == "__main__":
    run()
