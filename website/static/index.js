function deleteNote(noteID) {
    fetch('/delete-note', {  //reach the 'delete-note' endpoint
        method: 'POST',
        body: JSON.stringify({noteID: noteID}),
    }).then((_res) => {   //then clear the note
        window.location.href ="/";
    });
} 