"""
This module have the class note.
"""

class Note:
  def __init__(self, content):
    self.id = None
    self.content = content

  def __str__(self):
    return f'This is a note with id {self.id}, and content {self.content}'