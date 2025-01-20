<?php 

require_once "../connection.php";
if(isset($_GET["search"])) {
    $search = $_GET["search"];
    $sql= "select * from products where ref like '%$search%' order by id desc";
    $result = $conn->query($sql);
    ?>
<table class="table">
    <tr>
        <th>Ref</th>
        <th>Designation</th>
        <th>Prix</th>
        <th>Qte Stock</th>
        <th>Actions</th>
    </tr>
    <?php if($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) { ?>
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
    <?php
        } } else {
            echo '<tr><td colspan="5"> no data </td></tr>';
        }

        

    echo "</table>";

}