<html>
<head>
<title> led test </title>
<style>
body {
  background-color: yellow !important;
  font-size: 14px;
  margin: 0px;
  padding: 0px;
  position: absolute;
  width:1280px;
  height:720px;
  left:0px;
  top: 0px;
}
button:focus
{
  background-color:#555555;
}

.buttonstyle{
  height: 40px;
  width: 320px;
  outline: none;
}
</style>

</head>
<body>
<center>
<H1> light the world</H1>
</center>
<script>
function turn_light(state) {
  var logger = document.getElementById('logger');
  var xhr = new XMLHttpRequest();
  if (state == true) {
    xhr.open("GET","index.php?led=on", true);
    logger.innerHTML += 'the light is turned on' + "<br>";
//    var newURL = window.location.protocol + "//" + window.location.host + window.location.pathname;
//    window.location = newURL + "?led=on";
  }else{
    logger.innerHTML += 'the light is turned off' + "<br>";
    xhr.open("GET","index.php?led=off", true);
//    var newURL = window.location.protocol + "//" + window.location.host + window.location.pathname;
//    window.location = newURL + "?led=off";
  }
  xhr.send();
}
</script>

 <button class="buttonstyle" onclick="turn_light(false)">turn off</button>
 <button class="buttonstyle" onclick="turn_light(true)">turn on</button>
<br><br><br><br><br>
 <button class="buttonstyle" type="button" onclick="window.location.reload()">Reload Window</button><br>
<div id='logger'></div>

<?php
$led_state = $_GET['led'];
if(!empty($led_state)) {
  printf("led state = %s\n", $led_state);
  $cmd = "sudo ./led.py " . $led_state;
  echo  exec($cmd);
}
?>
</body>

</html>
