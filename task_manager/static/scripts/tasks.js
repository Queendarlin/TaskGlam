document.querySelectorAll('.delete-task-btn').forEach(button => {
    button.addEventListener('click', () => {
        const taskId = button.getAttribute('data-id');
        Swal.fire({
            title: 'Are you sure?',
            text: 'You won\'t be able to revert this!',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.isConfirmed) {
                fetch(`/tasks/${taskId}`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }).then(response => response.json()).then(data => {
                    if (data.success) {
                        document.getElementById(`task-${taskId}`).remove();
                        Swal.fire('Deleted!', 'Your task has been deleted.', 'success');
                    } else {
                        Swal.fire('Failed!', 'Failed to delete task.', 'error');
                    }
                });
            }
        });
    });
});

document.querySelectorAll('.mark-completed-btn').forEach(button => {
    button.addEventListener('click', () => {
        const taskId = button.getAttribute('data-id');
        fetch(`/tasks/${taskId}/complete`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ completed: true })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                button.textContent = 'Completed';
                button.classList.remove('btn-primary');
                button.classList.add('btn-success');
                button.disabled = true;
                Swal.fire('Success!', 'Task marked as completed.', 'success');
            } else {
                Swal.fire('Failed!', 'Failed to mark task as completed.', 'error');
            }
        });
    });
});
