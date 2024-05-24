document.addEventListener('DOMContentLoaded', function () {

  // Function to render the image to the user when they use the upload button.
  document.getElementById('upload-button').addEventListener('click', function () {
    var fileInput = document.getElementById('image');
    var file = fileInput.files[0];
    if (!file) {
      return; // No file selected
    }
    var reader = new FileReader();
    reader.onload = function (event) {
      var imageUrl = event.target.result;
      document.getElementById('uploaded-image').innerHTML = '<img src="' + imageUrl + '">';
    };
    reader.readAsDataURL(file);
  });

  // Extract the mimetype from the image and save it in a hidden input element.
  document.getElementById('image').addEventListener('change', function (event) {
    const file = event.target.files[0];
    const mimetype = file.type;
    document.getElementById('mimetype').value = mimetype;
  });

  // Event listener which runs the select check function when the submit button is clicked.
  document.getElementById('submit-button').addEventListener('click', function (event) {
    // Prevent the form from submitting if validation fails
    if (!checkSelectFields()) {
      event.preventDefault();
    }
  });


  // Code to check if the name chosen by the user already exists in the db
  var recommendationNameInput = document.getElementById("recommendation_name");
  var errorMessage = document.getElementById("title_error");
  // Listens for user typing in the input field.
  recommendationNameInput.addEventListener("input", function () {
    var recommendationName = recommendationNameInput.value.trim(); //removing any spaces
    if (recommendationName !== "") {
      checkRecommendationTitle(recommendationName);
    } else {
      errorMessage.style.display = "none";
    }
  });

  // Check the name, address or reveiw do not contain whitespace 
  document.getElementById('recommendation_name').addEventListener('blur', function () {
    var errorMessageWS = document.getElementById('recommendation_name_error');
    if (this.value.trim() === '') {
      errorMessageWS.style.display = "block";
    } else {
      errorMessageWS.style.display = 'none';
    }
  });

  document.getElementById('location_name').addEventListener('blur', function () {
    var errorMessageLocation = document.getElementById('location_error');
    if (this.value.trim() === '') {
      errorMessageLocation.style.display = "block"; // Show the error message
    } else {
      errorMessageLocation.style.display = 'none'; // Hide the error message
    }
  });

  document.getElementById('recommendation_review').addEventListener('blur', function () {
    var errorMessageReview = document.getElementById('review_error');
    if (this.value.trim() === '') {
      errorMessageReview.style.display = "block"; // Show the error message
    } else {
      errorMessageReview.style.display = 'none'; // Hide the error message
    }
  });





  //Check function sends a Post request to the server to check if the name already exits.
  //JSON response from check recommendation route gives a exists propery (with a value True or False)
  // when xhr has completed, reponse is parsed as JSON and error message is displayed if the title already exists.
  function checkRecommendationTitle(recommendationName) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/check_recommendation_title", true);
    xhr.setRequestHeader("Content-Type", "application/json"); // sets the type of data the server should expect
    xhr.onload = function () {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        if (response.exists) {
          // If the title already exists, display an error message
          errorMessage.style.display = "block";
        } else {
          // If the title is unique, hide the error message
          errorMessage.style.display = "none";
        }
      }
    };
    // if there is an error during the xhr
    xhr.onerror = function () {
      console.error("Request failed");
    };
    // data sent to server as JSON data to validate against existing entries in the db
    xhr.send(JSON.stringify({
      recommendation_name: recommendationName
    }));
  }


  // Function to check if the select options have been changed by the user and that mime type = a valid image format.
  function checkSelectFields() {
    let errorMessage = '';
    let isValid = true;

    let holidayId = document.getElementById('holiday_id');
    if (holidayId.value === '') {
      errorMessage += 'Please select a Holiday Type.\n';
      isValid = false;
    }

    let region = document.getElementById('region');
    if (region.value === '') {
      errorMessage += 'Please select a Region.\n';
      isValid = false;
    }

    let occupants = document.getElementById('occupants');
    if (occupants.value === '') {
      errorMessage += 'Please select the number of Occupants.\n';
      isValid = false;
    }

    let mimetype = document.getElementById('mimetype');
    if (mimetype.value === '') {
      errorMessage = 'Please select a file with the format jpeg, jpg, or png.\n';
      isValid = false;
    } else {
      // Check if the MIME type is an image format
      let acceptedImageTypes = ['image/jpeg', 'image/jpg', 'image/png'];
      if (!acceptedImageTypes.includes(mimetype.value)) {
        errorMessage = 'Please select a file with the format jpeg, jpg, or png.\n';
        isValid = false;
      }
    }
    if (!isValid) {
      alert(errorMessage);
    }
    return isValid;
  }


  // Function to give the user a count down of remaining characters for the reveiw
  document.getElementById('recommendation_review').addEventListener('input', function () {
    var textLength = this.value.length;
    var maxLength = parseInt(this.getAttribute('maxlength'));
    var remainingChars = maxLength - textLength;
    document.getElementById('charCount').textContent = remainingChars;
  });

});

// Function to check the maximum length of input fields.
function checkMaxLength(input) {
  if (input.value.length > input.maxLength) {
    input.value = input.value.slice(0, input.maxLength);
  }
}