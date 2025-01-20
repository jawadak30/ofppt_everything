<?php
echo "name is: ".$_POST["name"];
if (isset($_POST["age"])) {
    echo " </br> exist : ".$_POST["age"];

}else {
    echo " n'exist pas : ";
}


//something else: 
    // ??: like isset

    // $test = $_POST["name"] ?? '';
    // echo " </br> exist : ".$test;

    // end of something else