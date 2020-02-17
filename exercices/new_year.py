from datetime import datetime

for year in range(2021, 2021 + 10):
    if year % 2 == 0:
        new_year = datetime(year, 1, 1)
        print(year, new_year.strftime('%A'))
