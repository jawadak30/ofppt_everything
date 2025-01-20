function validation_name() {
    let name = document.getElementById('name').value;
    let pernom = document.getElementById('prenom').value;
    let equipe = document.getElementById('equipe').value;
    let valid = /'\w+/;
    if ( name == "" || pernom == "" || equipe == "" ){
        console.log("remplir les champs");
    }else {
        if ( name !== valid || pernom !== valid || equipe !== valid ){
            console.log("vous avez une faute dans le nom ou prénom ou le nom de l'equipe");
        }
    }
}
function validation_code(){
    let code = document.getElementById('code').value;
    let nombre = document.getElementById('nombre').value;
    let reg= /'\d+'/;
    if ( code =="" || nombre =="" ){
        console.log("remplir les champs");
    }else{
        if ( code !== reg || nombre !== reg ){
            console.log("vous avez une faute dans le code ou nombre");
        }
    }
}
function sauvegarder() {
    validation_name();
    validation_code();
}