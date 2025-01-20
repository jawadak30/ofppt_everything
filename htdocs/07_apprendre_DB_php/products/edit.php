<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>add product</title>

    <link rel="stylesheet" href="../css/global.css" />

</head>

<body>

    <?php 

    
     require_once "../connection.php";

     if($_SERVER["REQUEST_METHOD"] == "POST") {
        $id= $_POST["id"];
        $ref= $_POST["ref"];
        $designation= $_POST["designation"];
        $prix= $_POST["prix"];
        $qteStock= $_POST["qteStock"];
        $sql="update products set ref='$ref', designation='$designation',prix='$prix',qteStock='$qteStock' where id='$id'";
        if($conn->query($sql) === TRUE) {
            header("Location: index.php");
        }else {
            echo "error updating product".$conn->error;
        }

     } elseif(isset($_GET["id"])) {
        $id= $_GET["id"];
        $sql = "select * from products where id=$id";
        $result = $conn->query($sql);

        $product = $result->fetch_assoc();
    }



    

    ?>

    <h2>edit un produit</h2>
    <form method="post">
        <input type="hidden" name="id" value="<?= $product['id'] ?>" />
        <label>Référence</label><br />
        <input type="text" name="ref" value="<?= $product['ref'] ?>" /><br />
        <label>Designation</label><br />
        <input type="text" name="designation" value="<?= $product['designation'] ?>" /><br />
        <label>Prix</label><br />
        <input type="text" name="prix" value="<?= $product['prix'] ?>" /><br />
        <label>Qte Stock</label><br />
        <input type="text" name="qteStock" value="<?= $product['qteStock'] ?>" /><br />

        <input type="submit" class="btn-primary" name="submit" value="Modifier" />
    </form>



</body>

</html>