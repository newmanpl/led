<?php
  $led_which = $_GET['which_led'];
  $led_state = $_GET['led'];
  if(!empty($led_which))
    $cmd = "sudo ./ledmain.py " . $led_which . " " . $led_state . " >/dev/null 2>&1 &";
    //echo "$cmd";
    /*echo*/  exec($cmd);
    usleep(500*1000); //sleep 100 ms

  $con = mysqli_connect('192.168.8.133', 'root', 'pi', 'led');
    if ($con) {
    $tolight = 'light' . $led_which;
    $sql = "SELECT state FROM tb_led WHERE id='$tolight'";
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
