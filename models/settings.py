"""
This module have the class settings.
"""

class Settings:
  """
  Create a Settings object with a color to show
  and a date in boolean value for validate.
  """
  def __init__(self, color:str, date:bool):
    self.color = color
    self.date = date

  def see_date(self):
    """
    Return True if the date property
    is True.
    """

    return True if self.date == True else False

  def __str__(self):
    return 'This is a settings object'