
// Google Maps Elements
function initialize() {
  var mapOptions, map, marker,		
      addressEl = document.querySelector('#location_name'),
      latEl = document.querySelector('#map_lat'),
      longEl = document.querySelector('#map_long'),
      element = document.getElementById('map-canvas');

  mapOptions = {
      // How far the maps zooms in.
      zoom: 5,
      // Current Lat and Long position of the pin
      center: new google.maps.LatLng(54.4592725673968, -2.8300778240695252),
      // center : {
      // lat: -34.397,
      // lng: 150.644
      // },
      disableDefaultUI: false, // Disables the controls like zoom control on the map if set to true
      scrollWheel: true, // If set to false disables the scrolling on the map.
      draggable: true, // If set to false , you cannot move the map around.
      // mapTypeId: google.maps.MapTypeId.HYBRID, // If set to HYBRID its between sat and ROADMAP, Can be set to SATELLITE as well.
      // maxZoom: 11, // Wont allow you to zoom more than this
      // minZoom: 9  // Wont allow you to go more up.
  };

  // Creating a new map object using the constructor function google.maps.Map
  map = new google.maps.Map(element, mapOptions);
}

