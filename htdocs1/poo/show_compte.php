<?php 
include "poo.php";
$compte = new compte(12,12,"good");
echo $compte->to_string();

$compte = new compte(12,12,"good");
echo $compte->to_string();

$compte = new compte(13,1,"good");
echo $compte->to_string();

echo "nombre des comptes : ".compte::$nombre_comptes ;

?>