// Creating map and setting up default view
var map = L.map('map').setView([45.5019, -73.5674], 12);
//Coosing tiling provider and giving attributions
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
// Addding marker to map
var marker = L.marker([45.4897, -73.5881]).addTo(map);
marker.bindPopup("Dawson College")
// Adding circle to map
var circle = L.circle([45.4897, -73.5881], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map);
circle.bindPopup("Danger Zone around Dawson College")

// Standalone Popup
var popup = L.popup()
    .setLatLng([45.5019, -73.5674])
    .setContent("I am a standalone popup.")
    .openOn(map);
// openOn makes it so that popup closes when any other one is opened

// Map click event listener
// latlng, defines location on map where event happened 
var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);
