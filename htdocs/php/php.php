<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <?php
    $nameReq= "";
    $name="";
    $age="";
    $ageVIDE="";
    if($_SERVER['REQUEST_METHOD'] == "POST") {
        if (empty(trim($_POST["name"])) && empty(trim($_POST["age"]))) {
            $nameReq="name is required";
            $ageVIDE="please enter age";
        } else {
            $name=$_POST["name"];
            if (($_POST["age"])<18) {
                $ageVIDE = "you are not allowed $age ";
            }else {
                $age = $_POST["age"];
            }
            
        }
    }
    ?>

    <form action="test-php.php" method="POST" >
            name: <input type="text " name="name">
            <span class="required">*<?php echo $nameReq; ?></span>
            <span class="value">   value: <?php echo $name; ?></span>
            age: <input type="number" name="age">
            <span >*<?php echo $ageVIDE; ?></span>
            <span>    value: <?php echo $age; ?></span>
            <input type="submit" value="valider">
    </form>
</body>
</html>