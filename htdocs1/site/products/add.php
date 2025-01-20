<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/add.css">
</head>
<body>
    <h2>ajouter un produit </h2>
    <form action="" method="post">
        <label for="">id</label>
        <input type="text" name="id"> <br>
        <label for="">designation</label>
        <input type="text" name="designation"> <br>
        <label for="">prix</label>
        <input type="text" name="prix"> <br>
        <label for="">qte stock</label>
        <input type="text" name="qtestock"> <br>
        <input type="submit" value="ajouter" name="submit">
    </form>



    <?php
        require "connection.php";
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $id = $_POST["id"];
            $designation = $_POST["designation"];
            $prix = $_POST["prix"];
            $qtestock = $_POST["qtestock"];
            $sql = "insert into product (id,designation,prix,qtestock) values('$id','$designation','$prix','$qtestock') " ;
            if ($conn->query($sql) === TRUE){
                header("location: index.php");
            }else {
                "error";
            }
        }
    ?>
</body>
</html>
