<?php

require_once "connexion.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $matricule = $_POST["matricule"];
    $num_cli = $_POST["num_cli"];
    $marque = $_POST["marque"];
    $annee = $_POST["annee"];

    $sql = "UPDATE voiture SET num_cli='$num_cli',marque='$marque',annee='$annee' WHERE matricule = '$matricule'";

    if ($conn->query($sql)) {
        echo "<script>alert('modification est effectuée');window.location.href='listevoiture.php';</script>";
    } else {
        echo "<script>alert('modification est échouée');window.location.href='listevoiture.php';</script>";

    }
}

$matricule = "";
$num_cli = "";
$marque = "";
$annee = "";

if (isset($_GET["matricule"])) {
    $matricule = $_GET["matricule"];

    $sql = "SELECT * FROM voiture WHERE matricule=$matricule";

    if ($result = $conn->query($sql)) {
        $row = $result->fetch_assoc();

        $num_cli = $row["num_cli"];
        $marque = $row["marque"];
        $annee = $row["annee"];
    }
}

?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <title>Modifier Voiture</title>
</head>

<body>
    <div>
        <form method="POST">
            <label for="">NumClient</label>
            <input type="text" name="num_cli" value="<?= $num_cli ?>">
            <label for="">Marque</label>
            <input type="text" name="marque" value="<?= $marque ?>">
            <label for="">Annee</label>
            <input type="text" name="annee" value="<?= $annee ?>">
            <input type="hidden" name="matricule" value="<?= $matricule ?>">
            <input type="submit" value="Modifier">
        </form>
    </div>
</body>

</html>