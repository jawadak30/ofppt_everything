<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="index.css">
    <title>Document</title>
</head>
<body>
    <div class="container" id="signup" >
        <h1 class="form_title">register</h1>
        <form action="register.php" method="post">
            <div class="input_groupe">
                <i class="fas fa-user"></i>
                <input type="text" name="first_name" id="first_name" placeholder="first name">
            </div>
            <div class="input_groupe">
                <i class="fas fa-user"></i>
                <input type="text" name="last_name" id="last_name" placeholder="last name">
            </div>
            <div class="input_groupe">
                <i class="fas fa-user"></i>
                <input type="email" name="email" id="email" placeholder="first email">
            </div>
            <div class="input_groupe">
                <i class="fas fa-user"></i>
                <input type="tel" name="phone_number" id="phone_number" placeholder="phone number">
            </div>
            <div class="input_groupe">
                <i class="fas fa-user"></i>
                <input type="password" name="password" id="password" placeholder="password">
            </div>
            <div class="input_groupe">
                <i class="fas fa-user"></i>
                <input type="password" name="confirm_password" id="password" placeholder="confirm_password">
            </div>
            <input type="submit" class="btn" value="sign up" name="sign_up"/>
            <div class="links">
                <p>already have account?</p>
                <a href="sign_in.php"><button id="sign_in_button" onclick="">sign in</button></a>
            </div>
        </form>

    </div>
    <script src="index.js"></script>
</body>
</html>