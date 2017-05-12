<?php
$lightX = $_GET['which_led'];
$led_state = $_GET['led'];
//  $cur_time = microtime(true);
$con = mysqli_connect('192.168.8.166', 'led', 'access102', 'led');
if(!empty($lightX)) {
  //$cur_time = round(microtime(true) * 1000);
  //  $cmd = "sudo python ./ledmain.py " . $lightX . " " . $led_state . " >/dev/null 2>&1 &";
    $cmd = "sudo python ./ledmain.py " . $lightX . " " . $led_state ;
  //print_r("cur_time " . $cur_time);
  //echo "$cmd";
    /*echo*/  exec($cmd);
//    usleep(25*1000); //sleep 100 ms
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
