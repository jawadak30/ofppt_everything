<?php

require "voiture.php";

$v1 = new Voiture(12, "bmw", 2012, 12);

echo $v1->toString();

?>

<a href="listevoiture.php">liste voiture</a>
<a href="connection.php">login</a>