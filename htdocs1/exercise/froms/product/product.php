<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="product.css">
    <title>Document</title>
</head>
<body>
    <form action="" method="post">
        <label>Référence</label><br />
        <input type="text" name="referece" /><br />
        <label>Designation</label><br />
        <input type="text" name="designation" /><br />
        <label>Prix</label><br />
        <input type="text" name="prix" /><br />
        <label>Qte Stock</label><br />
        <input type="text" name="qteStock" /><br />

        <input type="submit" class="btn-primary" name="submit" value="Ajouter" />
    </form>
    <?php 

    if($_SERVER["REQUEST_METHOD"] == "POST") {
        $referece = $_POST["referece"];
        $designation = $_POST["designation"];
        $prix = $_POST["prix"];
        $qteStock = $_POST["qteStock"];

        $product=[$referece,$designation,$prix,$qteStock];
        $products[]=$product;
        print_r($product);
        foreach ($products as $product){
            
        }
        
    }

    ?>
    <script src="product.js"></script>
</body>
</html>