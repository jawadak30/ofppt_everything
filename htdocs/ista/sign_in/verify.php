<?php
include "C:/xampp/htdocs/ista/connextion_with_data/connection.php";
if (isset($_POST['sign_in'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];
    $password = md5($password);
    $sql = "SELECT * from users where email='$email' and password='$password' ";
    $result= $conn->query($sql);
    if ($result->num_rows>0) {
        session_start();
        $row=$result->fetch_assoc();
        $_SESSION['email']=$row['email'];
        header("location:/ista/landing/landing_page.php");
        exit();
    }else{
        echo "not found, incorrect email or password";
    }
}
?>