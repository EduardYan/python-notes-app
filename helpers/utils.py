"""
This module some functions
for use.
"""

from datetime import datetime

def get_date():
  """
  Return the time current
  for add at the note.
  """

  # get for return
  day = datetime.now().day
  month = datetime.now().month
  year = datetime.now().year

  date_current = {
    'day': day,
    'month': month,
    'year': year
  }

  return date_current

if __name__ == '__main__':
  date = get_date()
  print('Testing the get_date() function')
  print(date)