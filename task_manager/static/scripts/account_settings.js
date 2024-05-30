document.querySelector('form').addEventListener('submit', function(event) {
    const newPassword = document.getElementById('new_password').value;
    const confirmNewPassword = document.getElementById('confirm_new_password').value;

    if (newPassword !== confirmNewPassword) {
        event.preventDefault();
        alert('New passwords do not match');
    }
});