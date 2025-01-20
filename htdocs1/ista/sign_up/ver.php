<?php
include "C:/xampp/htdocs/ista/connextion_with_data/connection.php";
if(isset($_POST['sign_up'])){
    $first_name =$_POST['first_name'];
    $last_name =$_POST['last_name'];
    $email =$_POST['email'];
    $phone_number =$_POST['phone_number'];
    $password =$_POST['password'];
    $password =md5($password);


    $checkemail = "SELECT * FROM users where email='$email'";
    $result=$conn->query($checkemail);
    if ($result->num_rows>0) {
        echo "email adress exist !";
    }else{
        $insert_data = "INSERT into users(first_name,last_name,email,phone_number,password)
        VALUES('$first_name','$last_name','$email','$phone_number','$password')";
        if($conn->query($insert_data) == true){
            header("location: /ista/landing/landing_page.php");
        }else {
            echo "error:".$conn->error;
        }
    }
}
?>
