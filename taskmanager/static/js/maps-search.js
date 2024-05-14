function initialize() {
  var mapOptions, map, marker;
  var elementa = document.getElementById('map-canvas-recommendations');
  var locations = document.querySelectorAll('.card-content');

  //Initial Map loaded
  mapOptions = {
    zoom: 5,
    center: {
      lat: 54.4592725673968,
      lng: -2.8300778240695252
    },
    disableDefaultUI: false,
    scrollWheel: true,
    draggable: true,
    maxZoom: 12, //this prevents a user being able to see too closely where the holiday house is 
  };

  // Creating a new map object using the constructor function google.maps.Map
  map = new google.maps.Map(elementa, mapOptions);

  locations.forEach(function(location) {
    var recommendationId = location.dataset.recommendationId;
    var lat = parseFloat(location.dataset.locationLat);
    var lng = parseFloat(location.dataset.locationLong);
    var recommendationName = location.dataset.recommendationName;

    // Add marker for the recommendation
    marker = new google.maps.Marker({
      position: {
        lat: lat,
        lng: lng
      },
      map: map,
      title: `Title: ${recommendationName}`,
      draggable: false
    });

    // Set parameters for the user to click the marker and navigate to the correct page
    var recommendationUrl = `${window.location.origin}/recommendation/${recommendationId}`;

    // Click event listener to the marker to render specific review
    marker.addListener('click', function () {
      window.location.href = recommendationUrl;
    });
  });
}