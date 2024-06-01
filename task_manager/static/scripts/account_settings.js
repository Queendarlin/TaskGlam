// Enforces matching passwords during password change form submission
document.querySelector('form').addEventListener('submit', function(event) {

    // Prevent form submission if new and confirm passwords don't match
    const newPassword = document.getElementById('new_password').value;
    const confirmNewPassword = document.getElementById('confirm_new_password').value;

    if (newPassword !== confirmNewPassword) {
        event.preventDefault();
        alert('New passwords do not match');
    }
});