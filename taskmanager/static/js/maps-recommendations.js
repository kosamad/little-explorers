
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

  // Make an AJAX request to fetch map data and place markers
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/recommendations_map', true);
  xhr.onload = function() {
    if (xhr.status >= 200 && xhr.status < 400) {
      // Parse the response as JSON
      var mapData = JSON.parse(xhr.responseText);      

      // Iterate over each recommendation to extract data from the array of objects 
      mapData.forEach(function(data) {
        var lat = parseFloat(data['map_lat']);
        var lng = parseFloat(data['map_long']);
        var locationName = data['location_name'];
        var recommendationId = (data['recommendation_id']);
        console.log(recommendationId)      

        // Add marker for the recommendation
          marker = new google.maps.Marker({
          position: { lat: lat, lng: lng }, 
          map: map,
          title: locationName,
          draggable: false
        });

        // Set parameters for the user to click the marker and navigate to the correct page
        var recommendationUrl = `${window.location.origin}/recommendation/${recommendationId}`;

        // Click event listener to the marker to render specific reveiw
        marker.addListener('click', function() {
          window.location.href = recommendationUrl; 
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

