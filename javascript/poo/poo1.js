//Création d'un string JSON
var jsonData = '{"nom":"Saidi", "prenom":"Ali"}';
document.write(typeof(jsonData)+'<br>'); //string
//Convertir JSON vers Javascript
var jsObject = JSON.parse(jsonData);
document.write(typeof(jsObject)+'<br>');//object
document.write(jsObject+'<br>'); //[object object]
document.write(jsObject.nom + ""+jsObject.prenom+'<br>'); //Saidi Ali