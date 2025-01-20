<?php 

$servername = "localhost";
$username = "root";
$password = "";
$database = "products";

$conn = new mysqli($servername, $username, $password, $database);

// verifier la connextion
if($conn->connect_error) {
    die("error connexion :".$conn->connect_error);
} 