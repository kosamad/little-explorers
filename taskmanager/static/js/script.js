document.addEventListener('DOMContentLoaded', function () {
  // sidenav initialisation
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);
  // navbar dropdown initialisation
  let dropdown = document.querySelectorAll('.dropdown-trigger');
  M.Dropdown.init(dropdown);

  // select initialization
  let selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);

  // icon dropdown
  let dropdownTrigger = document.getElementById('dropdown-trigger-two');
  M.Dropdown.init(dropdownTrigger);

  // datepicker initialization
  let datepicker = document.querySelectorAll(".datepicker");
  M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    i18n: {
      done: "Select"
    }
  });

  //  modal initialization
  var modal = document.querySelectorAll('.modal');
  M.Modal.init(modal);


  // // Icon idendtificaion in the new recommendation form.
  //  var holidayTypeSelect = document.getElementById('holiday_id');
  //  var recommendationIconDisplay = document.getElementById('icon-display')
  // //  if statement prevents event listeners trying to attach on pages where they don't exist. 
  //  if (holidayTypeSelect){
  //     holidayTypeSelect.addEventListener('change', function () {
  //     var selectedHolidayId = holidayTypeSelect.value;
  //     recommendationIconDisplay.innerHTML = selectedHolidayId
  //     console.log("Selected Holiday Type ID:", selectedHolidayId);        
  //     });
  //   }

  // Displaying the icon to the user and storing it in the database
  var iconDropdown = document.getElementById('icon-dropdown');
  var selectedIconHidden = document.getElementById('selected_icon');
  var selectedIconDisplay = document.getElementById('selected_icon_display');
  var iconClass = '';


  if (iconDropdown) {
    iconDropdown.addEventListener('click', function (event) {
      if (event.target.classList.contains('icon-option')) {
        iconClass = event.target.getAttribute('data-icon');
        // Update the hidden input field with the selected icon class
        selectedIconHidden.value = iconClass;
        // Display the selected icon to the user
        selectedIconDisplay.innerHTML = '<input id="display_only" name="display_only" type="text" readonly class="validate" required><label for="display_only">Icon Selected: <i class="' + iconClass + '"></i></label>';
        // Prevent user clicking in the icon box
        var displayInput = document.getElementById('display_only');
        displayInput.disabled = true;
      }
    });
  }


})

// Removing flash messages after 3 seconds
setTimeout(function() {
  var flashMessages = document.getElementById('flash-messages');
  if (flashMessages) {
      flashMessages.remove();
  }
}, 3000); 