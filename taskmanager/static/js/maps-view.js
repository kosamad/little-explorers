// Google Maps Elements, initialise function and define variables. 
function initialize() {
  var mapOptions, map, marker, element = document.getElementById('map-canvas-view');

  // Get latitude and longitude values from divs on the page
  var lat = parseFloat(document.getElementById('fp-map_lat').innerText);
  var lng = parseFloat(document.getElementById('fp-map_long').innerText);

  //Initial Map loaded
  mapOptions = {
    zoom: 5,
    center: { lat: lat, lng: lng }, // Set center using lat and lng values
    disableDefaultUI: false,
    scrollWheel: true,
    draggable: true,    
    maxZoom: 12, //this revents a user being able to see too closely where the house is 
  };

  // Creating a new map object using the constructor function google.maps.Map
  map = new google.maps.Map(element, mapOptions);

  //Adding a marker to the map
  marker = new google.maps.Marker({
    position: { lat: lat, lng: lng }, // Set marker position using lat and lng values
    map: map,
    draggable: false
  });  

}
