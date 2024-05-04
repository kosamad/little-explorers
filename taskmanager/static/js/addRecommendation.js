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

  // Function to check the maximum length of input fields.
  function checkMaxLength(input) {
    if (input.value.length > input.maxLength) {
      input.value = input.value.slice(0, input.maxLength);
    }
  }

});