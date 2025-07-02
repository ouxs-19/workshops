<?php
    $db = new SQLite3("/var/db.sqlite");
    $db->exec("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)");
    $db->exec("INSERT INTO users VALUES ('Nazim', 'RandomPwd1')");
    $db->exec("INSERT INTO users VALUES ('admin', 'secretPass')");
    $db->exec("INSERT INTO users VALUES ('Fanel', 'MaybeSecure')");
    $db->exec("INSERT INTO users VALUES ('Mehdi', 'SQLIREALLY')");
    $db->exec("INSERT INTO users VALUES ('Ludmila', 'obviously')");
    $db->exec("INSERT INTO users VALUES ('Brahim', 'Brahim D Yuto')");
    $db->exec("INSERT INTO users VALUES ('Meriem', '38aea50657b6009f04165fff8f6a812e')");
    $db->close();
?>
