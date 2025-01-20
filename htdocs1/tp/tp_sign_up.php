<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="tp_sign_up.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>sign up</title>
</head>
<body>
    <?php
    $verify="";
    $verify_code="";
        if($_SERVER['REQUEST_METHOD'] == "POST") {
            if (empty(trim($_POST["first_name"])) || 
            empty(trim($_POST["last_name"]))  ||
             empty(trim($_POST["adresse"]))  ||
              empty(trim($_POST["password"]))  ||
               empty(trim($_POST["confirm_password"]))  ||
                empty(trim($_POST["phone"]))) {
                $verify="something wrong";
            } else {
                $first_name=$_POST["first_name"];
                $last_name=$_POST["last_name"];
                $adresse=$_POST["adresse"];
                $password=$_POST["password"];
                $confirm_password=$_POST["confirm_password"];
                $phone=$_POST["phone"];
                if ($password !== $confirm_password) {
                    $verify_code= "codes aren't th same";
                }else {
                    $password=$_POST["password"];

                    $confirm_password=$_POST["confirm_password"];  
                }
                $jsonData = file_get_contents("data.json");

                $allData = json_decode($jsonData, true);
        
                $formData = ["first_name" => $first_name, "last_name" => $last_name, "adresse" => $adresse, "password" => $password, "confirm_password" => $confirm_password , "phone" => $phone];
        
                $allData[] = $formData;
        
                $jsonData = json_encode($allData);
        
                $filename = "data.json";
        
                $result = file_put_contents($filename, $jsonData);
            }
        }
    ?>
    <form  method="post">
        <div class="container">
            <div class="box">
                <h1>sign up </h1>
                <div>
                    <label for="aa">first name:</label>
                    <input type="text"  id="aa"  name="first_name">
                </div>
                <div>
                    <label for="aaa">last name:</label>
                    <input type="text"  id="aaa" name="last_name">
                </div>
                <!-- <div>
                    <label>select trade role:</label>
                    <div class="inside" >
                        <label for="ja">buyer</label>
                        <input type="radio" name="role" id="ja" >
                        <label for="jaa">seller</label>
                        <input type="radio" name="role" id="jaa" >
                        <label for="jaaa">both</label>
                        <input type="radio" name="role" id="jaaa" >
                    </div>
                </div> -->
                <div>
                    <label for="aaaa">amail adresse:</label>
                    <input type="text" placeholder="please set the email adresse" id="aaaa" name="adresse" >
                </div>
                <div>
                    <label for="aaaaa">login password:</label>
                    <input min="8" type="text" placeholder="set password" id="aaaaa" name="password">
                    <?php echo $verify_code; ?>
                </div>
                <div>
                    <label for="jj">confirm password:</label>
                    <input min="8" type="text" placeholder="set password" id="jj" name="confirm_password">
                    <?php echo $verify_code; ?>
                </div>
                <div>
                    <label for="jjj">phone number:</label>
                    <input type="tel" id="jjj" placeholder="enter phone number " name="phone">
                </div>
                <div>
                    <input class="sub" type="submit" value="submit">
                    <input class="res" type="reset" value="reset">
                </div>
            </div>
        </div>
        <?php echo $verify; ?>
    </form>
</body>
</html>