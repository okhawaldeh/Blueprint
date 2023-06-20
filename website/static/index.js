function deleteNote(noteId) {
    fetch("/delete-note", { //this sends a post request to the target (delete-note)
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),

    }).then((_res) => { //once the request is done, redirect to home page (refresh)
      window.location.href = "/";
    });
  }