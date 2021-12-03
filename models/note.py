"""
This module have the class note.
"""

class Note:
  def __init__(self, date:dict, content:str):
    self.id = None
    self.content = content
    self.date = date

  def __str__(self):
    return f'This is a note with id {self.id}, and content {self.content}'