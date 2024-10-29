import datetime

weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
weekdays_short = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]
months = ["января", "февраля",
          "марта", "апреля", "мая",
          "июня", "июля", "августа",
          "сентября", "октября", "ноября",
          "декабря"]


def try_read_date(date_string):
    cont = True
    try:
        date = datetime.datetime.strptime(date_string, "%d.%m.%y")
    except:
        try:
            date = datetime.datetime.strptime(date_string, "%d.%m.%Y")
        except:
            try:
                date_string += f".{datetime.datetime.now().year}"
                date = datetime.datetime.strptime(date_string, "%d.%m.%Y")
            except:
                date = date_string
                cont = False
    return date, cont


def get_day_id_and_day_title(date: datetime.datetime):
    day_id = f"{weekdays[date.weekday()]}.{date.strftime('%d.%m.%Y')}"
    day_title = f"{weekdays_short[date.weekday()]} {date.day} {months[date.month - 1]}"
    return day_id, day_title


def return_days(dates):
    dates = dates.replace(",", "")
    dates = dates.split(" ")
    days = []
    for date in dates:
        if_date = False
        if "-" in date:
            first = date.split("-")[0]
            second = date.split("-")[1]
            cont = True

            first_date, new_cont = try_read_date(first)
            cont = cont and new_cont

            second_date, new_cont = try_read_date(second)
            cont = cont and new_cont

            if cont:
                if second_date < first_date and second_date.month == 1 and first_date.month == 12:
                    second_date = datetime.datetime(year=second_date.year + 1,
                                                    month=second_date.month, day=second_date.day)
                if first_date + datetime.timedelta(days=30) < second_date:
                    cont = False
                while first_date <= second_date and cont:
                    day_id, day_title = get_day_id_and_day_title(first_date)
                    days.append({"id": day_id, "title": day_title})
                    first_date += datetime.timedelta(days=1)
                    if_date = True
        else:
            day_date, if_date = try_read_date(date)
            if if_date:
                day_id, day_title = get_day_id_and_day_title(day_date)
                days.append({"id": day_id, "title": day_title})

        if not if_date:
            days.append({"id": date, "title": date})
    return days
