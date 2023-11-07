import datetime
from dateutil import easter

now = datetime.datetime.now()

# Get the current year
current_year = now.year

print(easter.easter(current_year + 1, method=3))
