<?php


class voiture{
    public $matricule ;
    public $marque ;
        public $model;
        public $color;
    public function __construct($matricule,$marque,$model,$color) {
        $this->matricule = $matricule;
        $this->marque = $marque;
        $this->model = $model;
        $this->color = $color;
    }

    // public function set_matricule($matricule) {
    //     $this->$matricule= $matricule;
    // }
    // public function get_matricule(){
    //     return $this->$matricule;
    // }
    // public function set_marque($marque) {
    //     $this->$marque= $marque;
    // }
    // public function get_marque(){
    //     return $this->$marque;
    // }
    // public function set_model($model) {
    //     $this->$model= $model;
    // }
    // public function get_moedel(){
    //     return $this->$model;
    // }
    // public function set_color($color) {
    //     $this->$color= $color;
    // }
    // public function get_color(){
    //     return $this->$color;
    // }
    public function toString(){
        return "la marque est: ".$this->marque."le model est: ".$this->model."le matricule est: ".$this->matricule."color".$this->color;
    }
}

class voiture extends car {
    function toString(){
        return "la marque est: ".$this->marque."le model est: ".$this->model."le matricule est: ".$this->matricule."color".$this->color;
    }
}
$audi = new voiture("audi01","audi",2005,"black");

// $audi = new voiture("audi01","audi",2005,"black");
echo $audi-> toString();
// echo "audi: ".$audi-> get_matricule();

// $renault = new voiture("renault01","renault",2010,"red");
// $renault -> set_matricule("renault01");
// $renault -> set_marque("renault");
// $renault -> set_model("2010");
// $renault -> set_color("red");

// echo "renault: ".$renault-> get_matricule();


?>