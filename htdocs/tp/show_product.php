<?php
$data = file_get_contents('product.json');
$products= json_decode($data,true);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="container">
        <a href="add_product.php"><button>add product</button></a>
        <table>
            <thead>
                <tr>
                    <th>id:</th>
                    <th>nom:</th>
                    <th>price:</th>
                    <th>description:</th>
                </tr>
            </thead>
            <tbody >
                <?php foreach ($products as $product):?>
                    <tr>
                        <td>
                            <?= $product["id"] ?>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <?= $product["nom"] ?>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <?= $product["price"] ?>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <?= $product["description"] ?>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</body>
</html>