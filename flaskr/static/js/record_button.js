function recordButton(input, select_type) {
    // Send an AJAX request to the Flask server to record the button click
    fetch('/record_button', {
        method: 'POST',
        body: JSON.stringify({ input: input, type: select_type }),
        headers: {
            'Content-Type': 'application/json'
        }
    });

}

function toggleButtonColor(button,input,type) {
    if (button.classList.contains('active')) {
        button.classList.remove('active');
    } else {
        button.classList.add('active');
    }
    recordButton(input, type);
}