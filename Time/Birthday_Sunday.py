import calendar

calendar_day_name = calendar.weekday(year=2023, month=7, day=26)

year = 2023

while calendar_day_name != 'Sunday':
    calendar_weekday = calendar.weekday(year=year, month=7, day=26)
    calendar_day_name = calendar.day_name[calendar_weekday]
    print(calendar.day_name[calendar_weekday] + ' ' + str(year))

    year += 1

