<?php
$servername = "localhost";
$username = "root";
$password  = "";
$database = "products";

$conn = new mysqli($servername,$username,$password,$database);

if ($conn->connect_error) {
    die ("error connexion :".$conn->connect_error);
}