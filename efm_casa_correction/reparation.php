<?php

require_once "connexion.php";

session_start();

if (isset($_SESSION['auth']) && $_SESSION['auth']) {
    $voiture = $_SESSION['voiture'];
} else {
    echo "<script>alert('you are not connected')</script>";
}
?>
<!DOCTYPE html>
<html>

<head>
    <title>Reparation</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div>
        <h2>Voiture Info</h2>
        <table>
            <tr>
                <td>Matricule</td>
                <td>Marque</td>
                <td>Annee</td>
                <td>NumClient</td>
            </tr>
            <tr>
                <td><?= $voiture['matricule'] ?></td>
                <td><?= $voiture['marque'] ?></td>
                <td><?= $voiture['annee'] ?></td>
                <td><?= $voiture['num_cli'] ?></td>
            </tr>
        </table>
        <h2>Voiture Historique</h2>
        <?php
        $sql = "SELECT * FROM reparation WHERE matricule =" . $voiture['matricule'];
        ?>
        <?php if ($result = $conn->query($sql)): ?>
            <?php if ($result->num_rows): ?>
                <table>
                    <thead>
                        <tr>
                            <th>NumRep</th>
                            <th>Matricule</th>
                            <th>Description</th>
                            <th>Date</th>
                            <th>Cout</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php while ($row = $result->fetch_assoc()): ?>
                            <tr>
                                <td><?= $row['num_rep'] ?></td>
                                <td><?= $row['matricule'] ?></td>
                                <td><?= $row['description'] ?></td>
                                <td><?= $row['date_rep'] ?></td>
                                <td><?= $row['cout'] ?></td>
                            </tr>
                        <?php endwhile ?>
                    </tbody>
                </table>
            <?php endif ?>
        <?php endif ?>
    </div>
</body>

</html>