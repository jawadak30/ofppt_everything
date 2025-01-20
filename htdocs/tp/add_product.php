<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="add_product.css">
    <title>Document</title>
</head>
<body>
    <?php
        $id = "";
        $nom = "";
        $price = "";
        $description = "";
        $idd = "";
        $nomm = "";
        $pricee = "";
        $descriptionn = "";
        $verify_id ="enter id";
        $verify_nom ="enter nom";
        $verify_price ="enter price";
        $verify_description ="enter description";
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $valid = true;
            if (empty(trim($_POST['id']))) {
                $idd = $verify_id;
                $valid = false;
            }
            else{
                $id= $_POST['id'];
            }
            if (empty(trim($_POST['nom']))) {
                $nomm = $verify_nom;
                $valid = false;
            }
            else{
                $nom= $_POST['nom'];
            }            
            if (empty(trim($_POST['price']))) {
                $pricee = $verify_price;
                $valid = false;
            }
            else{
                $price= $_POST['price'];
            }
            if (empty(trim($_POST['description']))) {
                $descriptionn = $verify_description;
                $valid = false;
            }
            else{
                $description= $_POST['description'];
            }
            if ($valid){

                $jsonData = file_get_contents("product.json");

                $allData = json_decode($jsonData, true);
        
                $formData = ["id" => $_POST['id'],"nom" => $_POST['nom'],"price" => $_POST['price'],"description" => $_POST['description']];
        
                $allData[] = $formData;
                $jsonData = json_encode($allData);
        
                $filename = "product.json";
        
                $result = file_put_contents($filename, $jsonData);
            }
        }
        
    ?>
    <form method="POST">
        <div class="box">
                <div class="id">
                    <label for="">id:</label>
                    <input type="text" name="id">
                    <?php echo $idd;?>
                </div>
                <div class="nom">
                    <label for="">nom:</label>
                    <input type="text" name="nom">
                    <?php echo $nomm; ?>
                </div>
                <div class="id">
                    <label for="">price:</label>
                    <input type="number" name="price" min="0" >
                    <?php echo $pricee;?>
                </div>
                <div class="id">
                    <label for="">description:</label>
                    <textarea name="description" id="" cols="30" rows="10"></textarea>
                    <?php echo $descriptionn;?>
                </div>
                <input type="submit" value="add product">
                <input type="reset" value="reset anything">
        </div>
    </form>
    <a href="show_product.php"><button>product list</button></a>
</body>
</html>