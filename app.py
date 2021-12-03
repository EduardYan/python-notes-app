"""
This is the principal
file for execute the web server.
"""

from flask import Flask, render_template, redirect, request, url_for, flash
from models.note import Note
from models.database import DataBase, DB_PATH
from queries.queries import INSERT_QUERY, DELETE_QUERY, SELECT_QUERY
from helpers.utils import get_date

app = Flask(__name__)
# settings for the sessions
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
@app.route('/home')
def home():
  """
  This is the initial route.
  """
  # getting the notes for pass to layout
  db = DataBase(DB_PATH)
  notes_list = db.select(SELECT_QUERY)
  db.close()

  # to index.html pass the notes lis of the database for show it
  return render_template('index.html', notes_list = notes_list)

@app.route('/about')
def about():
  """
  This route is for show
  the about page.
  """

  return render_template('about.html')

@app.route('/add-note', methods=['POST'])
def add_note():
  """
  This route is for add
  the note at the database.
  And redirect to home page.
  """

  # getting the content of the note of the form and creating a note object
  content_note = request.form['content']
  date = get_date()
  note = Note(date, content_note)

  # creating the connection and save the note in the database
  db = DataBase(DB_PATH)
  db.insert(INSERT_QUERY.format(day = note.date['day'], month = note.date['month'], year = note.date['year'],  content = note.content))
  db.close()

  flash('Note Added Successfully.')

  # redirecting to home
  return redirect(url_for('home'))

@app.route('/delete-note/<string:id>')
def delete_note(id):
  """
  This route is for delete
  the note of the database and redirect
  to home.
  """

  idNote = id

  # connecting and deleting
  db = DataBase(DB_PATH)
  db.delete(DELETE_QUERY.format(id = idNote))
  db.close()

  flash(f'Note number {id} Deleted Sucessfully.')

  # redirecting to home
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(port = 5000, debug = True)
