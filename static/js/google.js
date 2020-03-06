function initMap() {
  // The location of Space Florida
  var spacex = {lat: 28.609706, lng: -80.679705};
  // Position map view
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 15 , center: spacex});
  // Position marker at Space Florida
  var marker = new google.maps.Marker({position: spacex, map: map});
}