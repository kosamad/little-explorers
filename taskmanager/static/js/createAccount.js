

// Check the username or password do not contain whitespace 
document.getElementById('username').addEventListener('blur', function () {
    var errorMessageUsername = document.getElementById('username_error');
    if (this.value.trim() === '') {
        errorMessageUsername.style.display = "block";
    } else {
        errorMessageUsername.style.display = 'none';
    }
  });

document.getElementById('password_hash').addEventListener('blur', function () {
    var errorMessagePassword = document.getElementById('password_error');
    if (this.value.trim() === '') {
        errorMessagePassword.style.display = "block";
    } else {
        errorMessagePassword.style.display = 'none';
    }
  });
  

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



