def get_graf_quest_points(quest_points):
    quest_points = {point.step: point for point in quest_points}

    for step, point in quest_points.items():
        row, col = step // 1, step % 1
    graf_quest_points = []