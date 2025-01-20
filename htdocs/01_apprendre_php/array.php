<?php
$tab=array("product1","product2","product3");
for($i=0;$i<count($tab);$i++){
    echo $tab[$i]."<br/>";
}



$tab = ["product1","product2","product3"];
for($i=0;$i<count($tab);$i++){
    echo $tab[$i]."<br/>";
}


echo "<h1>boucle while<h1>";


$i=0;
while($i<count($tab)) {
    echo $tab[$i]."<br/>";
    $i +=1;
}


$i=0;
do{
    echo $tab[$i]."<br/>";
    $i+=1;
}while($i<count($tab))



// foreach($tab as $val) {
//     echo $val."<br/>";
// }

$tabs = [ "product1" => "lait", "product2" => "danone", "product3" => "biscouit" ] ;
foreach($tabs as $key => $tab){
    if($key == "product1"){
        echo $tab."<br/>";
    }else {
        echo $key."<br/>";
    }
} 
$tabs = [ "product1" => "lait", "product2" => "danone", "product3" => "biscouit" ] ;
foreach($tabs as $key => $tab){
    if($key == "product1")
        {
        $tabs[$key]== "laitttttttt"
        }
    }



function calculeAge()
?>