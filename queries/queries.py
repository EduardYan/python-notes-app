"""
This module have the queries
for the database.
"""

# queries for the database
DELETE_QUERY = 'DELETE FROM notes WHERE(id = {id})'
INSERT_QUERY = 'INSERT INTO notes(content) VALUES("{content}")'
SELECT_QUERY = 'SELECT * FROM notes'
