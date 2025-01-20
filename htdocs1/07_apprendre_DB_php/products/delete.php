<?php

require_once "../connection.php";

if(isset($_GET["id"])) {
    $id = $_GET["id"];

    $sql="delete from products where id='$id'";
    if($conn->query($sql) === TRUE) {
        header("Location: index.php");
    } else {
        echo "error deleting product".$conn->error;
    }
}