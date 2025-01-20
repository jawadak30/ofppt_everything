<?php

require_once "connexion.php";
session_start();
if ($_SESSION["auth"])
    echo "welcome";
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $num_cli = $_POST['num_cli'];
    $matricule = $_POST['matricule'];

    $sql = "SELECT * FROM voiture WHERE matricule='$matricule' AND num_cli = '$num_cli'";

    if ($result = $conn->query($sql)) {
        if ($result->num_rows) {
            $voiture = $result->fetch_assoc();
            $_SESSION['voiture'] = $voiture;
            $_SESSION['auth'] = true;
            header("location:reparation.php");
        } else {
            echo "<script>alert('no user')</script>";
        }
    }


}
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Login</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div>
        <form method="POST">
            <label for="">NumClient</label>
            <input type="text" name="num_cli">
            <label for="">Matricule</label>
            <input type="text" name="matricule">
            <input type="submit" value="Login">
        </form>
    </div>
</body>

</html>