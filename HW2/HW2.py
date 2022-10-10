import re
from datetime import datetime

dates = []

while True:
    date = input()
    correct_date = re.findall(r"\w+ \d{1,2}, \d{4}", date)
    dates.extend(correct_date)

    if date == "-1":
        break

    current_date = datetime.today().strftime('%Y-%m-%d')

    for day in dates:
        date = datetime.strptime(day, '%B %d, %Y')
        date_format = date.strftime('%Y-%m-%d')

    if date_format <= current_date:
        print(date.strftime('%m/%d/%Y'))
    elif date_format > current_date:
        continue
