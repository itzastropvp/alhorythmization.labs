import datetime
def show_datetime():
    now = datetime.datetime.now()
    print(now.strftime("Сьогодні: %d.%m.%y, час: %H:%M"))
show_datetime()