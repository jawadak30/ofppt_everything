from datetime import datetime,time,date
import re

# how to input date and time
reg_date = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
reg_time = re.compile(r"\b\d{2}:\d{2}\b")

while True:
    my_date = input("enter date(AAAA-MM-JJ):")
    matches = reg_date.search(my_date)
    if not matches:
        print("invalid date!")
        continue
    try:
        my_date = date.fromisoformat(my_date)
        my_today = date.today()
        if my_date <= my_today:
            print("invalid date!")
            continue
        print(f"your date is correct {my_date}")
    except:
        print("invalid date!")
        continue
    break
while True:
    my_time = input("enter heure(HH:MM):")
    matches = reg_time.search(my_time)
    if not matches:
        print("invalid time!")
        continue
    try:
        my_time = time.fromisoformat(my_time)
        print(f"your time is correct {my_time}")
    except:
        print("invalid time!")
        continue
    break

my_date_time = datetime.combine(my_date,my_time)
print(f"la date et heure sont {my_date_time}")