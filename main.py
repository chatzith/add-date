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

RESULT = f"""
The date after {days} days from now ({current_date.strftime("%d/%m/%Y")}) is:
{future_date}
"""

print(RESULT)
