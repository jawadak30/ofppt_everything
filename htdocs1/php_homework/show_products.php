<?php

$jsonData = file_get_contents("products.json");

$products = json_decode($jsonData, true);

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Show Products</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous" />
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</head>

<body>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col col-md-9">
                <div class="d-flex justify-content-between align-items-center my-5">
                    <h2>Products List</h2>
                    <a href="create_product.php" class="btn btn-primary">Add Products</a>
                </div>
                <?php if (isset($products)): ?>
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Category</th>
                                <th>Condition</th>
                                <th>Price</th>
                                <th>Description</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($products as $product): ?>
                                <tr>
                                    <td>
                                        <?= $product["product_name"] ?>
                                    </td>
                                    <td>
                                        <?= $product["product_category"] ?>
                                    </td>
                                    <td>
                                        <?= $product["product_condition"] ?>
                                    </td>
                                    <td>
                                        <?= $product["product_price"] . "$" ?>
                                    </td>
                                    <td>
                                        <?= $product["product_description"] ?>
                                    </td>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                <?php else: ?>
                    <div class="alert alert-warning" role="alert">
                        Oops! There are no products in the database!
                    </div>
                <?php endif; ?>
            </div>
        </div>
    </div>
</body>

</html>