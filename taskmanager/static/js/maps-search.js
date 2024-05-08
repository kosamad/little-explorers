function initialize() {
  var mapOptions, map, marker;
  var elementa = document.getElementById('map-canvas-search');
  var locations = document.querySelectorAll('.location-lat, .location-long');

  //Initial Map loaded
  mapOptions = {
    zoom: 5,
    center: { lat: 54.4592725673968, lng: -2.8300778240695252 },
    disableDefaultUI: false,
    scrollWheel: true,
    draggable: true,    
    maxZoom: 12, //this prevents a user being able to see too closely where the house is 
  };

  // Creating a new map object using the constructor function google.maps.Map
  map = new google.maps.Map(elementa, mapOptions);

  locations.forEach(function(location) {
    var lat = parseFloat(location.innerText);
    var lng = parseFloat(location.nextElementSibling.innerText);

    // Add marker for the recommendation
    marker = new google.maps.Marker({
      position: { lat: lat, lng: lng },
      map: map,
      draggable: false
    });
  });
}