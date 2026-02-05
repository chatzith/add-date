"""
Calculates and prints the future date
by adding the number of days provided in the argument
to the current date.
"""

import sys
from datetime import datetime, timedelta

days = int(sys.argv[1])

current_date = datetime.now()

future_date = (current_date + timedelta(days)).strftime("%d/%m/%Y")

print(future_date)
