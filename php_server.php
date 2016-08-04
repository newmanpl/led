<?php
$lightX = $_GET['which_led'];
$led_state = $_GET['led'];
$cpu_temp = $_GET['cpu_temp'];

if ($cpu_temp == 'req') {
  $cmd = "sudo python ./get_temp.py";
  exec($cmd, $res, $rc);

  $temp_num = substr($res[0], -4);
  print_r($temp_num);
} elseif ($cpu_temp == 'reboot') {
  forceShutdown(false); //only reboot
} else {
  forceShutdown(true);
}
// $cur_time = microtime(true);
if(!empty($lightX)) {
  $con = mysqli_connect('192.168.10.166', 'led', 'access102', 'led');
  //$cur_time = round(microtime(true) * 1000);
    $cmd = "sudo python ./ledmain.py " . $lightX . " " . $led_state . " >/dev/null 2>&1 &";
  //print_r("cur_time " . $cur_time);
  //echo "$cmd";
    /*echo*/  system($cmd);
    usleep(550*1000); //sleep 100 ms
    if ($con) {
    $sql = "SELECT state FROM tb_led WHERE id='$lightX'";
    $result = mysqli_query($con, $sql);

    if (false == $result) {
      printf("error: %s\n", mysqli_error($con));
    } else {
//      printf("successfully\n");
      $rows=mysqli_fetch_row($result);
      echo $rows[0];
    }
  } else {
    echo "error to get led state";
  }
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
