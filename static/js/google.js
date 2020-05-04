function initMap() {
  // Location of Spacex in Florida
  var spacex = {lat: 28.609706, lng: -80.679705};
  // Position the map view
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 15 , center: spacex});
  // Position the marker on Spacex Florida
  var marker = new google.maps.Marker({position: spacex, map: map});
}