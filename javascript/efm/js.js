function validation() {
    function validation_of_tv() {
        let text= document.getElementById('selectTVs').value;
        if (text == ""){
            alert("selectioné une tv");
        }
    }
    validation_of_tv();
    function validation_of_quantité() {
        var quantité = document.getElementById('number').value;
        if (Number(quantité)<1 || Number(quantité)>10)  {
            alert("laquantité doit etre enter 1 et 10 ");
        }
    }
    validation_of_quantité();
}
var jsonTVs= {
    tvs: [
        {
            nom:"SAMSUNG QLED QE65Q80AA",
            prix: 17999,
            taille:65,
            image: "",
        },
        {
            nom: "TCL QLED 55C825",
            prix: 6100,
            taille: 42,
            image: "images/img2.png",
          },
          {
            nom: "SONY OLED XR-75X90J",
            prix: 25000,
            taille: 52,
            image: "images/img3.png",
          },
          {
            nom: "LG OLED 77C1PVA",
            prix: 9000,
            taille: 65,
            image: "images/img4.jpg",
          },
    ],
};

function remplirTVs() {
    let selectionTV = document.getElementById('selectTVs');
    jsonTVs.tvs.forEach(tv => {
        let option= document.createElement("option");
        option.textContent = tv.nom;
        selectionTV.append(option); 
    });
};
remplirTVs();



function ajouterAuPanier(){
    validation();
    var panier = document.getElementById('selectTVs').value;
    var qt = document.getElementById('number').value;
    jsonTVs.tvs.forEach(element => {
        let ref= document.getElementById('references');
        let quantité = document.getElementById('quantité');
        if (element.nom == panier){
            ref.textContent= element.nom ;
            quantité.textContent= qt;
        }
    });
}
