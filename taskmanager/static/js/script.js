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

  // var iconDropdown = document.getElementById('icon-dropdown');
  // var getIcon = document.getElementById('get-icon');

  // iconDropdown.addEventListener('click', function (event) {
  //   // Check if the clicked element is an <i> tag
  //   if (event.target.classList.contains('icon-option')) {
  //     // Get the icon class from the data-icon attribute
  //     var selectedIcon = event.target.getAttribute('data-icon');
  //     // Update the selected icon div
  //     getIcon.innerHTML = '<input id="selected_icon" name="selected_icon" type="text" required><label for="selected_icon">Selected Icon:    <i class="' + selectedIcon  + '"></i></label>';
  //     console.log(iconClass);
  //   }
  // });

  var iconDropdown = document.getElementById('icon-dropdown');
  var selectedIconHidden = document.getElementById('selected_icon');
  var selectedIconDisplay = document.getElementById('selected_icon_display');

  iconDropdown.addEventListener('click', function (event) {
    if (event.target.classList.contains('icon-option')) {
      var iconClass = event.target.getAttribute('data-icon');
      // Update the hidden input field with the selected icon class
      selectedIconHidden.value = iconClass;
      // Display the selected icon to the user
      selectedIconDisplay.innerHTML = '<label for="display_only">Icon</label><input id="display_only" name="display_only" type="text" readonly><i class="' + iconClass + '"></i>';
    }
  });

});