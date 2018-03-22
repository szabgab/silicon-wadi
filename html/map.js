//$(document).ready(function(){
//    $("#title").html("Hello jQuery");
//}); 


var companies = [];

function show_map() {
    var t = document.getElementById('technology')
    var technology = '';
    if (t.options[t.selectedIndex]) {
        technology = t.options[t.selectedIndex].value;
    }
    //console.log(technology);
    var center = {lat: 32.2765615, lng: 34.81151369999998};
    var the_map = new google.maps.Map(document.getElementById('map'), {
        zoom: 9,
        center: center
    });

    for (var i=0; i < companies.length; i++) {
        for (var j=0; j < companies[i]['offices'].length; j++) {
            var company = companies[i];
            //console.log(company['offices'][j]);
            if (! company['offices'][j]['coordinates']) {
                continue;
            }

			// filter by technology
            if (technology) {
                if (! company['technologies']) {
                    continue;
                }
                var hits = companies[i]['technologies'].filter(function(v) {
                    return technology == v
                })
                if (hits.length == 0) {
                    continue;
                }
            }

			add_marker(the_map, company, j);
        }
    }
}

function add_marker(the_map, company, j) {
    //console.log(company['offices'][j]);
    var marker = new google.maps.Marker({
        position: company['offices'][j]['coordinates'],
        title: company.name,
        map: the_map
    });

    var msg = '<h4>' + company.name + '</h4>';
    msg += company.offices[j].address;
    msg += '<br>';
    msg += '<a href="' + company.url + '">Web site</a>';
    msg += "<br>";

    var infowindow = new google.maps.InfoWindow({
        content: msg
    });

    marker.addListener('click', function() {
        infowindow.open(the_map, marker);
    });
}

function initMap() {
    document.getElementById('show').addEventListener('click', show_map);

    $.get( '/data/technologies.json', function( data ) {
        console.log(data);
        var html = "<option></option>";
        for (var i=0; i < data.length; i++) {
            html += "<option>" + data[i] + "</option>";
        }
        $("#technology").html(html);
    });

    $.get( '/data/companies.json', function( data ) {
       companies = data;
       //console.log(companies);
       show_map();
    });
}

