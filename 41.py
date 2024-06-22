def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

def get_day_of_week(year, month, day):
    t = (year - 1900) * 365 + sum(is_leap_year(y) for y in range(1900, year))
    month_days = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t += sum(month_days[i] for i in range(month - 1))
    t += day - 1
    return t % 7  # 0 for Sunday, 1 for Monday, ..., 6 for Saturday

def count_sundays_on_first_of_month():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if get_day_of_week(year, month, 1) == 0:
                count += 1
    return count

if __name__ == "__main__":
    result = count_sundays_on_first_of_month()
    print("The number of Sundays that fell on the first of the month during the twentieth century is:", result)
