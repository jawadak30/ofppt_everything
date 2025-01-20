<?php
class compte {
    private $code;
    private $solde;
    private $titilaire;

    public static $nombre_comptes= 0;

    public function __construct($c,$s,$t) {
        $this->code = $c;
        $this->solde = $s;
        $this->titilaire = $t;
        self::$nombre_comptes+=1;
    }
    function get_code() {
        return $this->code;
    }
    function get_solde() {
        return $this->solde;
    }
    function get_titilaire() {
        return $this->titilaire;
    }

    function __toString() {
        return "code: ".$this->code."solde:       ".$this->solde."titilaire:       ".$this->titilaire;
    }
}

// $compte = new compte(12,12,"good");
// echo $compte->to_string();

?>