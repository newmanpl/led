<?php
$cpu_temp = $_GET['cpu_temp'];

if ($cpu_temp == 'req') {
  $cmd = "sudo python ./get_temp.py cpu_temp";
  exec($cmd, $res, $rc);

  $temp_num = substr($res[0], -4);
  print_r($temp_num);
} elseif ($cpu_temp == 'autorun') {
  $cmd = "sudo python ./get_temp.py autorun";
  exec($cmd, $res, $rc);
  $temp_num = substr($res[0], -4);
  print_r($temp_num);
} elseif ($cpu_temp == 'reboot') {
//  forceShutdown(false); //only reboot
} else {
//  forceShutdown(true);
}

function forceShutdown($shutdown) {
  if ($shutdown == true) {
    print_r("poweroff in 2.5 s");
    usleep(2550*1000);
    $cmd = "sudo poweroff -p ";
    exec($cmd);
 } else {
    print_r("reboot in 2.5 s");
    usleep(2550*1000);
    $cmd = "sudo reboot ";
    exec($cmd);
 }
}

function parseArgs($args) {
  foreach($args as $arg) {
    if ($arg == 'notify_led_state') {
      global $argv;
      $p1 = $argv[2];
      $p2 = $argv[3];
      print "now callback ";
      return true;
    }
  }
  return false;
}
?>
