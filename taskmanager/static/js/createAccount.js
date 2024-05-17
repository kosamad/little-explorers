
// Check if passords match
    function checkPasswordMatch() {
        var password = document.getElementById("password_hash").value;
        var confirmPassword = document.getElementById("password_hash2").value;
        var errorDiv = document.getElementById("password_error");
        var submitButton = document.getElementById("submit_button");

        if (password !== confirmPassword) {
            errorDiv.textContent = "Passwords do not match";
            submitButton.disabled = true; 
        } else {
            errorDiv.textContent = "";
            submitButton.disabled = false;
        }
    }



