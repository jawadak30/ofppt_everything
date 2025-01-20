<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="index.css">
    <title>Document</title>
</head>
<body>
    
    <div class="container" id="signin" >
        <h1 class="form_title">sign in</h1>
        <form action="register.php" method="post">
                    <div class="input_groupe">
                        <i class="fas fa-user"></i>
                        <input type="email" name="email" id="email" placeholder="first email">
                    </div>
                    <div class="input_groupe">
                        <i class="fas fa-user"></i>
                        <input type="password" name="password" id="password" placeholder="password">
                    </div>
                    <p class="recover-password">
                        <a href="#">recover password</a>
                    </p>
                    <input type="submit" class="btn" value="sign in" name="sign_in"/>
                    <div class="links">
                        <p>Don't have account yet?</p>
                        <a href="index.php"><button id="sign_up_button">sign up</button></a>
                    </div>
                </form>
    </div>
    <script src="index.js"></script>
</body>
</html>