// Implement Deleting Task
// Select all buttons with class 'delete-task-btn' using querySelectorAll
document.querySelectorAll('.delete-task-btn').forEach(button => {

    // Add a click event listener to each button
    button.addEventListener('click', () => {
        // Get the task ID from the button's data-id attribute
        const taskId = button.getAttribute('data-id');

        // Use SweetAlert2 (Swal) to display a confirmation dialog
        Swal.fire({
            title: 'Are you sure?',
            text: 'You won\'t be able to revert this!',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6', // Customize confirm button color
            cancelButtonColor: '#d33', // Customize cancel button color
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {

            // Check if user confirms deletion
            if (result.isConfirmed) {

                // Send a DELETE request to /tasks/:taskId endpoint
                fetch(`/tasks/${taskId}`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json' // Set content type header
                    }
                }).then(response => response.json()).then(data => { // Parse response as JSON

                    // Check if deletion was successful from response data
                    if (data.success) {

                        // Remove the task element from the DOM based on its ID
                        document.getElementById(`task-${taskId}`).remove();

                        // Show success message using SweetAlert2
                        Swal.fire('Deleted!', 'Your task has been deleted.', 'success');
                    } else {

                        // Show error message using SweetAlert2
                        Swal.fire('Failed!', 'Failed to delete task.', 'error');
                    }
                });
            }
        });
    });
});

// Implement Complete Task
// Select all buttons with class 'mark-completed-btn' using querySelectorAll
document.querySelectorAll('.mark-completed-btn').forEach(button => {
    button.addEventListener('click', () => {
        const taskId = button.getAttribute('data-id');

        // Send a POST request to /tasks/:taskId/complete endpoint to mark task complete
        fetch(`/tasks/${taskId}/complete`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Set content type for sending JSON data
            },
            body: JSON.stringify({
                completed: true
            }) // Set completed property to true
        }).then(response => response.json()).then(data => {
            if (data.success) {

                // Update button text and styles to reflect completed state
                button.textContent = 'Completed';
                button.classList.remove('btn-primary'); // Remove default button style
                button.classList.add('btn-success'); // Add success button style
                button.disabled = true; // Disable button after completion
                Swal.fire('Success!', 'Task marked as completed.', 'success');
            } else {
                Swal.fire('Failed!', 'Failed to mark task as completed.', 'error');
            }
        });
    });
});