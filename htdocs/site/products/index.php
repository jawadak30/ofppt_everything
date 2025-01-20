
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="..\css\index.css">
</head>
<body>

    <div class="row">
        <div class="menu">
            <div class="verticale-menu">
                <a href="#" class="active">commandse</a>
                <a href="#" class="active">products</a>
                <a href="#" class="active">factures</a>
            </div>
        </div>
        <div class="content">
            <table>
                <tr>
                    <th>id: </th>
                    <th>designation: </th>
                    <th>prix: </th>
                    <th>qte stock: </th>
                </tr>
                <?php
                require "connection.php";

                $sql = "select * from product";
                $result  = $conn->query($sql);
                if ($result-> num_rows > 0){
                    while($row = $result->fetch_assoc()) {

                ?>
                <tr>
                    <td><?= $row["id"] ?></td>
                    <td><?= $row["designation"] ?></td>
                    <td><?= $row["prix"] ?></td>
                    <td><?= $row["qtestock"] ?></td>
                </tr> 
                <?php }
                    }
                    ?>
            </table>
        </div>
        <a class="ajouter" href="add.php"><button>ajouter produit</button></a>
    </div>
</body>
</html>