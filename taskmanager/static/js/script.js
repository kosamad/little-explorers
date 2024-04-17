document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialisation
    var sidenav = document.querySelectorAll('.sidenav');
     M.Sidenav.init(sidenav);

    var dropdown = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(dropdown);
  });