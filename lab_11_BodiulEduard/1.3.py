import datetime
days_ua = {
    "Monday": "понеділок",
    "Tuesday": "вівторок",
    "Wednesday": "середа",
    "Thursday": "четвер",
    "Friday": "п’ятниця",
    "Saturday": "субота",
    "Sunday": "неділя"
}
year = int(input('В якому році ви народились? '))
month = int(input("Місяць: "))
birthday = int(input("День народження: "))
yearnow = datetime.datetime.today().year
age = yearnow - year
if (month, birthday) < (month, birthday):
    age -= 1
birth_day = datetime.date(year, month, birthday)
today = datetime.date.today()
if birth_day < today:
    birth_day = datetime.date(today.year + 1, month, birthday)
day_name = birth_day.strftime("%A")
days_to_birthday = (birth_day - today).days
print(f"Вік: {age}")
print(f"День народження: {days_ua[day_name]}")
print(f"Днів до наступного дня народження: {days_to_birthday}")