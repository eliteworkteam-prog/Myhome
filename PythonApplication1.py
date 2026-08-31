
from datetime import date


def day_of_week(day, month, year):
    days = [
        "понедельник", "вторник", "среда",
        "четверг", "пятница", "суббота", "воскресенье"
    ]
    return days[date(year, month, day).weekday()]


def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def get_age(day, month, year):
    today = date.today()
    age = today.year - year

    if (today.month, today.day) < (month, day):
        age -= 1

    return age


digits = {
    "0": [" *** ", "*   *", "*   *", "*   *", " *** "],
    "1": ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
    "2": [" *** ", "*   *", "   * ", "  *  ", "*****"],
    "3": ["**** ", "    *", " *** ", "    *", "**** "],
    "4": ["*  * ", "*  * ", "*****", "   * ", "   * "],
    "5": ["*****", "*    ", "**** ", "    *", "**** "],
    "6": [" *** ", "*    ", "**** ", "*   *", " *** "],
    "7": ["*****", "    *", "   * ", "  *  ", " *   "],
    "8": [" *** ", "*   *", " *** ", "*   *", " *** "],
    "9": [" *** ", "*   *", " ****", "    *", " *** "]
}


def print_date(day, month, year):
    birthday = f"{day:02d}{month:02d}{year:04d}"

    for row in range(5):
        for number in birthday:
            print(digits[number][row], end="  ")
        print()


print("Введите дату рождения:")

day = int(input("День: "))
month = int(input("Месяц: "))
year = int(input("Год: "))

try:
    date(year, month, day)

    print("\nДень недели:", day_of_week(day, month, year))

    if is_leap_year(year):
        print("Год високосный")
    else:
        print("Год не високосный")

    print("Возраст:", get_age(day, month, year))

    print("\nДата рождения:")
    print_date(day, month, year)

except ValueError:
    print("Ошибка: введена неправильная дата.")

