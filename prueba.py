from datetime import date, timedelta

def all_sundays(year):
    #January
    dt = date(year,1,1)

    #First Sunday of given year
    dt += timedelta(days=6-dt.weekday())
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)



for s in all_sundays(2020):
    print(s)