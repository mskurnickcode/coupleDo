    var lat = null
    var long = null
    navigator.geolocation.getCurrentPosition(function(position) {
        lat = position.coords.latitude;
        long = position.coords.longitude;
    });

    let locationShower = document.querySelector('#geolocation');
    locationShower.onmouseover = function() {
            document.querySelector('#geolocation').innerHTML = lat + ', ' + long;
        }
    locationShower.onmouseout = function() {
        document.querySelector('#geolocation').innerHTML = "Hello and Welcome to whoever is at coordinates:"
    }
