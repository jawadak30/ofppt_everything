<?php

require_once "connexion.php";

if (isset($_GET["matricule"])) {
    $matricule = $_GET["matricule"];
    $sql = "DELETE FROM voiture WHERE matricule=$matricule";
    if ($conn->query($sql)) {
        header("location:listevoiture.php");
    }
}