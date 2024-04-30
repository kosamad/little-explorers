
// Check if passords match
    function checkPasswordMatch() {
        var password = document.getElementById("password_hash").value;
        var confirmPassword = document.getElementById("password_hash2").value;
        var errorDiv = document.getElementById("password_error");

        if (password !== confirmPassword) {
            errorDiv.textContent = "Passwords do not match";
        } else {
            errorDiv.textContent = "";
        }
    }



