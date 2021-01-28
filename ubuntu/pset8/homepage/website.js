
    let selector = document.querySelector('select');
        var x = document.getElementById('selector').text;
        selector.onchange = function() {
                document.querySelector('#experience').innerHTML = this.value;
        }