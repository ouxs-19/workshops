<?php
error_reporting(0);
error_log(0);

if (isset($_POST["user"]) && isset($_POST["pass"]) && (!empty($_POST["user"])) && (!empty($_POST["pass"]))) {
    $user = $_POST["user"];
    $pass = $_POST["pass"];

    $db = new SQLite3("/var/db.sqlite");
    $result = $db->query("SELECT * FROM users WHERE username='$user' and password='$pass'" );
    if ($result === false) die("Something went wrong");
    else $result = $result->fetchArray();

    if ($result) {
        $logged_in = true;
        $asUser = $result["username"];
    }
    else $err = "No such user";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>MP24 - SQLi</title>
</head>
<body>
    <?php if (isset($logged_in) && $logged_in): ?>
    <p>Welcome back, you are logged in as <?= $asUser;?> <p>
    <?php else: ?>
    <form method="post">
        <input type="text" placeholder="Username" name="user" required>
        <input type="password" placeholder="Password" name="pass" required>
        <button type="submit">Login</button>
        <br><br>
        <?php if (isset($err)) echo $err; ?>
    </form>
    <?php endif; ?>
</body>
</html>
