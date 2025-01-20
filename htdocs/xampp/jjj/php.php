<?php

$product_name = "";
$product_category = "";
$product_condition = "";
$product_price = "";
$product_description = "";

$successMessage = "";

$messages["product_name_error"] = '';
$messages["product_category_error"] = '';
$messages["product_condition_error"] = '';
$messages["product_price_error"] = '';
$messages["product_description_error"] = '';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Print the POST array
    $isValid = true;
    if (empty($_POST['product_name'])) {
        $messages["product_name_error"] = '<div class="form-text text-danger">
        Enter a valid name
      </div>';
        $isValid = false;
    } else {
        $product_name = $_POST['product_name'];
    }
    if (!isset($_POST['product_category'])) {
        $messages["product_category_error"] = '<div class="form-text text-danger">
        Choose a category
      </div>';
        $isValid = false;
    } else {
        $product_category = $_POST['product_category'];
    }
    if (!isset($_POST['product_condition'])) {
        $messages["product_condition_error"] = '<div class="form-text text-danger">
        Choose a condition
      </div>';
        $isValid = false;
    } else {
        $product_condition = $_POST['product_condition'];
    }
    if (empty($_POST['product_price'])) {
        $messages["product_price_error"] = '<div class="form-text text-danger">
        Enter a valid price
      </div>';
        $isValid = false;
    } else {
        $product_price = $_POST['product_price'];
    }
    if (empty($_POST['product_description'])) {
        $messages["product_description_error"] = '<div class="form-text text-danger">
        Enter a description
      </div>';
        $isValid = false;
    } else {

        $product_description = $_POST['product_description'];
    }
    if ($isValid) {

        $jsonData = file_get_contents("products.json");

        $allData = json_decode($jsonData, true);

        $formData = ["product_name" => $product_name, "product_category" => $product_category, "product_condition" => $product_condition, "product_price" => $product_price, "product_description" => $product_description];

        $allData[] = $formData;

        $jsonData = json_encode($allData);

        $filename = "products.json";

        $result = file_put_contents($filename, $jsonData);

        if ($result) {
            $successMessage = '<div class="alert alert-success">Product added with success!</div>';
        } else {
            $successMessage = '<div class="alert alert-danger">Problem when adding the product!</div>';
        }

        $product_name = "";
        $product_category = "";
        $product_condition = "";
        $product_price = "";
        $product_description = "";
    }
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Add Product</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous" />
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</head>

<body>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col col-md-6">
                <div class="d-flex justify-content-between align-items-center my-5">
                    <h2>Add New Product</h2>
                    <a href="show_products.php" class="btn btn-primary">Show Products</a>
                </div>
                <?php echo $successMessage; ?>
                <!-- form -->
                <form method="post" class="p-3 border rounded">
                    <!-- product name -->
                    <div class="mb-3">
                        <label for="product_name" class="form-label">Product Name</label>
                        <input type="text" name="product_name" id="product_name" class="form-control"
                            value="<?php echo $product_name ?>" placeholder="Product Name" />
                        <?php echo $messages["product_name_error"]; ?>
                    </div>
                    <!-- product category -->
                    <div class="mb-3">
                        <label for="product_category" class="form-label">Product Category</label>
                        <select class="form-select" name="product_category" id="product_category">
                            <option selected disabled>Choose category</option>
                            <option value="electronics" <?php if ($product_category == "electronics")
                                echo "selected" ?>>Electronics</option>
                                <option value="clothes" <?php if ($product_category == "clothes")
                                echo "selected" ?>>Clothes</option>
                                <option value="toys" <?php if ($product_category == "toys")
                                echo "selected" ?>>Toys</option>
                                <option value="tools" <?php if ($product_category == "tools")
                                echo "selected" ?>>Tools</option>
                            </select>
                        <?php echo $messages["product_category_error"]; ?>
                    </div>
                    <!-- product condition -->
                    <div class="mb-3">
                        <label class="form-label me-5">Product Condition</label>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" name="product_condition" id="radio_option1"
                                value="new" <?php if ($product_condition == "new")
                                    echo "checked" ?> />
                                <label class="form-check-label" for="radio_option1">New</label>
                            </div>
                            <div class="form-check form-check-inline">
                                <input class="form-check-input" type="radio" name="product_condition" id="radio_option2"
                                    value="used" <?php if ($product_condition == "used")
                                    echo "checked" ?> />
                                <label class="form-check-label" for="radio_option2">Used</label>
                            </div>
                        <?php echo "<br>" . $messages["product_condition_error"]; ?>
                    </div>
                    <!-- product price -->
                    <div class="mb-3">
                        <label for="product_price" class="form-label">Product Price</label>
                        <div class="input-group mb-3">
                            <span class="input-group-text">$</span>
                            <input type="number" class="form-control" id="product_price" name="product_price"
                                value="<?php echo $product_price; ?>" placeholder="00.00" />
                        </div>
                        <?php echo $messages["product_price_error"]; ?>
                    </div>
                    <!-- product description  -->
                    <div class="mb-3">
                        <label for="product_description" class="form-label">Product Description</label>
                        <textarea class="form-control" id="product_description" name="product_description" rows="3"
                            placeholder="Product Description"><?php echo $product_description; ?></textarea>
                        <?php echo $messages["product_description_error"]; ?>
                    </div>
                    <button type="submit" class="btn btn-primary">Add Product</button>
                    <button type="button" onclick="fillForm()" class="btn btn-secondary">
                        AutoFill
                    </button>
                </form>
            </div>
        </div>
    </div>
    <script>
        const form = document.querySelector("form");
        function fillForm() {
            form.elements["product_name"].value = "test";
            form.elements["product_category"].value = "electronics";
            form.elements["product_condition"].value = "new";
            form.elements["product_price"].value = "12.00";
            form.elements["product_description"].value =
                "Ut ad do aute eiusmod sint tempor esse nulla enim duis quis.";
        }
    </script>
</body>

</html>