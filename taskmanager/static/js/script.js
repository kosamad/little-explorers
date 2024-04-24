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
  var dropdownTrigger = document.getElementById('dropdown-trigger-two');
  M.Dropdown.init(dropdownTrigger);

  // Displaying the icon to the user and storing it in the database
  var iconDropdown = document.getElementById('icon-dropdown');
  var selectedIconHidden = document.getElementById('selected_icon');
  var selectedIconDisplay = document.getElementById('selected_icon_display');
  var iconClass = '';

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






})

function checkMaxLength(input) {
  if (input.value.length > input.maxLength) {
    input.value = input.value.slice(0, input.maxLength);
  }
}