<?php
echo "<h2>^_^^_^php control^_^ </h2>";
$led_which = $_GET['which_led'];
$led_state = $_GET['led'];
if(!empty($led_which)) {
  $cmd = "sudo ./led.py " . $led_which . " " . $led_state . " >/dev/null 2>&1 &";
  echo "$cmd";
  echo  exec($cmd);
} else {
    echo "error to get led state";
}
function notify_led_state() 
{ 
     print_r("called led state in php file"); 
} 
?>
