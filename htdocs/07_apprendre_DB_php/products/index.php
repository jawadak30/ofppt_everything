<html>

<head>
    <link rel="stylesheet" href="../css/product.css" />
    <link rel="stylesheet" href="../css/global.css" />



</head>

<body>
    <?php 
     require_once "../connection.php";
    ?>
    <div class="row">
        <div class="menu">
            <div class="vertical-menu">
                <a href="#" class="">Commandes</a>
                <a href="#" class="active">Products</a>
                <a href="#" class="">Factures</a>

            </div>
        </div>
        <div class="content">
            <div class="flex">
                <a href="add.php" class="btn-primary"> Ajouter produit</a>
                <div>
                    <input type="text" class="filter" />
                    <button class="btn-filter">Filter</button>

                </div>
            </div>

            <div class="result-filter">
                <table class="table">
                    <tr>
                        <th>Ref</th>
                        <th>Designation</th>
                        <th>Prix</th>
                        <th>Qte Stock</th>
                        <th>Actions</th>
                    </tr>
                    <?php
                    $sql="select * from products";
                    $result = $conn->query($sql);

                    if($result->num_rows > 0) {
                        while($row = $result->fetch_assoc()) {
                ?>

                    <tr>
                        <td><?=  $row["ref"] ?></td>
                        <td><?=  $row["designation"] ?></td>
                        <td><?=  $row["prix"] ?></td>
                        <td><?=  $row["qteStock"] ?></td>
                        <td>
                            <a href="edit.php?id=<?=  $row["id"] ?>">edit</a>
                            <a href="delete.php?id=<?=  $row["id"] ?>">delete</a>

                        </td>

                    </tr>
                    <?php }
                    }
                    ?>
                </table>
            </div> <!-- end result-filter -->
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.js"></script>

    <script>
    $(".btn-filter").on("click", function() {
        var filter = $(".filter").val();

        $.ajax({
            type: 'GET',
            url: 'filter.php',
            data: "search=" + filter,
            success: function(response) {
                console.log("response:", response);

                $(".result-filter").html(response);

            }
        })
    });
    $(".filter").on("keyup", function() {
        var filter = $(".filter").val();

        $.ajax({
            type: 'GET',
            url: 'filter.php',
            data: "search=" + filter,
            success: function(response) {
                console.log("response:", response);

                $(".result-filter").html(response);

            }
        })
    })
    </script>

</body>

</html>