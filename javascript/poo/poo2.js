//Création d'un objet Javascript
var jsObject = {nom:"Saidi", prenom:"ali"};
document.write(typeof(jsObject)+'<br>');//Object
//Convertir javascript vers JSON
var jsonString = JSON.stringify(jsObject);
document.write(typeof(jsonString)+'<br>');//string
document.write(jsonString);//{"nom":"Saidi","prenom":"ali"}
//remarquer la présence des "" dans les clés