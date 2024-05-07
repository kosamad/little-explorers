// Google Maps Elements, initialise function and define variables. 
function initialize() {
  var mapOptions, map, marker, element = document.getElementById('map-canvas-recommendations');
  
  //Initial Map loaded
  mapOptions = {
    zoom: 5,
    center: new google.maps.LatLng(54.4592725673968, -2.8300778240695252),
    disableDefaultUI: false,
    scrollWheel: true,
    draggable: true,    
    maxZoom: 12, 
  };
  
  map = new google.maps.Map(element, mapOptions);

  // Make an AJAX request to fetch map data
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/recommendations_map', true);
  xhr.onload = function() {
    if (xhr.status >= 200 && xhr.status < 400) {
      // Parse the response as JSON
      var mapData = JSON.parse(xhr.responseText);

      // Iterate over each recommendation to extract latitude and longitude
      mapData.forEach(function(data) {
        var lat = parseFloat(data['map_lat']);
        var lng = parseFloat(data['map_long']);
        var locationName = data['location_name'];       

        // Add marker for this recommendation
          marker = new google.maps.Marker({
          position: { lat: lat, lng: lng }, 
          map: map,
          title: locationName,
          draggable: false
        });
      });
    } else {
      console.error('Request failed: ' + xhr.status);
    }
  };
  xhr.onerror = function() {
    console.error('Request failed');
  };
  xhr.send();
}






  // // Get latitude and longitude values from divs on the page
  // {% for recommendation in recommendations %}
  //       var lat = parseFloat(document.getElementById('map_lat_{{ recommendation.id }}').innerText);
  //       var lng = parseFloat(document.getElementById('map_long_{{ recommendation.id }}').innerText);

  // // Creating a new map object using the constructor function google.maps.Map
  // map = new google.maps.Map(element, mapOptions);

  // //Adding a marker to the map
  // marker = new google.maps.Marker({
  //   position: { lat: lat, lng: lng }, 
  //   map: map,
  //   draggable: false
  // });
  // {% endfor %}}


