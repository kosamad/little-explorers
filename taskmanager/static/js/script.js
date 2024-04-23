document.addEventListener('DOMContentLoaded', function () {
  // sidenav initialisation
  var sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);
  // navbar dropdown initialisation
  var dropdown = document.querySelectorAll('.dropdown-trigger');
  M.Dropdown.init(dropdown);

  // icon dropdown
  
  var dropdownTrigger = document.getElementById('dropdown-trigger-two');
    M.Dropdown.init(dropdownTrigger);

  var iconDropdown = document.getElementById('icon-dropdown');
  var selectedIcon = document.getElementById('selected-icon');

  iconDropdown.addEventListener('click', function (event) {
    // Check if the clicked element is an <i> tag
    if (event.target.classList.contains('icon-option')) {
      // Get the icon class from the data-icon attribute
      var iconClass = event.target.getAttribute('data-icon');
      // Update the selected icon div
      selectedIcon.innerHTML = '<input id="selected_icon" name="selected_icon" type="text" readonly required><label for="selected_icon">Selected Icon:    <i class="' + iconClass + '"></i></label>';
      console.log(iconClass);
    }
  });

})