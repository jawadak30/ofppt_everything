<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="sign_in.css">
    <title>Document</title>
</head>
<body>
    
    <div class="container" id="signin" >
        <h1 class="form_title">sign in</h1>
        <form action="verify.php"  method="post">
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
                        <a href="/ista/sign_up/sign_up.php" target="_blank"><button>sign up</button></a>
                    </div>
                </form>
    </div>
    <script src="/ista/sign_in/sign_in.js"></script>
</body>
</html>