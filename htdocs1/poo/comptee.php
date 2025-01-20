<?php
include "poo.php";
class comptee extends compte {

    private $taux;
    public function __construct($c,$t,$s,$taux) {
        parent::__construct($c,$t,$s);
        $this->taux = $taux;
    }

    public function __toString() {
        return parent::__toString()."taux :".$this->taux;
        
    }
    public function calculInterets($year) {
        return ($this->get_solde()*(1+$this->taux))*$year;
    }
}

$ct = new comptee(12,20,2,13214123);
echo $ct;

echo "intrets: ".$ct->calculInterets(1221);
?>