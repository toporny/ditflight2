<?php
$row = 1;
if (!isset($_GET['airports'])) {
  print "example usage:<br>\nhttp://alltic.home.pl/d16127504/?airports=DUB,BVA,LTN,ORK,GDN";
  exit;
}
$arr = explode(",",$_GET['airports']);
if (count($arr)>9){
  print "MAX 9 elements! Example usage:<br>\nhttp://alltic.home.pl/d16127504/?airports=DUB,BVA,LTN,ORK,GDN";
  exit;
}


?>
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Marker Labels</title>
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAm3Tw0uz0aA-GNfIqPRE6qi2Kn-rzDHD0"></script>

    <script>
      // In the following example, markers appear when the user clicks on the map.
      // Each marker is labeled with a single alphabetical character.
      var labels = '0123456789';
      var labelIndex = 0;

      function initialize() {
        var bangalore = { lat: 53.421333, lng: -6.270075 };
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 1,
          center: bangalore
        });

        positions = [
<?php
if (($handle = fopen("airport.csv", "r")) !== FALSE) {
   $result_array = array();
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $row++;
        if (in_array($data[4], $arr)) {
          $result_array[$data[4]] =  array($data[6], $data[7], $data[1], $data[2], $data[3], $data[4]);
        #echo "          {name :'".$data[4]."', lat: ". $data[6] . ", long: ". $data[7] . "},\n";
        }
    }
    fclose($handle);
foreach($arr as $key =>$item) {
            echo "          {name :'".$item."', lat: ". $result_array[$item][0] . ", long: ". $result_array[$item][1]  .  ", name1: '". $result_array[$item][2]."', name2: '". $result_array[$item][3]."', name3: '". $result_array[$item][4].  "'},\n";
}

#print_r($result_array);
#exit;
}
?>
        ];

        var latlngbounds = new google.maps.LatLngBounds();
        var flightPlanCoordinates = [];
        for (i=0;i<positions.length; i++) {
            console.log(positions[i].name);
            console.log(positions[i].lat);
            console.log(positions[i].long);
            flightPlanCoordinates.push({lat: positions[i].lat, lng: positions[i].long});
            myLatLng = {lat: positions[i].lat, lng: positions[i].long};
            latlngbounds.extend( myLatLng );
            addMarker2(myLatLng, map, positions[i].name, positions[i].name1, positions[i].name2, positions[i].name3 );
        }
        map.fitBounds(latlngbounds);

        var flightPath = new google.maps.Polyline({
          path: flightPlanCoordinates,
          geodesic: true,
          strokeColor: '#FF0000',
          strokeOpacity: 1.0,
          strokeWeight: 2
        });


        var flightPlanCoordinates = [];
        flightPlanCoordinates.push({lat: positions[positions.length-1].lat, lng: positions[positions.length-1].long});
        flightPlanCoordinates.push({lat: positions[0].lat, lng: positions[0].long});

        var flightPath2 = new google.maps.Polyline({
          path: flightPlanCoordinates,
          geodesic: true,
          strokeColor: '#FF00FF',
          strokeOpacity: 1.0,
          strokeWeight: 2
        });

        flightPlanCoordinates.push({lat: positions[0].lat, lng: positions[0].long});

        flightPath2.setMap(map);

        flightPath.setMap(map);

      }

      // Adds a marker to the map.
      function addMarker2(location, map, name, info1, info2, info3) {
        // Add the marker at the clicked location, and add the next-available label
        // from the array of alphabetical characters.
        var marker = new google.maps.Marker({
          position: location,
          title: 'Hello World!',
          label: labels[labelIndex++ % labels.length],
          map: map
        });
        var infowindow = new google.maps.InfoWindow({
          content: '<b>'+name+'</b><br>'+info1+'<br>'+info2+'<br>'+info3
        });
        marker.addListener('click', function() {
          infowindow.open(map, marker);
        });
      }


      google.maps.event.addDomListener(window, 'load', initialize);

    </script>
  </head>
  <body>
    <div id="map"></div>
  </body>
</html>