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

    <h2>Ajouter un produit</h2>
    <form method="post">
        <label>Référence</label><br />
        <input type="text" name="ref" /><br />
        <label>Designation</label><br />
        <input type="text" name="designation" /><br />
        <label>Prix</label><br />
        <input type="text" name="prix" /><br />
        <label>Qte Stock</label><br />
        <input type="text" name="qteStock" /><br />

        <input type="submit" class="btn-primary" name="submit" value="Ajouter" />
    </form>


    <?php 
     require_once "../connection.php";

     if($_SERVER["REQUEST_METHOD"] == "POST") {
        $ref = $_POST["ref"];
        $designation = $_POST["designation"];
        $prix = $_POST["prix"];
        $qteStock = $_POST["qteStock"];

        $sql="insert into products (ref, designation,prix,qteStock) values('$ref','$designation','$prix','$qteStock')";

        if($conn->query($sql) === TRUE) {
            header("Location: index.php");
        } else{
            echo "error lors l'ajout product";
        }

     }

    ?>
</body>

</html>