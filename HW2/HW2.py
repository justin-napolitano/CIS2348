import re
from datetime import datetime

dates = []
with open("inputDates.txt", "r") as dates_file:
    for date in dates_file:
        correct_date = re.findall(r"\w+ \d{1,2}, \d{4}", date)
        dates.extend(correct_date)

current_date = datetime.today().strftime('%Y-%m-%d')

for item in dates:
    date = datetime.strptime(item, '%B %d, %Y')
    date_ = date.strftime('%Y-%m-%d')

    if date_ < current_date:
        f = open("parsedDates.txt", "a")
        f.write(date.strftime('%m/%d/%Y') + "\n")

f.close()