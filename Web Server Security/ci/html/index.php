<html>
  <head>
    <title>Ping Service</title>
    <meta charset="utf-8"/>
  </head>

  <style>
    body {
      font-family: 'sans-serif';
      font-size: x-large;
      background-size: cover;
      background-color: black;
      color: lime;
    }
    a {
      text-decoration: none;
      color: cornsilk;
    }
    input {
      font-size: x-large;
      color: black;
    }
  </style>

  <body>
    <a href="index.php" title="Ping Service">
      <h1>Ping Service</h1>
    </a>
    <p>Check out this great pinging tool !</p>
    <br>
    <form method="POST">
      <input type="text" autofocus="on" name="ip" placeholder="127.0.0.1">
      <input type="submit" name="submit" value="Run">
    </form>

<?php
  if (isset($_POST["ip"])) {
    $ip = $_POST["ip"];
    $output = system('ping -c 1 '.$ip);
    echo '<p>Output:<br><br>'.nl2br("$output").'</p>';
  }
?>

</body>
</html>

