<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="autres.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <title>login</title>
</head>
<body>
<?php
        // $verify= "";
        // if($_SERVER['REQUEST_METHOD'] == "POST") {
        //     if (empty(trim($_POST["password"])) || empty(trim($_POST["adresse"])))  {
        //         $verify="something wrong";
        //     } else {
        //         $adresse=$_POST["adresse"];
        //         $password=$_POST["password"];
        //         $jsonData = file_get_contents("data.json");
        //         $products = json_decode($jsonData, true);
        //     }
        // }
    ?>
    <form action="POST" method="POST" >
        <div class="container">
            <div class="box">
                <h1>login</h1>
                <div>
                    <i class="fa-regular fa-circle-user"></i>
                    <input type="text" placeholder="email or phone number" name="adresse">
                </div>
                <div>
                    <i class="fa-solid fa-lock"></i>
                    <input type="password" name="" id="" placeholder="enter password" name="phone">
                </div>
                <div><a href="">forget password?</a></div>
                <div class="button">
                    <input class="log" type="submit" value="login">
                </div>
                <div class="icons">
                    <p>or sign in with:</p>
                    <div id="ic">
                        <i id="google" class="fa-brands fa-google"></i>
                        <i class="fa-brands fa-facebook"></i>
                        <i class="fa-brands fa-twitter"></i>
                    </div>
                </div>
                <div class="sign-up">
                    <p>
                        Not a memeber?
                        <a href="">sign up now</a>
                    </p>
                </div>
            </div>
        </div>
    </form>
</body>
</html>