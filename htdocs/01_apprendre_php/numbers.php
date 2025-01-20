<?php
$a=5;
$b=5.22;
$c="30";
echo $a+$c;
var_dump($a);
var_dump($b);
var_dump($c);
var_dump(intval($c));
echo "</hr> ";
echo min(100,10,-50,23)."</br>";
echo max(100,10,-50,23)."</br>";
// round //
echo "round(0.6):".round(0.6)."</br>";
echo "round(0.5):".round(0.5)."</br>";
echo "round(0.49):".round(0.49)."</br>";
echo "round(-4.40):".round(-4.40)."</br>";
echo "round(-5.40):".round(-5.40)."</br>";
echo "ceil:".ceil(-5.1)."</br>";
echo "ceil:".floor(-5.1)."</br>";
echo "ceil:".rand()."</br>";
?>