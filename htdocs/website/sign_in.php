<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="sing_up.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
    <title>worldcome</title>
</head>
<body>
    <?php include "head.php"; ?>
        <form action="">
            <div class="container">
                <div class="logo">
                    <h1>world <span>come</span></h1>
                </div>
                <div class="email">
                    <i for="email" class="fa-solid fa-user"></i>
                    <input type="text" id="email" >
                </div>
                <div class="ja">
                    <div class="password">
                        <i for="password" class="fa-solid fa-lock"></i>
                        <input type="password" name="" id="password" >
                    </div>
                    <p><a href="">forgot password?</a></p>
                </div>
                <button id="button" type="submit" onclick="validateemail()"> login</button>
                <div class="sign_in" >
                    <p>Didn't have a account?<a href="">create account</a></p>
                </div>
            </div>
            <script src="sing_up.js"></script>
        </form>
    <?php include "footer.php"; ?>
</body>
</html>