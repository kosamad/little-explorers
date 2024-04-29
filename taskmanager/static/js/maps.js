// Code for map, search box and geocoding modified from the youtube tutorial by Imran Sayed using the methods by Google's API

// Google Maps Elements, initialise function and define variables. 
function initialize() {
  var mapOptions, map, marker, searchBox,
    addressEl = document.querySelector('#location_name'),
    latEl = document.querySelector('#map_lat'),
    longEl = document.querySelector('#map_long'),
    element = document.getElementById('map-canvas');


  //Initial Map loaded
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
    position: {
      lat: 53.46796246,
      lng: -2.32526235
    },
    map: map,
    draggable: true
  });

  //can add mutliple markers to map by creating different marker variables

  // create a search box. Places library loaded from google JS API
  searchBox = new google.maps.places.SearchBox(addressEl);

  // when address is changed and selected, place the marker at that location. 
  google.maps.event.addListener(searchBox, 'places_changed', function () {

    var places = searchBox.getPlaces(), //gets the place info (address etc) from the searchbox
      bounds = new google.maps.LatLngBounds(), //gives lat and long values.
      i, place, lat, long,
      address = places[0].formatted_address;

    for (i = 0; place = places[i]; i++) {
      bounds.extend(place.geometry.location);
      marker.setPosition(place.geometry.location); // Sets marker position
    }  

    map.fitBounds(bounds); // adjust viewport to where the bounds are. 
    map.setZoom(15);
    //getting lat and long data from the map
    lat = marker.getPosition().lat();
    long = marker.getPosition().lng();
    latEl.value = lat;
    longEl.value = long;
  })

  // Capturing the marker information if the user moves the marker on the map. 
  google.maps.event.addListener(marker, "dragend", function (event) {
    var lat, long, address;
    lat = marker.getPosition().lat();
    long = marker.getPosition().lng();

    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({
      latLng: marker.getPosition()
    }, function (result, status) {
      if ('OK' === status) {
        address = result[0].formatted_address;
        //updated address, lat and long parameters in HTML
        addressEl.value = address;
        latEl.value = lat;
        longEl.value = long;

      } else {
        console.log('Geocode was not successful for the following reason: ' + status);
      }




      // Closes the previous info window if it already exists
      // if (infoWindow) {
      //   infoWindow.close();
      // }

      /**
       * Creates the info Window at the top of the marker need to put in first function if I want it. 
      //  */
      // infoWindow = new google.maps.InfoWindow({
      //   content: address
      // });

      // infoWindow.open(map, marker);
    });
  })

};