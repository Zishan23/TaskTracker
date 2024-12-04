/**
 * deleteNote Function
 * The unique identifier of the note to be deleted.
 * Sends a POST request to '/delete-note' endpoint, deleting the specified note.
 * Redirects to the home page after successful deletion.
 */

function deleteNote(noteID){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}