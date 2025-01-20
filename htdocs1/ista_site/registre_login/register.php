<?php
include "connection.php";
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
            header("location: index.php");
        }else {
            echo "error:".$conn->error;
        }
    }
}





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
        header("location:ista_site/landign_page/landing_page.php");
        exit();
    }else{
        echo "not found, incorrect email or password";
    }
}
?>