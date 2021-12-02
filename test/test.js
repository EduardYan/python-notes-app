/**
 * This is a file for save the note
 * in the localStorage.
 */



class Note {
  /**
   * 
   * @param {number} id The id of the note for indentify
   * @param {string} content The text content of the note
   */
  constructor(id, content) {
    this.id = id;
    this.content = content;

  }

}

class UI {
  constructor() {
    this.notes = []; // list for save the notes
    this.notesCounter = 1;
  }

  getNotes() {
    // getting and validating the notes for show
    const notes = localStorage.getItem('notes');
    if (notes) {
      this.notes = JSON.parse(notes);
      this.notesCounter = this.notes.length;
      return this.notes;

    } else {
      return 'Not Found';
    }
  }

  /**
   * 
   * @param {number} id The id of the note for delete
   */
  deleteNote(id) {
    console.log(id);
  }

  /**
   * 
   * @param {Note} note The object note for show
   * @returns A text for confirm the saved
   */
  saveNote (note) {
    const noteObject = { // objecto for save
      id: note.id,
      content: note.content,
    };

    this.notes.push(noteObject); // adding at the list for save

    localStorage.setItem('notes', JSON.stringify(this.notes));
    this.notesCounter++; // adding

    return "Saved Succesfully";
  }

  /**
   * 
   * @param {Note} note The note for show
   * @returns A text for confirm the save
   */
  showNote(note) {
    const container = document.querySelector('#notes-view')
    const cardNote = document.createElement('div');
    cardNote.className = "note";
    cardNote.innerHTML = `
    <span class="title-note">${note.id}</span>
    <p class="text-note">${note.content}</p>
    <button class="delete-button">Delete</button>
    `;

    container.append(cardNote);

    return "Showed"
  }

  /**
   * Show the notes in the interface
   */
  showNotes () {
    // recorriendo the notes for show
    for (let i = 0; i < this.notes.length; i++)  {
      const noteCurrent =  this.notes[i];
      this.showNote(noteCurrent);
    }

  }
}

/**
 * 
 * @returns The text of the note created
 */
function getText() {
  textNote = document.getElementById("text").value;
  return textNote;
}



// creating a ui object and showing the notes
const ui = new UI();
const notes = ui.getNotes();
console.log(notes);
ui.showNotes();

document.getElementById("save-button").addEventListener("click", () => {
  const textNote = getText();
  const note = new Note(ui.notesCounter, textNote);

  ui.saveNote(note); // saving and showing the note
  ui.showNote(note);


});

const numberNote = document.querySelector(".title-note");

document.querySelector(".delete-button").addEventListener("click", () => {
  ui.deleteNote(numberNote);
});