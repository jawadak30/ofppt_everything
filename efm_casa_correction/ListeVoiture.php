<?php

require_once "connexion.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $num_cli = $_POST["num_cli"];
    $marque = $_POST["marque"];
    $annee = $_POST["annee"];

    $sql = "INSERT INTO voiture (marque,annee,num_cli) VALUES ('$marque','$annee','$num_cli')";

    $conn->query($sql);
    echo "<script>alert('success')</script>";
}
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Ajouter Voiture</title>
    <link rel="stylesheet" href="style.css">
    <script>
        function deleteconfirmation(id) {
            if (confirm("Do you want to delete this car?")) {
                window.location.href = "supprimervoiture.php?matricule=" + id;
            }
        }
    </script>
</head>

<body>
    <div>
        <form method="POST">
            <label for="">NumClient</label>
            <input type="text" name="num_cli">
            <label for="">Marque</label>
            <input type="text" name="marque">
            <label for="">Annee</label>
            <input type="text" name="annee">
            <input type="submit" value="Ajouter">
        </form>

        <?php $sql = "SELECT * FROM voiture"; ?>
        <?php if ($result = $conn->query("$sql")): ?>
            <?php if ($result->num_rows > 0): ?>
                <h1>Liste des voitures</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Matricule</th>
                            <th>Marque</th>
                            <th>Annee</th>
                            <th>Matricule</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php while ($row = $result->fetch_assoc()): ?>

                            <tr>
                                <td>
                                    <?= $row["matricule"] ?>
                                </td>
                                <td>
                                    <?= $row["marque"] ?>
                                </td>
                                <td>
                                    <?= $row["annee"] ?>
                                </td>
                                <td>
                                    <?= $row["num_cli"] ?>
                                </td>
                                <td>
                                    <a href="modifiervoiture.php?matricule=<?= $row['matricule'] ?>">modifier</a>
                                    <a href="#" onclick="deleteconfirmation(<?= $row['matricule'] ?>)">supprimer</a>
                                </td>
                            </tr>
                        <?php endwhile; ?>
                    </tbody>
                </table>
            <?php endif; ?>
        <?php else: ?>
            echo "Error in executing the query";
        <?php endif; ?>

    </div>
</body>

</html>