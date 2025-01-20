<?php

class Voiture
{
    private $matricule;
    private $marque;
    private $annee;
    private $numClient;

    public function __construct($matricule, $marque, $annee, $numClient)
    {
        $this->matricule = $matricule;
        $this->marque = $marque;
        $this->annee = $annee;
        $this->numClient = $numClient;
    }

    public function getMatricule()
    {
        return $this->matricule;
    }
    public function getMarque()
    {
        return $this->marque;
    }
    public function getAnnee()
    {
        return $this->annee;
    }
    public function getNumClient()
    {
        return $this->numClient;
    }
    public function toString()
    {
        return "<pre>" . $this->matricule . "\t" . $this->marque . "\t" . $this->annee . "\t" . $this->numClient . "</pre>";
    }
}