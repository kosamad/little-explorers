
// Google Maps Elements
function initialize() {
  var mapOptions, map, marker,		
      addressEl = document.querySelector('#location_name'),
      latEl = document.querySelector('#map_lat'),
      longEl = document.querySelector('#map_long'),
      element = document.getElementById('map-canvas');


// Initial Map loaded
  mapOptions = {      
      zoom: 5,      
      center: new google.maps.LatLng(54.4592725673968, -2.8300778240695252),
     
      disableDefaultUI: false,
      scrollWheel: true, 
      draggable: true,
      //max zoom so area cannot be set too specifically.
  //  maxZoom: 12, 
      
  };

  // Creating a new map object using the constructor function google.maps.Map
  map = new google.maps.Map(element, mapOptions);

//Adding a marker to the map
  marker = new google.maps.Marker({
		position: {lat:53.46796246, lng: -2.32526235},
		map: map,		
		draggable: true
	});

  //can add mutliple markers to map by creating different marker variables
}

